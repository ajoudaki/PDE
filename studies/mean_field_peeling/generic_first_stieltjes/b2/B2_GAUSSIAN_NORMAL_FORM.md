# Gaussian normal form for two hidden layers and two inputs

**Status:** explicit contracted Gaussian normal form; exact finite-width source
identity and independent polynomial regression gates passed  
**Date:** 2026-08-18  
**Observable:** \(g_c=c^Tf\), \(D_c=n\nabla g_c\mathbin\cdot\nabla\),
and \(C_c=\lim_{n\to\infty}\mathbb E[D_c^3g_c]\)  
**Geometry:** arbitrary deterministic \(c\in\mathbb R^2\) and arbitrary
positive-semidefinite \(Q^0\in\mathbb R^{2\times2}\)

This note completes the Gaussian/response peel of
[`FINITE_WIDTH_DIRECTIONAL_PROGRAM.md`](FINITE_WIDTH_DIRECTIONAL_PROGRAM.md).
The terminal formulas contain only finite Gaussian expectations of
\(\phi,\phi',\phi'',\phi'''\) at the two first-layer coordinates or the two
top-layer coordinates.  There is no Hermite approximation, random weight,
neuron sum, auxiliary Gaussian field, unresolved response variable, or
covariance inverse in the final answer.

## 1. Literal atom grammar

Let \(I=\{1,2\}\).  For every PSD \(2\)-by-\(2\) matrix \(Q\), index word
\({\bf i}=(i_1,\ldots,i_m)\in I^m\), and derivative word
\({\bf r}=(r_1,\ldots,r_m)\in\{0,1,2,3\}^m\), define

\[
 \mathcal I_Q({\bf i};{\bf r})
 :=\mathbb E_{G\sim N(0,Q)}
   \prod_{k=1}^m\phi^{(r_k)}(G_{i_k}).
\tag{1.1}
\]

Equation (1.1) is defined by the Gaussian pushforward measure, including when
\(Q\) is singular; no density and no \(Q^{-1}\) are used.  Empty products
equal one.

Take

\[
 U\sim N(0,Q^0),\qquad x_{r,a}=\phi^{(r)}(U_a),
\tag{1.2}
\]

and define the deterministic first hidden Gram

\[
 Q^1_{ab}=\mathbb E_U[x_{0,a}x_{0,b}]
 =\mathcal I_{Q^0}((a,b);(0,0)).
\tag{1.3}
\]

Next take \(Z\sim N(0,Q^1)\), put
\(y_{r,a}=\phi^{(r)}(Z_a)\), and define

\[
 Q^2_{ab}=\mathbb E_Z[y_{0,a}y_{0,b}],\qquad
 E^1_{ab}=\mathbb E_U[x_{1,a}x_{1,b}],\qquad
 E^2_{ab}=\mathbb E_Z[y_{1,a}y_{1,b}].
\tag{1.4}
\]

Every expectation below is an instance of (1.1).  Products of deterministic
expectations and finite sums of atoms are allowed.  Thus (1.1)--(1.4) are a
literal finite grammar, not shorthand for a stochastic limiting process.

## 2. First tangent and directional NTK

Define the top-source covariance, first transpose response, and total first
tangent response by

\[
 \mathsf D_{ab}=c_ac_bE^2_{ab},
 \qquad
 \mathsf L_{ab}=Q^0_{ab}E^1_{ab},
 \qquad
 \mathsf K_{ab}=Q^1_{ab}+\mathsf L_{ab}.
\tag{2.1}
\]

Both \(\mathsf L\) and \(\mathsf K\) are symmetric.  The directional NTK
coefficient is

\[
 \boxed{
 A_c
 =\sum_{a,b\in I}c_ac_bQ^2_{ab}
  +\sum_{a,b\in I}\mathsf D_{ab}\mathsf K_{ab}
 =\sum_{a,b\in I}c_ac_b
  \bigl(Q^2_{ab}+Q^1_{ab}E^2_{ab}
       +Q^0_{ab}E^1_{ab}E^2_{ab}\bigr).}
\tag{2.2}
\]

The \(\mathsf L\) term is the same-row/Onsager sector of the middle matrix.
It cannot be deleted by treating a multiplication by \(W\) after a
multiplication by \(W^T\) as fresh.

## 3. Fully contracted bottom-layer coefficients

The following three deterministic arrays contain every bottom-layer quantity
that survives in the terminal expression:

\[
\begin{aligned}
 \mathsf G_{ab}
 &:=\sum_{p,q\in I}Q^0_{ap}Q^0_{bq}\mathsf D_{pq}
 \mathbb E_U[x_{1,a}x_{1,p}x_{1,b}x_{1,q}],\\
 \mathsf M_{sa}
 &:=\sum_{p,q\in I}Q^0_{ap}Q^0_{aq}\mathsf D_{pq}
 \mathbb E_U[x_{0,s}x_{2,a}x_{1,p}x_{1,q}],\\
 \mathsf N_{sa}
 &:=3Q^0_{as}\sum_{p,q\in I}Q^0_{ap}Q^0_{aq}\mathsf D_{pq}
 \mathbb E_U[x_{3,a}x_{1,s}x_{1,p}x_{1,q}],\\
 \boldsymbol\kappa_{sa}&:=3\mathsf M_{sa}+\mathsf N_{sa}.
\end{aligned}
\tag{3.1}
\]

Here \(\mathsf G\) is symmetric, while \(\mathsf M,\mathsf N\), and
\(\boldsymbol\kappa\) need not be.  Formula (3.1) has already integrated out
the backward Gaussian channel; in particular, it contains only layer-one
atoms of the grammar (1.1).

For the response audit in Section 4, it is useful to state the covariance of
channels that later vanish from the terminal answer.  Define the deterministic
Wick functional

\[
 \mathfrak W_{\mathsf D}(i_1,\ldots,i_m)
 :=
 \begin{cases}
 \displaystyle\sum_{\pi\in\operatorname{Pair}(m)}
 \prod_{\{r,t\}\in\pi}\mathsf D_{i_ri_t},&m\text{ even},\\[2mm]
 0,&m\text{ odd}.
 \end{cases}
\tag{3.2}
\]

This is a finite deterministic contraction (one, three, and fifteen pairings
for \(m=2,4,6\)).  Put

\[
\begin{aligned}
 \mathsf O_{ab}
 &:={\sum_{p,q,r,t\in I}}
 Q^0_{ap}Q^0_{aq}Q^0_{br}Q^0_{bt}
 \mathfrak W_{\mathsf D}(p,q,r,t)\\[-1mm]
 &\hspace{19mm}\times
 \mathbb E_U[x_{2,a}x_{1,p}x_{1,q}x_{2,b}x_{1,r}x_{1,t}],\\
 \mathsf V_{ab}
 &:={\sum_{p,q,r,t\in I}}
 Q^0_{ap}Q^0_{bq}Q^0_{br}Q^0_{bt}
 \mathfrak W_{\mathsf D}(p,q,r,t)\\[-1mm]
 &\hspace{19mm}\times
 \mathbb E_U[x_{1,a}x_{1,p}x_{3,b}x_{1,q}x_{1,r}x_{1,t}],\\
 \mathsf F_{ab}
 &:={\sum_{p,q,r,s,t,u\in I}}
 Q^0_{ap}Q^0_{aq}Q^0_{ar}Q^0_{bs}Q^0_{bt}Q^0_{bu}
 \mathfrak W_{\mathsf D}(p,q,r,s,t,u)\\[-1mm]
 &\hspace{19mm}\times
 \mathbb E_U[x_{3,a}x_{1,p}x_{1,q}x_{1,r}
                    x_{3,b}x_{1,s}x_{1,t}x_{1,u}].
\end{aligned}
\tag{3.3}
\]

Equations (3.2)--(3.3) are included to make every covariance block in the
peel explicit.  They do not add any random variable to the final grammar.

## 4. Exhaustive response peel

This section is a derivation intermediate representation (IR), not the final
normal form.  It records all matrix-reuse responses and all potentially
nonzero fresh covariances before the auxiliary Gaussians are contracted.

Let \(\mathsf a\sim N(0,1)\), and temporarily let
\(R\sim N(0,\mathsf D)\) be independent of \(U\).  Define

\[
 t_a=\sum_{p\in I}Q^0_{ap}x_{1,p}R_p,qquad
 P_a=x_{1,a}t_a,qquad
 E_a=x_{2,a}t_a^2,qquad
 F_a=x_{3,a}t_a^3.
\tag{4.1}
\]

For the three forward reuses after \(R=A^Tb\), the unrestricted transpose
rule gives

\[
 AP_a\ \rightsquigarrow\
 \sum_s\mathsf L_{as}b_s+\Gamma_a,qquad
 AE_a\ \rightsquigarrow\ \Omega_a,qquad
 AF_a\ \rightsquigarrow\
 \sum_s\mathsf N_{sa}b_s+\Lambda_a,
\tag{4.2}
\]

where \(b_s=\mathsf a c_sy_{1,s}\).  The response of \(AE_a\) is zero
because \(\mathbb E[\partial_{R_s}E_a]=0\).  The nonzero responses in
(4.2) are exactly

\[
 \mathbb E[\partial_{R_s}P_a]=\mathsf L_{as},
 \qquad
 \mathbb E[\partial_{R_s}F_a]=\mathsf N_{sa}.
\tag{4.3}
\]

The joint fresh Gaussian block has the completely explicit covariance

\[
 \operatorname{Cov}
 \begin{pmatrix}Z\\\Gamma\\\Omega\\\Lambda\end{pmatrix}
 =
 \begin{pmatrix}
 Q^1&0&\mathsf M&0\\
 0&\mathsf G&0&\mathsf V\\
 \mathsf M^T&0&\mathsf O&0\\
 0&\mathsf V^T&0&\mathsf F
 \end{pmatrix},
\qquad \mathsf a\ \text{independent}.
\tag{4.4}
\]

For example,
\(\operatorname{Cov}(Z_s,\Omega_a)=\mathsf M_{sa}\) and
\(\operatorname{Cov}(\Gamma_a,\Lambda_b)=\mathsf V_{ab}\).  The second
covariance is generally nonzero and is retained in (4.4).  Every displayed
zero is instead certified by an odd number of \(R\)'s in (4.1).

The three top-preactivation tangents are therefore

\[
 \zeta_a=\sum_s\mathsf K_{as}b_s+\Gamma_a,qquad
 \sigma_a=\Omega_a,qquad
 \tau_a=\sum_s\boldsymbol\kappa_{sa}b_s+\Lambda_a.
\tag{4.5}
\]

The empirical first-cross term in \(\sigma\) vanishes because
\(\mathbb E_U[P_ax_{0,s}]=0\).  The \(3\mathsf M\) part of
\(\boldsymbol\kappa\) is the deterministic \(M(X_0,E)\) term in
\(\tau\); the \(\mathsf N\) part is the cubic same-row response.

The remaining transpose line must be peeled after \(\zeta\), but before
introducing \(E,F\).  Set

\[
 h=\sum_i c_i y_{0,i},\qquad
 v_a=\sum_i\mathsf K_{ai}c_i y_{1,i},qquad
 \zeta_a=\mathsf a v_a+\Gamma_a,
\tag{4.6}
\]

and

\[
 B_a=c_a\{h y_{1,a}+\mathsf a y_{2,a}\zeta_a\}.
\tag{4.7}
\]

There are exactly two earlier forward-input families, \(X_0\) and \(P\).
The response along \(P_s\) is

\[
 \mathbb E[\partial_{\Gamma_s}B_a]
 =\delta_{sa}c_a\mathbb E[\mathsf a y_{2,a}]=0.
\tag{4.8}
\]

The complete nested response along \(x_{0,s}\) is

\[
\boxed{
 \rho_{sa}=c_a\mathbb E_Z\!\left[
 c_s y_{1,s}y_{1,a}
 +\delta_{sa}\{h y_{2,a}+y_{3,a}v_a\}
 +\mathsf K_{as}c_s y_{2,a}y_{2,s}
 \right].}
\tag{4.9}
\]

This is \(\mathbb E[\partial_{Z_s}B_a]\) with the dependence of
\(\zeta\) through the Onsager term in (4.6) retained.  Let

\[
 \chi_{sa}:=\mathsf D_{sa}+\rho_{sa}.
\tag{4.10}
\]

Then the differentiated backward field has the IR law

\[
 \dot R_a\ \rightsquigarrow\
 \sum_s\chi_{sa}x_{0,s}+\Delta_a,
 \qquad \operatorname{Cov}(\Delta_a,\Delta_b)=\beta_{ab}.
\tag{4.11}
\]

The fresh covariance \(\beta\) is contracted explicitly in (5.3) below.
Moreover,

\[
 \operatorname{Cov}(R_s,\Delta_a)=\mathbb E[b_sB_a]=0,
\tag{4.12}
\]

so \(\Delta\) is jointly independent of \((U,R)\).  Equations
(4.8)--(4.12) certify that the response registry is complete even if
\(Q^0,Q^1,\mathsf D\) are singular.

## 5. Deterministic top-layer contractions

The following finite functions of \(Z\) are only algebraic abbreviations:

\[
 h(Z)=\sum_i c_i y_{0,i},\qquad
 v_a(Z)=\sum_i\mathsf K_{ai}c_i y_{1,i},
\tag{5.1}
\]

\[
 f_a(Z)=h(Z)y_{1,a},\qquad
 g_a(Z)=y_{2,a}v_a(Z),\qquad
 w_a(Z)=\sum_s\boldsymbol\kappa_{sa}c_sy_{1,s}.
\tag{5.2}
\]

Expanding these displayed sums turns every expectation in this section
literally into atoms (1.1).  First define

\[
\boxed{
 \beta_{ab}=c_ac_b\mathbb E_Z\!\left[
 f_af_b+f_ag_b+g_af_b+3g_ag_b
 +\mathsf G_{ab}y_{2,a}y_{2,b}
 \right].}
\tag{5.3}
\]

This follows by contracting \(\mathsf a\) and \(\Gamma\) in
\(\mathbb E[B_aB_b]\): the coefficient three is
\(\mathbb E\mathsf a^4\), and the last term is the only fresh-Gaussian
pairing.

The completely contracted straight-line third derivative is

\[
\boxed{
\begin{aligned}
 T_c={}&\sum_a c_a\,\mathbb E_Z\!\left[
 3y_{3,a}\{v_a^3+v_a\mathsf G_{aa}\}
 +y_{1,a}w_a
 +3h y_{2,a}\{v_a^2+\mathsf G_{aa}\}
 \right]\\
 &+3\sum_{a,s}c_a\mathsf M_{sa}\,
 \mathbb E_Z\!\left[
 \delta_{sa}y_{3,a}v_a
 +\mathsf K_{as}c_sy_{2,a}y_{2,s}
 +c_sy_{1,s}y_{1,a}
 +\delta_{sa}h y_{2,a}
 \right].
\end{aligned}}
\tag{5.4}
\]

The second line is the exact Stein contraction
\(\mathbb E[\Omega_aF(Z)]
=\sum_s\mathsf M_{sa}\mathbb E[\partial_{Z_s}F(Z)]\).
It uses no inverse covariance and remains valid for singular \(Q^1\), by
Gaussian integration by parts in an underlying standard-Gaussian
factorization.  The \(\Lambda\) term in (4.5) vanishes only here:
its sole terminal occurrence is linear in the independent centered
\(\mathsf a\).  Thus the generally nonzero \(\mathsf V\) block in (4.4)
was not discarded prematurely.

The readout and middle-weight Hessian-square blocks are

\[
\boxed{
\begin{aligned}
 H_{a,c}
 &:=\mathbb E_Z\!\left[
 \left(\sum_a c_ay_{1,a}v_a\right)^2
 +\sum_{a,b}c_ac_b\mathsf G_{ab}y_{1,a}y_{1,b}
 \right],\\
 H_{W,c}
 &:=\sum_{a,b}\left(Q^1_{ab}\beta_{ab}
                    +\mathsf D_{ab}\mathsf G_{ab}\right).
\end{aligned}}
\tag{5.5}
\]

The mixed rank-one term in the exact middle-weight block is zero because
\(\mathbb E_U[P_ax_{0,b}]=0\), not because the two factors were declared
independent.

## 6. Deterministic first-weight contraction

All backward Gaussians in the first-weight block can be Wick-contracted
without differentiating \(\phi\).  Define the following functions of \(U\):

\[
 \overline A_a(U)
 :=x_{2,a}\sum_pQ^0_{ap}x_{1,p}\mathsf D_{ap},
 \qquad
 \overline B_a(U)
 :=x_{1,a}\sum_s\chi_{sa}x_{0,s},
\tag{6.1}
\]

and

\[
\begin{aligned}
 \mathcal A_{ab}(U)
 :=x_{2,a}x_{2,b}\sum_{p,q}Q^0_{ap}Q^0_{bq}x_{1,p}x_{1,q}
 \big(&\mathsf D_{ap}\mathsf D_{bq}
      +\mathsf D_{ab}\mathsf D_{pq}\\
      &+\mathsf D_{aq}\mathsf D_{pb}\big).
\end{aligned}
\tag{6.2}
\]

The three terms in parentheses are exactly the three Wick pairings of
\(R_aR_pR_bR_q\).  The terminal first-weight block is

\[
\boxed{
\begin{aligned}
 H_{U,c}:=\sum_{a,b}Q^0_{ab}\Big{
 &\mathbb E_U[\mathcal A_{ab}
 +\overline B_a\overline B_b
 +\overline A_a\overline B_b
 +\overline B_a\overline A_b]\\
 &+E^1_{ab}\beta_{ab}\Big}.
\end{aligned}}
\tag{6.3}
\]

Equations (6.1)--(6.3) contain only atoms of \(U\sim N(0,Q^0)\).  In
particular, the auxiliary \(R,\Delta\) in the response IR have both been
eliminated.

## 7. Closed Gaussian normal form

Combining (5.4), (5.5), and (6.3) gives

\[
 \boxed{
 C_c=2T_c+4\bigl(H_{a,c}+H_{W,c}+H_{U,c}\bigr).}
\tag{7.1}
\]

Together, (1.1)--(3.1), (4.9)--(4.10), and (5.1)--(7.1) are the requested
closed Gaussian normal form.  To emit a flat atom polynomial, perform the
following finite deterministic recursion:

1. evaluate \(Q^1,E^1\) from \(Q^0\)-atoms and \(Q^2,E^2\) from
   \(Q^1\)-atoms;
2. evaluate \(\mathsf D,\mathsf L,\mathsf K\), followed by
   \(\mathsf G,\mathsf M,\mathsf N,\boldsymbol\kappa\);
3. distribute the two-term sums in \(h,v,f,g,w\) inside each
   \(Z\)-expectation;
4. evaluate \(\beta,\rho,\chi\), followed by the four blocks in
   (5.4)--(6.3);
5. form (2.2) and (7.1).

Every loop index ranges over the fixed set \(I=\{1,2\}\); the recursion is a
finite DAG.  Its leaves are exactly atoms (1.1), and no basis approximation is
performed.  The maximum activation derivative order is three.  The largest
Gaussian integration dimension is two, regardless of the number of factors
inside an atom.

Since \(A_c\) is homogeneous of degree two and \(C_c\) of degree four in
\(c\), the full symmetric directional correction tensor can also be
reconstructed from \(c\mapsto C_c\) by polarization.

## 8. Exact reductions and regression gates

### 8.1 One active input

Take \(c=(1,0)\) and write \(q=Q^0_{11}>0\).  Although \(Q^0_{12}\) and the
second input may be arbitrary, \(\mathsf D\) has only one nonzero entry, so
every terminal sum collapses to the first coordinate.  Under the atom names
of `L2_B1_GAUSSIAN_NORMAL_FORM.md`,

\[
\begin{gathered}
 \mathsf K_{11}=q_1+qd_1=c_{\rm B1},\qquad
 \mathsf G_{11}=q^2e_1d_2,\\
 \mathsf M_{11}=q^2d_2m_1,qquad
 \mathsf N_{11}=3q^3d_2j_1,\\
 \beta_{11}=\tau_{\rm B1},\qquad
 \rho_{11}=\alpha_{\rm B1},\qquad
 \chi_{11}=k_{\rm B1}.
\end{gathered}
\tag{8.1}
\]

Substitution into (2.2) and (5.4)--(7.1) gives exactly the audited
17-atom formulas

\[
 A_c=A_{\rm B1},\qquad C_c=C_{\rm B1}.
\tag{8.2}
\]

This equality was also checked by an independent exact polynomial evaluator
for constant, linear, quadratic, and cubic activations with a non-diagonal
ambient \(Q^0\).

### 8.2 Constant and linear activations

For \(\phi\equiv1\),

\[
 A_c=(c_1+c_2)^2,\qquad C_c=0.
\tag{8.3}
\]

For \(\phi(x)=x\), let \(q_{\rm eff}=c^TQ^0c\).  The network is exactly the
same deep-linear scalar network evaluated on the effective input
\(x_{\rm eff}=c_1x_1+c_2x_2\).  The normal form gives

\[
 A_c=3q_{\rm eff},\qquad C_c=48q_{\rm eff}^2,
\tag{8.4}
\]

for every PSD \(Q^0\), including singular cases.

### 8.3 Exact quadratic two-input campaign

Let

\[
 \phi(x)=x^2,qquad
 Q^0=\begin{pmatrix}1&\theta\\\theta&1\end{pmatrix},qquad
 t=\theta^2.
\tag{8.5}
\]

For \(c_+=(1,1)/2\), (2.2) and (7.1) reduce exactly to

\[
 A_+=63+20t+28t^2,
\tag{8.6}
\]

\[
 C_+=279680+423312t+788336t^2+143232t^3+50624t^4.
\tag{8.7}
\]

For \(c_-=(1,-1)/2\), they reduce to

\[
 A_-=48-20t-28t^2=(1-t)(48+28t),
\tag{8.8}
\]

\[
\begin{aligned}
 C_-&=168192-91904t-270144t^2+143232t^3+50624t^4\\
    &=(1-t)^2(168192+244480t+50624t^2).
\end{aligned}
\tag{8.9}
\]

These four polynomials agree coefficient-for-coefficient with the accepted
independent Campaign-2 quotient-Wick/tree calculation.  They also check the
forced null channel at \(\theta=1\).

### 8.4 Independent implementation comparison

The exact rational evaluator
[`contracted_gnf_polynomial_reference.py`](contracted_gnf_polynomial_reference.py)
was derived separately from this response ledger.  A term-by-term comparison
found the following exact dictionary and no discrepancy:

\[
 \texttt{source_cov}=\mathsf D,\quad
 \texttt{tangent_c}=\mathsf K,\quad
 \texttt{tangent_cov}=\mathsf G,\quad
 \texttt{second_cross}=\mathsf M,
\tag{8.10}
\]

\[
 \texttt{third_response}=\mathsf N,\quad
 \texttt{tau_response}=\boldsymbol\kappa,\quad
 \texttt{nested_response}=\rho,\quad
 \texttt{total_response}=\chi.
\tag{8.11}
\]

Its exact tests cover (8.1)--(8.9) and channel homogeneity.  Separately, the
finite-width directional contraction agrees seedwise with both a feature-ODE
jet and a raw-coordinate multivariate third jet; those checks audit the source
identity before the width limit.

## 9. Probability theorem and regularity boundary

Equations (1.1)--(7.1) identify the deterministic master-theorem value of the
fixed Tensor Program in `FINITE_WIDTH_DIRECTIONAL_PROGRAM.md`.  Suppose
\(\phi\) is **polynomially smooth**: \(\phi\in C^\infty(\mathbb R)\), and
every derivative \(\phi^{(k)}\), for every \(k\ge0\), is bounded in absolute
value by a polynomial whose constants may depend on \(k\).  Then Theorem 3.7
of Golikov and Yang, *Non-Gaussian Tensor Programs*, applied to that fixed
program gives

\[
 C_{n,c}\longrightarrow C_c
 \quad\text{almost surely and in }L^p
 \quad(1\le p<\infty),
 \qquad
 \mathbb E C_{n,c}\longrightarrow C_c.
\tag{9.1}
\]

Gaussian weights satisfy the matrix-moment hypotheses, and fixed correlated
initial coordinates are generated by a deterministic square root of \(Q^0\).
All empirical 2-by-2 matrices in the finite-width program are finitely many
`Moment` scalars, and arbitrary reuse of the middle matrix and its transpose
is part of the theorem's syntax.  Neither singular \(Q^0\) nor singular
\(Q^1\) requires a rank assumption in the formulas above.

There is a genuine regularity distinction.  The algebraic normal form uses
only \(\phi\) through \(\phi'''\), but the cited \(L^p\) theorem requires
polynomial bounds for derivatives of every order.  Under only finite-order
pseudo-Lipschitz hypotheses, Tensor Programs III, Theorem E.15, supplies the
almost-sure fixed-program limit, while the annealed conclusion in (9.1)
still needs a separate uniform-integrability bound.  ReLU is outside the
smooth theorem envelope and is not covered by this note.

Finally, \(C_c\) is the first nonlinear feature correction associated with
the direction \(g_c\).  For a generic activation it need not be nonnegative;
calling \(C_c/(2A_c^2)\) a positive Stieltjes moment requires an additional
positivity result and is not asserted here.
