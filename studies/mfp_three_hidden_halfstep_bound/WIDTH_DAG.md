# Fixed-step width limit for the three-hidden-layer network

## 1. Statement proved here

This note treats only the width-first identification.  It does not expand a
finite-width network in the step size.  Let \(h\ne0\) be fixed with
\(|h|\le1\).  For the exact three-hidden-layer network in Section 2, define
the four population two-time Grams produced by the Gaussian program in
Section 5:

\[
 Q_H^{[1]}=(\mathbb E[H_rH_s])_{0\le r,s\le1},\qquad
 Q_G^{[1]}=(\mathbb E[G_rG_s])_{0\le r,s\le1},
\]

\[
 K_E^{[1]}=(\mathbb E[E_rE_s])_{0\le r,s\le1},\qquad
 K_C^{[1]}=(\mathbb E[C_rC_s])_{0\le r,s\le1}.                 \tag{1.1}
\]

Assume that \(\phi\in C^2(\mathbb R)\), that \(\phi\) has at most linear
growth, that \(\phi'\) and \(\phi''\) are bounded, and that

\[
 \mathbb E\phi(Z)^2=1,\qquad
 d:=\mathbb E\phi'(Z)^2>0,\qquad Z\sim N(0,1).               \tag{1.2}
\]

The stronger \(C^{12}\) envelope used for the quantitative theorem implies
these assumptions.  Suppose, at this fixed \(h\), that all four matrices in
(1.1) are positive definite.  Then every finite-width value field in the
ten-action chronology

\[
 X^0,Y^0,R^0,S^0,X^1,Y^1,R^1,S^1,X^2,Y^2                 \tag{1.3}
\]

converges, in normalized \(L^p\) for every finite \(p\), to the field with
the same name in the Gaussian operator DAG of Section 5.  Every empirical
Gram and raw overlap used in the ten conditioning steps converges in every
finite \(L^p\) and is uniformly integrable.  The stopped/extended
conditional-regression coefficients and innovation scales defined in
Section 8.4 have the same property; no assertion about an untruncated
inverse Gram on the discarded event is needed.  In particular, for
\(k=1,2\),

\[
 \lim_{n\to\infty}\mathbb E f_n^k=F_k(h),                    \tag{1.4}
\]

where the limit is taken at this fixed nonzero \(h\).  The two terminal
three-time feature Grams may be singular.  No three-time Gram is inverted.

There is also a rank-free one-step corollary needed for the comparison
\(F_2(\eta)-F_1(2\eta)\): if \(d>0\), then for every fixed
\(0<|h|\le1\),

\[
 \lim_{n\to\infty}\mathbb E f_n^1=F_1(h),                  \tag{1.5}
\]

without assuming positive definiteness of any two-time Gram.  Its chronology
is the six-action prefix through \(Y^1\).  Only the positive scalar base
Grams \(Q_{H,00}=Q_{G,00}=1\), \(K_{C,00}=d\), and \(K_{E,00}=d^2\) are
inverted.  The new innovation at \(X^1\) is allowed to vanish and is handled
by the square-root estimate (8.12), because it is used only as the query of
the terminal action \(Y^1\); no two-time Gram is subsequently inverted.

The proof below is unconditional once the four rank inequalities (1.1) are
given.  Thus the only separate width-bridge obligation in a small-step
theorem is an activation-defined radius on which those four inequalities
hold.  Section 9 identifies their exact Schur complements.

If \(d=0\), continuity and the full support of Gaussian measure imply
\(\phi'\equiv0\); hence \(\phi\) is a constant of modulus one.  Every hidden
parameter gradient is zero, \(a^{s+1}=a^s+h\phi\), and
\(f_n^s=sh\) exactly.  In that case no conditioning rank is needed.

## 2. Exact finite-width network and normalization

Let all three hidden layers have width \(n\).  Let \(x\in\mathbb R^p\) be
deterministic and satisfy

\[
 \frac{\|x\|^2}{p}=1.                                       \tag{2.1}
\]

At initialization take mutually independent standard Gaussian families

\[
 w_j^0\sim N(0,I_p),\quad W_{ij}^0\sim N(0,1),\quad
 V_{ki}^0\sim N(0,1),\quad a_k^0\sim N(0,1).                \tag{2.2}
\]

There are no biases.  At time \(s\), put

\[
 u_j^s=\frac{(w_j^s)^Tx}{\sqrt p},\qquad H_j^s=\phi(u_j^s),
\]

\[
 z_i^s=\frac1{\sqrt n}\sum_jW_{ij}^sH_j^s,\qquad
 G_i^s=\phi(z_i^s),
\]

\[
 y_k^s=\frac1{\sqrt n}\sum_iV_{ki}^sG_i^s,\qquad
 f_n^s=\frac1n\sum_ka_k^s\phi(y_k^s).                       \tag{2.3}
\]

One simultaneous feature-ascent step is

\[
 \theta^{s+1}=\theta^s+hn\nabla_\theta f_n^s.               \tag{2.4}
\]

Define the two back-propagated cotangents

\[
 C_k^s=a_k^s\phi'(y_k^s),\qquad
 d_i^s=\frac1{\sqrt n}\sum_kV_{ki}^sC_k^s,\qquad
 E_i^s=d_i^s\phi'(z_i^s),
\]

\[
 b_j^s=\frac1{\sqrt n}\sum_iW_{ij}^sE_i^s.                 \tag{2.5}
\]

Direct differentiation of (2.3), with every right-hand side evaluated at
time \(s\), gives the exact updates

\[
 \begin{aligned}
 a_k^{s+1}&=a_k^s+h\phi(y_k^s),\\
 V_{ki}^{s+1}&=V_{ki}^s+\frac h{\sqrt n}C_k^sG_i^s,\\
 W_{ij}^{s+1}&=W_{ij}^s+\frac h{\sqrt n}E_i^sH_j^s,\\
 w_j^{s+1}&=w_j^s+\frac h{\sqrt p}b_j^s\phi'(u_j^s)x,\\
 u_j^{s+1}&=u_j^s+h b_j^s\phi'(u_j^s).
 \end{aligned}                                               \tag{2.6}
\]

For example, \(\partial f_n^s/\partial z_i^s=d_i^s/n\) and
\(\partial f_n^s/\partial u_j^s=b_j^s\phi'(u_j^s)/n\); this verifies the
two less immediate scalings in (2.6).

Write \(W=W^0\), \(V=V^0\), and introduce the raw source-matrix actions

\[
 X^s=WH^s/\sqrt n,\quad S^s=W^TE^s/\sqrt n,
\qquad
 Y^s=VG^s/\sqrt n,\quad R^s=V^TC^s/\sqrt n.                 \tag{2.7}
\]

For \(P\in\{H,G,E,C\}\), write

\[
 \langle P^r,P^s\rangle_n=\frac1n(P^r)^TP^s,
\]

and denote these four empirical Grams by
\(Q_{H,rs}^{(n)},Q_{G,rs}^{(n)},K_{E,rs}^{(n)},K_{C,rs}^{(n)}\).
Summing the rank-one updates in (2.6) gives, without approximation,

\[
 \begin{aligned}
 z^s&=X^s+h\sum_{r<s}Q_{H,rs}^{(n)}E^r,\\
 y^s&=Y^s+h\sum_{r<s}Q_{G,rs}^{(n)}C^r,\\
 d^s&=R^s+h\sum_{r<s}K_{C,rs}^{(n)}G^r,\\
 b^s&=S^s+h\sum_{r<s}K_{E,rs}^{(n)}H^r,\\
 a^s&=a^0+h\sum_{r<s}\phi(y^r).
 \end{aligned}                                               \tag{2.8}
\]

In particular, no current-time Gram term occurs in any line of (2.8).

## 3. The ten predictable actions

The correct reveal order for two recomputed gradient steps is

\[
 \begin{array}{c|c|l}
 \text{action}&\text{matrix query}&\text{field made measurable}\\
 \hline
 X^0&W H^0&z^0,G^0\\
 Y^0&V G^0&y^0,a^0,C^0\\
 R^0&V^TC^0&d^0,E^0\\
 S^0&W^TE^0&b^0,u^1,H^1\\
 X^1&W H^1&z^1,G^1\\
 Y^1&V G^1&y^1,a^1,C^1\\
 R^1&V^TC^1&d^1,E^1\\
 S^1&W^TE^1&b^1,u^2,H^2\\
 X^2&W H^2&z^2,G^2\\
 Y^2&V G^2&y^2,f_n^2.
 \end{array}                                                  \tag{3.1}
\]

The phrase “made measurable” includes adding the already known rank-one
terms from (2.8).  Each query in the middle column is therefore measurable
before the corresponding action is revealed.  In particular, \(H^1\)
depends on the already revealed reused-column actions \(R^0,S^0\), and
\(G^1\) depends on all four time-zero actions.  Neither is replaced by an
independent copy.

The one-step output uses the prefix through \(Y^1\).  The two-step output
uses all ten actions.

## 4. Adaptive conditioning for two independent reused matrices

The next theorem is the finite-dimensional probability input.  It is stated
for any finite interlacing of actions, not only (3.1).

**Lemma 4.1 (adaptive two-matrix conditioning).**  Let \(M_1,M_2\) be
independent \(n\times n\) standard Gaussian matrices, independent of an
external sigma-field \(\mathcal E\).  At every stage choose one matrix and
one row or column query.  The query may be an arbitrary measurable function
of \(\mathcal E\) and all previously revealed actions of both matrices, but
must be measurable before its new action is revealed.

For \(\ell=1,2\), let \(H_\ell,C_\ell\) collect the row and column queries
already made to \(M_\ell\), and let

\[
 Y_\ell=M_\ell H_\ell/\sqrt n,\qquad
 D_\ell=M_\ell^TC_\ell/\sqrt n.
\]

Conditionally on the global revealed filtration, jointly for
\(\ell=1,2\),

\[
 M_\ell=P_{C_\ell}M_\ell+M_\ell P_{H_\ell}
          -P_{C_\ell}M_\ell P_{H_\ell}
          +P_{C_\ell}^{\perp}\widetilde M_\ell
                    P_{H_\ell}^{\perp},                     \tag{4.1}
\]

where \(\widetilde M_1,\widetilde M_2\) are conditionally independent
standard Gaussian matrices, independent of the revealed filtration.

For either matrix, put

\[
 Q=H^TH/n,\quad K=C^TC/n,\quad
 \mathcal R=C^TY/n=D^TH/n.                                  \tag{4.2}
\]

If \(Q,K\) are invertible, a new column query \(c\) satisfies

\[
 \frac{M^Tc}{\sqrt n}
 =DK^{-1}k+HQ^{-1}(r-\mathcal R^TK^{-1}k)
   +\tau_cP_H^\perp g,                                      \tag{4.3}
\]

where

\[
 k=C^Tc/n,\quad r=Y^Tc/n,\quad
 \tau_c^2=c^Tc/n-k^TK^{-1}k.                               \tag{4.4}
\]

A new row query \(q_\mathrm{new}\) satisfies

\[
 \frac{Mq_\mathrm{new}}{\sqrt n}
 =YQ^{-1}q+CK^{-1}(v-\mathcal RQ^{-1}q)
   +\tau_qP_C^\perp g,                                      \tag{4.5}
\]

where

\[
 q=H^Tq_\mathrm{new}/n,\quad v=D^Tq_\mathrm{new}/n,\quad
 \tau_q^2=q_\mathrm{new}^Tq_\mathrm{new}/n-q^TQ^{-1}q.     \tag{4.6}
\]

Empty blocks are omitted.  With singular blocks, the conditional-law
identity (4.1) and the analogues of (4.3)--(4.6) hold with orthogonal
projectors and Moore--Penrose inverses.

**Proof.**  Let \(\mathcal F_t\) be the global filtration after \(t\)
actions.  We prove by induction that, conditional on \(\mathcal F_t\), the
two unrevealed residuals in (4.1) are independent double-orthogonal Gaussian
matrices.  This is true at \(t=0\) by independence of \(M_1,M_2\).

Suppose the next predictable action is \(M_1q_\mathrm{new}\).  Given
\(\mathcal F_t\), decompose

\[
 q_\mathrm{new}=P_{H_1}q_\mathrm{new}+q_\perp.
\]

Only \(P_{C_1}^\perp\widetilde M_1q_\perp\) is unrevealed.  If
\(q_\perp\ne0\), let \(e=q_\perp/\|q_\perp\|\).  The Gaussian projections
\(\widetilde M_1ee^T\) and \(\widetilde M_1(I-ee^T)\) are independent.
Revealing the former leaves

\[
 P_{C_1}^\perp\widetilde M_1
 P_{\operatorname{span}(H_1,q_\mathrm{new})}^\perp
\]

fresh and independent.  It is also independent of the untouched residual
of \(M_2\).  When \(q_\perp=0\), no residual component is revealed.  A
column action is the transpose argument, and an action on \(M_2\) is
identical with the labels exchanged.  Predictability is essential here:
adjoining the query itself reveals no new information after conditioning on
\(\mathcal F_t\).  This closes the finite induction and proves (4.1),
including conditional independence of the two residual matrices despite
interlaced, cross-dependent queries.

For (4.3), write \(c=CK^{-1}k+c_\perp\).  The first component contributes
\(DK^{-1}k\).  The projection of \(M^Tc_\perp/\sqrt n\) onto
\(\operatorname{span}(H)\) is

\[
 HQ^{-1}\frac{Y^Tc_\perp}{n}
 =HQ^{-1}(r-\mathcal R^TK^{-1}k),
\]

and its remaining conditional covariance is
\((\|c_\perp\|^2/n)P_H^\perp=\tau_c^2P_H^\perp\).  This proves
(4.3)--(4.4).  The row formula follows by transposition.  Orthogonal
projection gives the pseudoinverse version without any rank assumption.

## 5. The Gaussian operator DAG

The program is chronological, so the following covariance prescriptions
are definitions rather than self-consistency assumptions.  Start with
independent \(U,A\sim N(0,1)\).  Introduce four centered Gaussian source
blocks

\[
 \xi=(\xi_0,\xi_1,\xi_2),\quad
 \chi=(\chi_0,\chi_1),\quad
 \zeta=(\zeta_0,\zeta_1,\zeta_2),\quad
 \omega=(\omega_0,\omega_1),                               \tag{5.1}
\]

mutually independent and independent of \((U,A)\), with covariances

\[
 \operatorname{Cov}(\xi_r,\xi_s)=Q_{H,rs},\quad
 \operatorname{Cov}(\chi_r,\chi_s)=K_{E,rs},
\]

\[
 \operatorname{Cov}(\zeta_r,\zeta_s)=Q_{G,rs},\quad
 \operatorname{Cov}(\omega_r,\omega_s)=K_{C,rs}.            \tag{5.2}
\]

They are extended one coordinate at a time after the corresponding query
Gram has already been computed.  Equivalently, at each extension take the
Gaussian regression on the old block plus a fresh independent Gaussian with
the Schur-complement variance.  This supplies a finite construction of
(5.1)--(5.2), including when a terminal Schur complement is zero.

Put \(u_0=U\), \(H_s=\phi(u_s)\).  For \(s=0,1,2\), whenever the indicated
earlier fields exist, define

\[
 \rho^W_{sr}=\mathbb E[\partial_{\chi_r}H_s]\quad(0\le r<s),
\]

\[
 z_s=\xi_s+\sum_{r<s}(\rho^W_{sr}+hQ_{H,rs})E_r,
 \qquad G_s=\phi(z_s),                                      \tag{5.3}
\]

\[
 \rho^V_{sr}=\mathbb E[\partial_{\omega_r}G_s]\quad(0\le r<s),
\]

\[
 y_s=\zeta_s+\sum_{r<s}(\rho^V_{sr}+hQ_{G,rs})C_r,
\]

\[
 a_s=A+h\sum_{r<s}\phi(y_r),\qquad C_s=a_s\phi'(y_s).      \tag{5.4}
\]

For \(s=0,1\), define

\[
 \sigma^V_{sr}=\mathbb E[\partial_{\zeta_r}C_s]
 \quad(0\le r\le s),
\]

\[
 d_s=\omega_s+\sum_{r\le s}\sigma^V_{sr}G_r
              +h\sum_{r<s}K_{C,rs}G_r,
 \qquad E_s=d_s\phi'(z_s),                                 \tag{5.5}
\]

\[
 \sigma^W_{sr}=\mathbb E[\partial_{\xi_r}E_s]
 \quad(0\le r\le s),
\]

\[
 b_s=\chi_s+\sum_{r\le s}\sigma^W_{sr}H_r
              +h\sum_{r<s}K_{E,rs}H_r,
\]

\[
 u_{s+1}=u_s+h b_s\phi'(u_s),\qquad H_{s+1}=\phi(u_{s+1}). \tag{5.6}
\]

Every Gram entry in these formulas is the expectation of the product of
the displayed scalar fields.  All partial derivatives hold the other
canonical marks in (5.1) fixed.  Bounded derivatives and at-most-linear
growth make every field and response integrand a polynomial-growth function
of finitely many Gaussian marks, so the expectations exist.

The outputs are

\[
 F_1(h)=\mathbb E[a_1\phi(y_1)],\qquad
 F_2(h)=\mathbb E[a_2\phi(y_2)].                            \tag{5.7}
\]

For completeness, the response derivatives are generated by an acyclic
finite recursion.  Treat all population Grams and already evaluated
response expectations as deterministic coefficients.  Set

\[
 L^W_{st}=\rho^W_{st}+hQ_{H,ts}\quad(t<s),\qquad
 T^W_{st}=\sigma^W_{st}+h\mathbf1_{\{t<s\}}K_{E,ts},
\]

\[
 L^V_{st}=\rho^V_{st}+hQ_{G,ts}\quad(t<s),\qquad
 T^V_{st}=\sigma^V_{st}+h\mathbf1_{\{t<s\}}K_{C,ts}.
\]

The derivatives with respect to a bottom source \(\chi_r\) obey

\[
 \partial_{\chi_r}b_s
 =\mathbf1_{\{r=s\}}+\sum_{t\le s}T^W_{st}
                         \partial_{\chi_r}H_t,
\]

\[
 \partial_{\chi_r}u_{s+1}
 =\partial_{\chi_r}u_s
 +h\left[
   (\partial_{\chi_r}b_s)\phi'(u_s)
   +b_s\phi''(u_s)\partial_{\chi_r}u_s
 \right],
\qquad
 \partial_{\chi_r}H_{s+1}
 =\phi'(u_{s+1})\partial_{\chi_r}u_{s+1}.                  \tag{5.8}
\]

These derivatives determine \(\rho^W\).  For a middle transpose source
\(\omega_r\),

\[
 \partial_{\omega_r}z_s
 =\sum_{t<s}L^W_{st}\partial_{\omega_r}E_t,\qquad
 \partial_{\omega_r}G_s
 =\phi'(z_s)\partial_{\omega_r}z_s,
\]

\[
 \partial_{\omega_r}d_s
 =\mathbf1_{\{r=s\}}+\sum_{t\le s}T^V_{st}
                         \partial_{\omega_r}G_t,
\]

\[
 \partial_{\omega_r}E_s
 =(\partial_{\omega_r}d_s)\phi'(z_s)
   +d_s\phi''(z_s)\partial_{\omega_r}z_s.                  \tag{5.9}
\]

These determine \(\rho^V\).  For a top row source \(\zeta_r\),

\[
 \partial_{\zeta_r}y_s
 =\mathbf1_{\{r=s\}}+\sum_{t<s}L^V_{st}
                              \partial_{\zeta_r}C_t,
\qquad
 \partial_{\zeta_r}a_s
 =h\sum_{t<s}\phi'(y_t)\partial_{\zeta_r}y_t,
\]

\[
 \partial_{\zeta_r}C_s
 =(\partial_{\zeta_r}a_s)\phi'(y_s)
   +a_s\phi''(y_s)\partial_{\zeta_r}y_s.                   \tag{5.10}
\]

These determine \(\sigma^V\).  Finally, for a middle row source \(\xi_r\),

\[
 \partial_{\xi_r}z_s
 =\mathbf1_{\{r=s\}}+\sum_{t<s}L^W_{st}\partial_{\xi_r}E_t,
\qquad
 \partial_{\xi_r}G_s=\phi'(z_s)\partial_{\xi_r}z_s,
\]

\[
 \partial_{\xi_r}d_s
 =\sum_{t\le s}T^V_{st}\partial_{\xi_r}G_t,
\]

\[
 \partial_{\xi_r}E_s
 =(\partial_{\xi_r}d_s)\phi'(z_s)
   +d_s\phi''(z_s)\partial_{\xi_r}z_s.                     \tag{5.11}
\]

These determine \(\sigma^W\).  Time increases on the right-hand side of
none of (5.8)--(5.11), so the recursion terminates after the displayed two
training stages.  It also proves directly the asserted polynomial Gaussian
envelopes for every response integrand.

At time zero,

\[
 \sigma^V_{00}=\mathbb E[A\phi''(\zeta_0)]=0.
\]

Thus \(d_0=\omega_0\).  Since \(\omega_0\) is centered and independent of
\(\xi_0\),

\[
 \sigma^W_{00}=\mathbb E[\omega_0\phi''(\xi_0)]=0,
\]

so \(b_0=\chi_0\).  Consequently

\[
 Q_{H,00}=Q_{G,00}=1,\qquad K_{C,00}=d,\qquad K_{E,00}=d^2. \tag{5.12}
\]

This also confirms directly that the first four Gaussian source actions are
nondegenerate whenever \(\phi\) is nonconstant.

## 6. All reused-matrix response cancellations

Rather than asserting ten analogous cancellations, we prove one block
identity and then instantiate it at every line of (3.1).

Consider either one of the two matrices.  At a representative coordinate,
let

\[
 h=(H_0,\ldots,H_{m-1})^T,\qquad
 c=(C_0,\ldots,C_{m-1})^T
\]

be its old row and column queries, and let \(y,d\) be the corresponding raw
row and transpose actions.  Suppose the already identified actions have the
form

\[
 y=\xi+Pc,\qquad d=\chi+Sh,                                \tag{6.1}
\]

where \(P_{sr}\) is the response of row query \(s\) to old column-source
coordinate \(r\), and \(S_{sr}\) is the response of column query \(s\) to
row-source coordinate \(r\).  Put

\[
 Q=\mathbb E[hh^T],\qquad K=\mathbb E[cc^T].                \tag{6.2}
\]

For a centered, possibly singular Gaussian vector \(X\) with covariance
\(\Sigma\), and a \(C^1\) polynomial-growth function \(g\),

\[
 \mathbb E[Xg(X)]=\Sigma\,\mathbb E[\nabla g(X)].            \tag{6.3}
\]

Indeed, write \(X=BZ\) with \(Z\) standard Gaussian, apply scalar Gaussian
integration by parts to each coordinate of \(Z\), and use
\(BB^T=\Sigma\).  The polynomial envelope supplies domination.  Therefore

\[
 \mathcal R:=\mathbb E[cy^T]=SQ+KP^T.                       \tag{6.4}
\]

Here the first term follows from
\(\mathbb E[c\xi^T]=SQ\), and the second from (6.1).

### 6.1 A new row action

Let \(H_m\) be the new row query, let

\[
 q=\mathbb E[hH_m],\qquad
 \rho=\mathbb E[\nabla_\chi H_m].                           \tag{6.5}
\]

Equation (6.3) and (6.1) give

\[
 v:=\mathbb E[dH_m]=K\rho+Sq.                              \tag{6.6}
\]

The population version of (4.5) is

\[
 y^TQ^{-1}q+c^TK^{-1}(v-\mathcal RQ^{-1}q)
       +\text{orthogonal innovation}.                       \tag{6.7}
\]

Substituting (6.4)--(6.6),

\[
 K^{-1}(v-\mathcal RQ^{-1}q)
 =\rho-P^TQ^{-1}q.                                         \tag{6.8}
\]

The term \(c^TP^TQ^{-1}q\) from the first summand of (6.7) cancels the
negative term in (6.8).  The remaining Gaussian regression

\[
 \xi^TQ^{-1}q+
 \sqrt{Q_{mm}-q^TQ^{-1}q}\,Z
\]

is precisely the next coordinate \(\xi_m\) of the jointly Gaussian source
block.  Thus the complete new raw row action is

\[
 \boxed{\ \xi_m+\sum_{r<m}\rho_rC_r\ }.                    \tag{6.9}
\]

The orthogonal projection of the finite-dimensional innovation onto the old
column-query span disappears in normalized \(L^p\); this is quantified in
Section 8.  Formula (6.9), however, already includes every nonvanishing
population response.

### 6.2 A new transpose action

Now suppose the new row action has been included, so \(h\) and \(y\) have
length \(m+1\), while the old \(c,d\) have length \(m\).  Embed \(S\) as an
\(m\times(m+1)\) matrix by adding a zero last column, and let \(P\) be the
\((m+1)\times m\) row-response matrix.  For the new column query \(C_m\),
put

\[
 k=\mathbb E[cC_m],\qquad
 \sigma=\mathbb E[\nabla_\xi C_m].                          \tag{6.10}
\]

Then

\[
 r:=\mathbb E[yC_m]=Q\sigma+Pk,                             \tag{6.11}
\]

while (6.4) remains valid.  The population form of (4.3) is

\[
 d^TK^{-1}k+h^TQ^{-1}(r-\mathcal R^TK^{-1}k)
       +\text{orthogonal innovation}.                       \tag{6.12}
\]

Using (6.4) and (6.11),

\[
 Q^{-1}(r-\mathcal R^TK^{-1}k)
 =\sigma-S^TK^{-1}k.                                       \tag{6.13}
\]

The first term of (6.12) equals

\[
 \chi^TK^{-1}k+h^TS^TK^{-1}k,                              \tag{6.14}
\]

so the last term in (6.14) cancels the negative term in (6.13).  The
remaining Gaussian regression extends \(\chi\) by its covariance with the
old coordinates.  Hence the complete new raw transpose action is

\[
 \boxed{\ \chi_m+\sum_{r\le m}\sigma_rH_r\ }.              \tag{6.15}
\]

This proves both cancellations for arbitrary history and therefore also
when the queries depend on actions of the other matrix.

### 6.3 Instantiation at all ten actions

For \(W\), substitute

\[
 (H,C,y,d,\xi,\chi)=(H,E,X,S,\xi,\chi),
\]

and for \(V\), substitute

\[
 (H,C,y,d,\xi,\chi)=(G,C,Y,R,\zeta,\omega).
\]

Equations (6.9) and (6.15) give, in the exact chronological order,

\[
 \begin{array}{c|l}
 X^0&\xi_0\\
 Y^0&\zeta_0\\
 R^0&\omega_0+\sigma^V_{00}G_0=\omega_0\\
 S^0&\chi_0+\sigma^W_{00}H_0=\chi_0\\
 X^1&\xi_1+\rho^W_{10}E_0\\
 Y^1&\zeta_1+\rho^V_{10}C_0\\
 R^1&\omega_1+\sigma^V_{10}G_0+\sigma^V_{11}G_1\\
 S^1&\chi_1+\sigma^W_{10}H_0+\sigma^W_{11}H_1\\
 X^2&\xi_2+\rho^W_{20}E_0+\rho^W_{21}E_1\\
 Y^2&\zeta_2+\rho^V_{20}C_0+\rho^V_{21}C_1.
 \end{array}                                                \tag{6.16}
\]

Adding the learned rank-one terms from (2.8) turns (6.16) exactly into
(5.3)--(5.6).  Thus no response created by either \(W/W^T\) or \(V/V^T\)
has been discarded.

## 7. Complete finite-action ledger

The following table lists the new empirical information at every action.
An “old cross block” means

\[
 \mathcal R_W^{(n)}=(E^{\rm old})^TX^{\rm old}/n
                    =(S^{\rm old})^TH^{\rm old}/n,
\]

or

\[
 \mathcal R_V^{(n)}=(C^{\rm old})^TY^{\rm old}/n
                    =(R^{\rm old})^TG^{\rm old}/n.          \tag{7.1}
\]

Both equalities are exact matrix identities, since both sides are the same
triple product with \(W\), respectively \(V\).

\[
\begin{array}{c|l|l}
\text{action}&\text{new Gram entries}&\text{new raw overlaps}\\
\hline
X^0&Q_{H,00}^{(n)}&\text{none}\\
Y^0&Q_{G,00}^{(n)}&\text{none}\\
R^0&K_{C,00}^{(n)}&(Y^0)^TC^0/n\\
S^0&K_{E,00}^{(n)}&(X^0)^TE^0/n\\
X^1&Q_{H,01}^{(n)},Q_{H,11}^{(n)}&(S^0)^TH^1/n,\ \mathcal R_W^{(n)}\\
Y^1&Q_{G,01}^{(n)},Q_{G,11}^{(n)}&(R^0)^TG^1/n,\ \mathcal R_V^{(n)}\\
R^1&K_{C,01}^{(n)},K_{C,11}^{(n)}&(Y^{0:1})^TC^1/n,\ \mathcal R_V^{(n)}\\
S^1&K_{E,01}^{(n)},K_{E,11}^{(n)}&(X^{0:1})^TE^1/n,\ \mathcal R_W^{(n)}\\
X^2&Q_{H,r2}^{(n)}\ (0\le r\le2)&(S^{0:1})^TH^2/n,\ \mathcal R_W^{(n)}\\
Y^2&Q_{G,r2}^{(n)}\ (0\le r\le2)&(R^{0:1})^TG^2/n,\ \mathcal R_V^{(n)}.
\end{array}                                                  \tag{7.2}
\]

At a transpose action, the vector \((Y^{\rm old})^TC^s/n\), together with
the old cross block, supplies exactly \(r,k,\mathcal R\) in
(4.3)--(4.4).  At a row action, \((D^{\rm old})^TH^s/n\), together with
the old cross block, supplies exactly \(v,q,\mathcal R\) in
(4.5)--(4.6).  Hence (7.2) omits no conditioning input.

## 8. Concentration, coupling, and uniform integrability

We now prove the convergence assertion of Section 1 for the actual network.
No state-evolution theorem is invoked.

For a vector \(x\in\mathbb R^n\), write

\[
 \|x\|_{n,p}=\left(\frac1n\sum_i|x_i|^p\right)^{1/p}.       \tag{8.1}
\]

We use two quantitative facts.  If \(Z_i\) are iid centered and have a
finite \(p\)-th moment, Rosenthal's inequality gives, for \(p\ge2\),

\[
 \left\|\frac1n\sum_iZ_i\right\|_{L^p}
 \le C_p\left(n^{-1/2}\|Z_1\|_{L^2}
             +n^{-1+1/p}\|Z_1\|_{L^p}\right).              \tag{8.2}
\]

Also, for an \(n\times n\) standard Gaussian matrix \(M\),

\[
 \mathbb P(\|M\|_{\rm op}>2\sqrt n+t)\le2e^{-t^2/2}.       \tag{8.3}
\]

Thus \(\|M\|_{\rm op}/\sqrt n\) has moments of every fixed order uniformly
in \(n\).

### 8.1 One compatible ideal array

For each of the three layers take iid copies of the canonical marks used by
the population DAG:

* bottom coordinates carry \((U,\chi_0,\chi_1)\);
* middle coordinates carry \((\xi_0,\xi_1,\xi_2,
  \omega_0,\omega_1)\);
* top coordinates carry \((A,\zeta_0,\zeta_1,\zeta_2)\).

The four time blocks are constructed chronologically by Gaussian
Gram--Schmidt.  For example, after \(H_1\) is known,

\[
 \xi_1=\frac{Q_{H,01}}{Q_{H,00}}\xi_0
 +\sqrt{Q_{H,11}-\frac{Q_{H,01}^2}{Q_{H,00}}}\,Z_{\xi,1}, \tag{8.4}
\]

and, after \(E_1\) is known,

\[
 \chi_1=\frac{K_{E,01}}{K_{E,00}}\chi_0
 +\sqrt{K_{E,11}-\frac{K_{E,01}^2}{K_{E,00}}}\,Z_{\chi,1}.\tag{8.5}
\]

The \(\zeta\)- and \(\omega\)-blocks use the same formulas with
\((Q_H,K_E)\) replaced by \((Q_G,K_C)\).  The terminal coordinates
\(\xi_2,\zeta_2\) are the regression on their two old coordinates plus a
fresh Gaussian scaled by the possibly zero terminal Schur complement.  All
fresh \(Z\)'s and all three layer arrays are independent.

Between these extensions, apply the scalar maps (5.3)--(5.6).  Thus ideal
coordinates are iid within each physical layer, while all same-coordinate
time dependence is retained.  At each action in (3.1), use the same fresh
Gaussian vector both for the conditional residual in Lemma 4.1 and for the
corresponding Gram--Schmidt innovation.  Lemma 4.1 guarantees that these
choices can be made jointly for \(W\) and \(V\).  This is one coupled
chronological construction, rather than ten unrelated marginal couplings.

### 8.2 Orthogonal projections are negligible

Let \(L\in\mathbb R^{n\times r}\) have fixed \(r\), and suppose
\(L^TL/n\) has smallest eigenvalue at least \(\gamma>0\).  If
\(g\sim N(0,I_n)\) is conditionally independent of \(L\), then

\[
 P_Lg=L(L^TL/n)^{-1}\frac{L^Tg}{n}.                         \tag{8.6}
\]

Conditionally on \(L\), the coefficient vector on the right is centered
Gaussian with covariance \((L^TL/n)^{-1}/n\).  Minkowski and Gaussian
moment bounds therefore yield, for finite \(p,s\),

\[
 \left\|\|P_Lg\|_{n,p}\right\|_{L^s(g\mid L)}
 \le \frac{C_{p,s,r,\gamma}}{\sqrt n}
       \sum_{j=1}^r\|L_j\|_{n,p}.                           \tag{8.7}
\]

Consequently \(\tau P_L^\perp g\) may be coupled to \(\tau g\) with
normalized \(L^p\) error tending to zero whenever the query norm and
\(\tau\) have the moment bounds proved below.  This applies independently
to both matrices.

### 8.3 The finite ten-step induction

Fix the present nonzero \(h\).  By the rank assumption (1.1) and (5.12), the
finite list of population inverses and nonterminal innovation variances has
a strictly positive minimum; call it \(4\gamma_h\).  At action \(t\), let
\(\mathcal G_t\) be the intersection of the preceding good event with the
requirements that every empirical Gram inverted at that action have least
eigenvalue at least \(2\gamma_h\), and that every newly formed innovation
variance which will be used by a later action be at least
\(2\gamma_h\).  All these quantities are measurable before the action is
revealed.  No lower bound is imposed on the new feature innovation at
\(X^2\) or \(Y^2\).

Stop the coupled representation at the first failure of a good event by
setting subsequent represented fields to zero.  This changes only the proof
representation, not the raw network (2.3)--(2.6).  We prove simultaneously,
for every prescribed finite moment order \(P\), after each of the ten
actions:

1. every constructed stopped field differs from its ideal field by a
   quantity tending to zero in \(L^P(\Omega;\|\cdot\|_{n,P})\);
2. every constructed stopped and ideal field has a uniform moment bound at
   every finite order requested later in the finite proof;
3. every empirical Gram and overlap in (7.2) differs in \(L^P\) from its
   population expectation by a quantity tending to zero;
4. before the two terminal row actions, all three errors above are
   \(O(n^{-1/2})\).

The base \(H^0_j=\phi(U_j)\) is iid.  By (8.2),

\[
 Q_{H,00}^{(n)}\longrightarrow\mathbb E\phi(U)^2=1
\]

in every \(L^P\).  Conditional on \(H^0\), the coordinates of
\(X^0=WH^0/\sqrt n\) are iid \(N(0,Q_{H,00}^{(n)})\).
Coupling them to \(\xi_0\sim N(0,1)\) with the same standard normals and
using

\[
 |\sqrt x-1|\le |x-1|\quad\text{when }x\ge1/2              \tag{8.8}
\]

gives the first field estimate.  The complement of \(x\ge1/2\) has
probability \(O(n^{-M})\) for every \(M\), by applying (8.2) at a
sufficiently high moment order.  Applying the polynomial-Lipschitz map
\(G^0=\phi(X^0)\), followed by (8.2), establishes the base data for
\(Y^0\).  Its conditional Gaussian coupling is the identical argument.

Assume the four assertions hold immediately before a later action.  Every
next query is obtained from earlier fields by finitely many additions,
products, and compositions with \(\phi\) or \(\phi'\).  By the mean-value
theorem and the activation envelope, each such coordinate map \(\Psi\)
satisfies, for some finite integer \(r\),

\[
 |\Psi(x;\theta)-\Psi(x';\theta')|
 \le C(1+\|x\|^r+\|x'\|^r)
       (\|x-x'\|+\|\theta-\theta'\|).                      \tag{8.9}
\]

Here \(\theta\) consists of the finitely many empirical Gram coefficients
already constructed.  Hölder's inequality at moment orders
\(2P,2Pr\) transfers the induction estimate through (8.9), and also gives
all required higher moments.

Every regression coefficient in (4.3) or (4.5) is a rational function of a
fixed finite list of empirical entries in (7.2).  On \(\mathcal G_t\),
matrix inversion is Lipschitz because

\[
 \|A^{-1}-B^{-1}\|
 \le\|A^{-1}\|\,\|A-B\|\,\|B^{-1}\|,                       \tag{8.10}
\]

and both inverse norms are at most \((2\gamma_h)^{-1}\).  A nonterminal
innovation standard deviation is Lipschitz because its variance is at least
\(2\gamma_h\).  Hence its empirical coefficient error is
\(O_{P,h}(n^{-1/2})\).  Use the same fresh Gaussian vector in the actual and
ideal innovations.  The coefficient bounds, (8.7), and Hölder's inequality
then prove the next field estimate.

For every ideal coordinate observable \(\Theta\) in (7.2), its coordinates
within the relevant physical layer are iid and have moments of all orders.
Equation (8.2) gives

\[
 \left\|\frac1n\sum_i\Theta_i-\mathbb E\Theta_1\right\|_{L^P}
 \le C_{P,h}n^{-1/2}.                                      \tag{8.11}
\]

The actual-versus-ideal difference is bounded by (8.9) and Hölder.  This
proves the next Gram and overlap estimates and closes one action.  Since the
list (3.1) has ten entries, repeating this explicitly stated implication ten
times terminates.

At \(X^2\), the population Schur complement for the new \(\xi_2\) may
vanish.  Instead of a Lipschitz square root use

\[
 |\sqrt x-\sqrt y|\le\sqrt{|x-y|},\qquad x,y\ge0.           \tag{8.12}
\]

The resulting normalized error is still \(o(1)\), and is
\(O(n^{-1/4})\) under the preceding bounds.  Although \(G^2\) is then the
query for the following \(V\)-action, that action inverts only the old
two-time matrices \(Q_G^{[1]},K_C^{[1]}\).  Thus (8.9)--(8.11) propagate
the \(o(1)\) query error through \(Y^2\); no inverse or response uses the
possibly singular three-time \(Q_H\).  The same argument with (8.12) handles
the final \(\zeta_2\) innovation.  This proves all four induction assertions,
including the two permitted terminal degeneracies.

For the six-action one-step prefix, apply the same terminal argument one
stage earlier: permit the \(X^1\) innovation to vanish, propagate its
\(o(1)\) error through the polynomial-Lipschitz query \(G^1\), and terminate
at \(Y^1\).  Every inverse before that point is one of the four positive
scalar base Grams in (5.12).  This proves (1.5).

To bound failures, use the induction at an arbitrarily high moment order.
Entrywise Gram convergence, Weyl's eigenvalue inequality, (8.10), and
Markov's inequality imply, for each prescribed \(M\),

\[
 \mathbb P(\mathcal G_t^c\cap\mathcal G_{t-1})
 \le C_{M,h}n^{-M}.                                        \tag{8.13}
\]

The finite union over ten actions has the same bound.  This proof never
requires an unconditional moment bound for an inverse empirical Gram.

### 8.4 Regression coefficients and response identification

Let \(\Theta_{t,n}\) collect the empirical inverse-Gram coefficients and
innovation scales in (4.3) or (4.5).  Extend it off \(\mathcal G_t\) by its
deterministic population value \(\Theta_t\):

\[
 \widetilde\Theta_{t,n}
 =\Theta_{t,n}\mathbf1_{\mathcal G_t}
  +\Theta_t\mathbf1_{\mathcal G_t^c}.                       \tag{8.14}
\]

Equations (8.10)--(8.12) show that
\(\widetilde\Theta_{t,n}\to\Theta_t\) in every finite \(L^P\); hence these
coefficients are uniformly integrable.  Off the good event the raw network
has no inverse-Gram parameter—(8.14) is only a proof device.

Every population cross-moment in (6.4), (6.6), and (6.11) is the limit of a
raw empirical overlap in (7.2).  Equation (6.3) rewrites that already
identified limit as one of the response expectations in (5.3)--(5.6).
Thus the symbols \(\rho^{W,V}\), \(\sigma^{W,V}\) are not assumed
finite-width tangent fields, and no empirical derivative is smuggled into
the argument.

### 8.5 Removing the stopping and passing expectations

It remains to show that the raw network contributes negligibly on the event
discarded in (8.13).  Define normalized Euclidean majorants, with \(M\)
denoting the activation envelope and \(|h|\le1\), by

\[
 \mathsf u_0=\|u^0\|_{n,2},\quad
 \mathsf a_0=\|a^0\|_{n,2},\quad
 \mathsf w_0=\|W/\sqrt n\|_{\rm op},\quad
 \mathsf v_0=\|V/\sqrt n\|_{\rm op},
\]

and, for \(s=0,1\), recursively by

\[
 \begin{aligned}
 \mathsf h_s&=M(1+\mathsf u_s),&
 \mathsf z_s&=\mathsf w_s\mathsf h_s,&
 \mathsf g_s&=M(1+\mathsf z_s),\\
 \mathsf y_s&=\mathsf v_s\mathsf g_s,&
 \mathsf c_s&=M\mathsf a_s,&
 \mathsf d_s&=\mathsf v_s\mathsf c_s,\\
 \mathsf e_s&=M\mathsf d_s,&
 \mathsf b_s&=\mathsf w_s\mathsf e_s,&
 \mathsf a_{s+1}&=\mathsf a_s+M(1+\mathsf y_s),\\
 \mathsf u_{s+1}&=\mathsf u_s+M\mathsf b_s,&
 \mathsf v_{s+1}&=\mathsf v_s+\mathsf c_s\mathsf g_s,&
 \mathsf w_{s+1}&=\mathsf w_s+\mathsf e_s\mathsf h_s.
 \end{aligned}                                               \tag{8.15}
\]

At \(s=2\), use the first four rules to define the terminal forward
majorants.  The exact equations (2.3)--(2.6), Cauchy--Schwarz, and

\[
 \left\|\frac h n xy^T\right\|_{\rm op}
 \le |h|\|x\|_{n,2}\|y\|_{n,2}                             \tag{8.16}
\]

prove by direct substitution that every actual normalized Euclidean field
is bounded by its corresponding quantity in (8.15).  These quantities are
fixed polynomials with nonnegative coefficients in

\[
 1+M+\|u^0\|_{n,2}+\|a^0\|_{n,2}
 +\|W/\sqrt n\|_{\rm op}+\|V/\sqrt n\|_{\rm op}.            \tag{8.17}
\]

By (8.3) and Gaussian vector moments, (8.17) has moments of every order
uniformly in \(n\).  Traversing the finite expression tree for any
coordinate field and using \(\|x\|_p\le\|x\|_2\) produces a bound

\[
 \|X\|_{n,p}\le n^{\alpha_{X,p}}
 P_{X,p}(\text{quantity in (8.17)})                         \tag{8.18}
\]

for a finite exponent and polynomial independent of \(n\).  Choose \(M\)
in (8.13) larger than every exponent occurring in the finite list and apply
Hölder.  With \(T=10\) denoting the end of the ten-action list, the
contribution of \(\mathcal G_T^c\) to every raw field, Gram, and overlap
tends to zero in the required \(L^P\).  Hence all stopped
convergence assertions hold for the unmodified network.

Finally,

\[
 |f_n^s|
 \le\|a^s\|_{n,2}\|\phi(y^s)\|_{n,2}
 \le M\mathsf a_s(1+\mathsf y_s).                           \tag{8.19}
\]

The right-hand side has a uniform \(L^{1+\delta}\) bound for every fixed
\(\delta>0\).  The coupled coordinate convergence and (8.11) therefore
pass through expectation, proving (1.4).  This completes concentration,
uniform integrability, and fixed-nonzero-\(h\) identification.

## 9. Exact rank requirements

For clarity, the nonterminal innovation variances, in chronological order,
are

\[
 K_{C,00}=d,\qquad K_{E,00}=d^2,                            \tag{9.1}
\]

\[
 q_H:=Q_{H,11}-\frac{Q_{H,01}^2}{Q_{H,00}},\qquad
 q_G:=Q_{G,11}-\frac{Q_{G,01}^2}{Q_{G,00}},                 \tag{9.2}
\]

\[
 k_C:=K_{C,11}-\frac{K_{C,01}^2}{K_{C,00}},\qquad
 k_E:=K_{E,11}-\frac{K_{E,01}^2}{K_{E,00}}.                 \tag{9.3}
\]

The action \(X^1\) creates \(q_H\), which must be positive because
\((H^0,H^1)\) is used in \(S^1\) and \(X^2\).  The action \(Y^1\) creates
\(q_G\), used in \(R^1\) and \(Y^2\).  The actions \(R^1,S^1\) create
\(k_C,k_E\), used in \(Y^2,X^2\), respectively.  Therefore

\[
 q_H,q_G,k_C,k_E>0                                         \tag{9.4}
\]

is equivalent to the four positive-definiteness assumptions (1.1), in view
of (5.12).  No mixed \(W\)-\(V\) Gram is inverted: independence of the two
residual matrices in Lemma 4.1 and the response identities of Section 6
account for all cross-layer dependence.

The Schur complement for \(\xi_2\) at \(X^2\) may be zero because there is
no later \(W^T\) action.  The Schur complement for \(\zeta_2\) at \(Y^2\)
may likewise be zero.  Thus neither
\((Q_{H,rs})_{0\le r,s\le2}\) nor
\((Q_{G,rs})_{0\le r,s\le2}\) needs to be invertible.

At \(h=0\), the two-time Grams are singular because time-zero and time-one
fields coincide.  This causes no limit-order problem: at \(h=0\) every
finite-width update is the identity and the centered readout has expected
output zero.  For \(h\ne0\), the result proved here is pointwise at that
fixed \(h\).  A quantitative theorem may subsequently prove (9.4) for
\(0<|h|\le h_\phi\) and only then study \(h\to0\) in the already identified
Gaussian DAG.

## 10. Width-bridge conclusion and remaining obligation

Sections 2--8 prove the claimed fixed-step identification of the actual
finite network, including adaptive dependence through both reused matrices,
every response cancellation, all empirical conditioning data, concentration,
and uniform integrability.  The bridge uses precisely the four rank
inequalities (9.4).

Accordingly, this note leaves no dynamic-cavity or state-evolution gap.
For the full quantitative half-step theorem, the separate tasks are:

1. prove an activation-defined \(h_\phi>0\) on which (9.4) holds;
2. prove \(C^5\) regularity of the width-first DAG at the singular point
   \(h=0\);
3. compute its cubic coefficient and an activation-envelope fifth-order
   remainder.

Those analytic tasks are not asserted in this width-identification note.
