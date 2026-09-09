# Quantitative two-versus-one comparison at arbitrary depth

## Theorem

Fix a hidden depth \(L\ge1\).  All hidden widths are \(n\), the input is
the scalar \(1\), and there are no biases.  Assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,\qquad G\sim N(0,1),
\]

and

\[
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
 \tag{T.1}
\]

Let \(F_{k,n,L}(h)\) be the expected output after \(k\) simultaneous,
recomputed feature-ascent steps of size \(h\).  The limit order is

\[
 F_{k,L}(h)=\lim_{n\to\infty}F_{k,n,L}(h)
 \quad\text{at fixed }h,
 \tag{T.2}
\]

followed only afterwards by \(h\to0\).  Put

\[
 \Delta_L(\eta)=F_{2,L}(\eta)-F_{1,L}(2\eta).
 \tag{T.3}
\]

Sections 1--5 below construct

\[
 \kappa_{\phi,L},\qquad B_\phi\ge1,qquad 0<h_\phi\le\tfrac12,
 \qquad E_L\in\mathbb N,
\]

where \(B_\phi,h_\phi\) depend only on \(\phi\), \(E_L\) depends only on
\(L\), and \(\kappa_{\phi,L}\) is a terminating finite recursion of
Gaussian activation integrals.  They satisfy

\[
 \boxed{
 \left|\Delta_L(\eta)-\kappa_{\phi,L}\eta^3\right|
 \le B_\phi^{E_L}|\eta|^5,
 \qquad |\eta|\le h_\phi^{E_L}.}
 \tag{T.4}
\]

A completely explicit, deliberately coarse choice is given in (5.1)--(5.5).
In particular, for every \(\varepsilon>0\),

\[
 |\Delta_L(\eta)|
 \le (|\kappa_{\phi,L}|+\varepsilon)|\eta|^3
 \tag{T.5}
\]

whenever

\[
 |\eta|\le
 \eta_0(\phi,L,\varepsilon)
 :=\min\left\{h_\phi^{E_L},
 \sqrt{\frac{\varepsilon}{1+B_\phi^{E_L}}}\right\}.
 \tag{T.6}
\]

No constant in this theorem is defined using a supremum or continuity
modulus of \(F_{1,L},F_{2,L},\Delta_L\), a trained trajectory, or an
opposite-limit initialization derivative.

## 1. Exact network and fixed-step width limit

At time \(s\), set

\[
 Z_1^s=u^s,\qquad X_1^s=\phi(Z_1^s),
\]

\[
 Z_\ell^s=\frac{W_\ell^sX_{\ell-1}^s}{\sqrt n},\qquad
 X_\ell^s=\phi(Z_\ell^s),\qquad 2\le\ell\le L,
\]

\[
 f_{n,L}^s=\frac1n(a^s)^TX_L^s.
 \tag{1.1}
\]

All entries of \(u^0,a^0,W_2^0,\ldots,W_L^0\) are mutually independent
standard Gaussians.  Define cotangents by

\[
 D_L^s=a^s\odot\phi'(Z_L^s),
\]

\[
 R_{\ell-1}^s=\frac{(W_\ell^s)^TD_\ell^s}{\sqrt n},\qquad
 D_{\ell-1}^s=R_{\ell-1}^s\odot\phi'(Z_{\ell-1}^s).
 \tag{1.2}
\]

The exact ascent update \(\theta^{s+1}=\theta^s+hn\nabla f_{n,L}^s\) is

\[
 a^{s+1}=a^s+hX_L^s,\qquad
 W_\ell^{s+1}=W_\ell^s+\frac h{\sqrt n}D_\ell^s(X_{\ell-1}^s)^T,
 \qquad
 Z_1^{s+1}=Z_1^s+hD_1^s.
 \tag{1.3}
\]

Writing \(Q^a_{rs}=n^{-1}(X_a^r)^TX_a^s\) and
\(K^a_{rs}=n^{-1}(D_a^r)^TD_a^s\), the learned pieces separate exactly:

\[
 Z_\ell^s=\frac{W_\ell^0X_{\ell-1}^s}{\sqrt n}
       +h\sum_{r<s}Q^{\ell-1}_{rs}D_\ell^r,
\]

\[
 R_{\ell-1}^s=\frac{(W_\ell^0)^TD_\ell^s}{\sqrt n}
       +h\sum_{r<s}K^\ell_{rs}X_{\ell-1}^r.
 \tag{1.4}
\]

There is no current-time term.  The two-step chronology consists of

\[
 \begin{array}{c}
 W_2X_1^0,\ldots,W_LX_{L-1}^0;\quad
 W_L^TD_L^0,\ldots,W_2^TD_2^0;\\
 W_2X_1^1,\ldots,W_LX_{L-1}^1;\quad
 W_L^TD_L^1,\ldots,W_2^TD_2^1;\\
 W_2X_1^2,\ldots,W_LX_{L-1}^2,
 \end{array}
 \tag{1.5}
\]

namely \(5(L-1)\) predictable actions.  In particular,
\(X_{\ell-1}^1\) is allowed to depend on the already exposed column action
of the same reused matrix.

For each connector \(2\le\ell\le L\), introduce independent forward and
transpose Gaussian source blocks \(\xi_\ell,\chi_\ell\), with

\[
 \mathbb E\xi_{\ell,r}\xi_{\ell,s}
  =\mathbb E X_{\ell-1,r}X_{\ell-1,s},\qquad
 \mathbb E\chi_{\ell,r}\chi_{\ell,s}
  =\mathbb E D_{\ell,r}D_{\ell,s}.
 \tag{1.6}
\]

Define

\[
 \rho^\ell_{sr}=\mathbb E[\partial_{\chi_{\ell,r}}X_{\ell-1,s}],
 \quad r<s,
\qquad
 \sigma^\ell_{sr}=\mathbb E[\partial_{\xi_{\ell,r}}D_{\ell,s}],
 \quad r\le s.
 \tag{1.7}
\]

The inverse-free population DAG is

\[
 Z_{1,0}=U,\qquad X_{1,s}=\phi(Z_{1,s}),\qquad
 Z_{1,s+1}=Z_{1,s}+hD_{1,s},
\]

\[
 Z_{\ell,s}=\xi_{\ell,s}
 +\sum_{r<s}(\rho^\ell_{sr}+hQ^{\ell-1}_{rs})D_{\ell,r},
 \qquad X_{\ell,s}=\phi(Z_{\ell,s}),
 \tag{1.8}
\]

\[
 R_{\ell-1,s}=\chi_{\ell,s}
 +\sum_{r\le s}\sigma^\ell_{sr}X_{\ell-1,r}
 +h\sum_{r<s}K^\ell_{rs}X_{\ell-1,r},
\qquad
 D_{\ell-1,s}=R_{\ell-1,s}\phi'(Z_{\ell-1,s}),
 \tag{1.9}
\]

and

\[
 A_s=A+h\sum_{r<s}X_{L,r},\qquad
 D_{L,s}=A_s\phi'(Z_{L,s}),\qquad
 F_{k,L}(h)=\mathbb E[A_kX_{L,k}].
 \tag{1.9a}
\]

The fixed-step bridge is not assumed.  It is proved in
`WIDTH_GENERAL.md` as follows.  Conditional on any global predictable
interlacing of the \(L-1\) matrices, each reused matrix has the exact
residual decomposition

\[
 W=P_CW+WP_H-P_CWP_H+P_C^\perp\widetilde W P_H^\perp,
 \tag{1.10}
\]

and the residual matrices \(\widetilde W\) remain conditionally independent.
The proof exposes one Gaussian row or column at a time and inducts over the
explicit list (1.5).  Gaussian integration by parts gives, for an old row
query vector \(x\), old cotangent vector \(d\), and their raw actions,

\[
 \mathbb E[d\,X_{\rm new}]=K\rho+Sq,
 \qquad
 \mathbb E[y\,D_{\rm new}]=Q\sigma+Pk.
 \tag{1.11}
\]

Substitution in the exact row/column regression formulas cancels the two
cross-projection terms and leaves exactly (1.8)--(1.9).  This proves every
response term, including the reused-column dependence of time-one features.

The same action induction couples every innovation to an iid ideal
coordinate array.  Rosenthal's inequality controls all empirical Grams and
overlaps; the finite-rank Gaussian projection estimate controls the removed
old-query projections.  On stopped events, inverse-Gram coefficients are
Lipschitz; failure probabilities are \(O(n^{-m})\) for arbitrary \(m\).
An explicit forward/backward Euclidean-norm recursion bounds the raw network
by a polynomial in the initialization Gaussian vector norms and normalized
matrix operator norms, removing the stopping and proving uniform
integrability.  At terminal time two, the inequality

\[
 |\sqrt x-\sqrt y|\le\sqrt{|x-y|}
 \tag{1.12}
\]

handles a zero innovation without ever inverting a three-time Gram.
Consequently, at every fixed nonzero \(h\), the finite-width \(F_{2,n,L}(h)\)
converges to (1.8)--(1.9) whenever precisely the \(2(L-1)\) matrices

\[
 Q^{a,[1]}(h),\quad1\le a\le L-1,
 \qquad
 K^{a,[1]}(h),\quad2\le a\le L
 \tag{1.13}
\]

are positive definite.  The \(3(L-1)\)-action one-step prefix is rank-free:
it inverts only \(Q^a_{00}=1\) and
\(K^a_{00}=d^{L-a+1}\).  Thus it identifies \(F_{1,L}(2h)\) at every fixed
\(h\).  This closes the width-first bridge before any small-step argument.

## 2. The inductive two-time ranks

Assume in this section that \(L\ge2\).  When \(L=1\) there is no reused
matrix and hence no Gram-rank obligation; the scalar two-step call in
Section 3 applies directly.

Let

\[
 g=\phi(G),\quad p=\phi'(G),\quad q=\phi''(G),
\]

and define the activation integrals

\[
 d=\mathbb Ep^2,\quad u=\mathbb Ep^4,\quad v=\mathbb E[gq],
 \quad m=\mathbb E[gp^2q],
\]

\[
 r=\mathbb E[p\phi'''(G)],\quad s=\mathbb Eq^2,
 \quad e=\mathbb E[p^2q^2],\quad \ell=\mathbb E[g^2p^2].
 \tag{2.1}
\]

Assume \(d>0\).  Put

\[
 \Theta_a=\sum_{j=0}^a d^j,\qquad
 b_a=d^{L-a},\qquad \pi_a=d^{L-a+1}.
 \tag{2.2}
\]

Here \(b_a\) and \(\pi_a\) are the initialization variances of the reverse
carrier and cotangent at layer \(a\).  The forward induction is

\[
 V_0=0,\qquad
 V_a=dV_{a-1}+\Theta_{a-1}^2b_au,
 \qquad1\le a\le L.
 \tag{2.3}
\]

The reverse induction is initialized by

\[
 \beta_{L+1}=0,\qquad\gamma_{L+1}=1,
\]

and, for \(a=L,L-1,\ldots,1\), is

\[
 \begin{aligned}
 \beta_a={}&b_aV_{a-1}s+3\Theta_{a-1}^2b_a^2e+d\beta_{a+1}
 +\gamma_{a+1}^2\ell
 +2\Theta_{a-1}\gamma_{a+1}b_am,\\
 \gamma_a={}&\pi_a+\Theta_{a-1}b_a(r+s)
 +\gamma_{a+1}(v+d).
 \end{aligned}
 \tag{2.4}
\]

These formulas are not guessed jets.  In the already width-limited DAG,
the time-one feature tangent has the stochastic representation

\[
 P_a=p(Z_a)\left(\sqrt{V_{a-1}}E_a
              +\Theta_{a-1}R_ap(Z_a)\right),
 \tag{2.5}
\]

where \(Z_a,E_a,R_a\) are independent and
\(R_a\sim N(0,b_a)\).  Hence \(\mathbb EP_a^2=V_a\) and
\(\mathbb E[X_{a,0}P_a]=0\).  The learned contribution gives \(1\), while
the differentiated reused-matrix response gives
\(d\Theta_{a-2}\); this proves the coefficient \(\Theta_{a-1}\) in
(2.5).

Likewise, the cotangent tangent is exactly

\[
 T_a=\sqrt{\beta_{a+1}}B_ap
 +\gamma_{a+1}gp
 +\sqrt{V_{a-1}}R_aE_aq
 +\Theta_{a-1}R_a^2pq,
 \tag{2.6}
\]

with fresh \(B_a\).  Squaring (2.6) proves the first line of (2.4).  The
derivative of the sum of the two transpose responses is

\[
 \mathbb E[\partial_{Z_a}T_a]
 =\gamma_{a+1}(v+d)+\Theta_{a-1}b_a(r+s),
 \tag{2.7}
\]

and the learned transpose term contributes \(\pi_a\), proving the second
line.  Thus every reused-matrix response is present in the induction.

A signed Gaussian realization of each coalescing two-time source gives

\[
 \boxed{
 \lim_{h\to0}\frac{\det Q^{a,[1]}(h)}{h^2}=V_a,
 \quad1\le a\le L-1,}
\]

\[
 \boxed{
 \lim_{h\to0}\frac{\det K^{a,[1]}(h)}{h^2}=\pi_a\beta_a,
 \quad2\le a\le L.}
 \tag{2.8}
\]

Positivity follows from the stochastic squares, not by discarding the
possibly signed cross term in (2.4).  At the top, the fresh
\(\sqrt{V_{L-1}}R_LE_Lq\) component is nonzero when \(s>0\).  If \(s=0\),
then \(\phi\) is nonconstant affine and \(\beta_L=\ell=d>0\).  Downward,
the fresh \(B_a\)-component gives \(\beta_a\ge d\beta_{a+1}\).

With

\[
 \widehat s=\begin{cases}s,&s>0,\\1,&s=0,\end{cases}
 \qquad
 \lambda_\phi=\min\{1,d,u,\ell,\widehat s\}>0,
 \tag{2.9}
\]

the same induction yields the common explicit lower bound

\[
 \boxed{a_{G,L}\ge\lambda_\phi^{4L}}
 \tag{2.10}
\]

for every leading coefficient in (2.8).  `RANK_GENERAL.md` supplies the
signed-source proof, the complete response calculation, and the finite
fourth-order Price compiler that turns (2.8) into a punctured rank interval.

## 3. Singular regularity and the exact cubic coefficient

The full inverse-free call list, singular-covariance regularization
argument, and finite envelope recursion used in this section are proved in
`COMPILER_GENERAL.md`, Sections 1--4.  We record their outputs here in the
notation of the theorem.

For a Gaussian expectation node

\[
 N(h)=\mathbb E_{Y\sim N(0,\Sigma(h))}\psi(h,Y),
\]

define

\[
 {\cal P}_\Sigma=\partial_h+\frac12\Sigma'(h):D_Y^2,
 \qquad \Psi_0=\psi,\qquad \Psi_{j+1}={\cal P}_\Sigma\Psi_j.
 \tag{3.1}
\]

Fourier differentiation of the Gaussian characteristic function proves
(3.1) without a covariance inverse, including when \(\Sigma(0)\) is
singular.  Cutoff, mollification, and the polynomial Gaussian envelope
from (T.1) justify five iterations.

For \(L\ge2\), evaluate the population DAG in the following \(3L-2\)
local calls:

1. one bottom time-one feature call;
2. \(L-2\) interior time-one forward calls;
3. one top time-one call, producing \(F_{1,L}\) and \(K^{L,[1]}\);
4. \(L-2\) downward time-one cotangent calls;
5. one bottom time-two call;
6. \(L-2\) terminal interior forward calls;
7. one terminal top call, producing \(F_{2,L}\).

For \(L=1\), the same count equals one: a single expectation over
independent \((A,U)\) evaluates the exact simultaneous scalar recursions
\(A_{s+1}=A_s+h\phi(Z_s)\) and
\(Z_{s+1}=Z_s+hA_s\phi'(Z_s)\) for \(s=0,1\).

Each call has Gaussian dimension at most five.  Earlier Gram and response
jets are inserted as formal tokens \(S^{[j]}\) with
\(\partial_hS^{[j]}=S^{[j+1]}\).  Applying (3.1) node by node defines

\[
 {\cal J}_r(N)=
 \mathbb E_{N(0,\Sigma(0))}[\Psi_r(0,Y)],
 \qquad0\le r\le5.
 \tag{3.2}
\]

This is an acyclic definition by Gaussian integrals.  Only afterwards does
singular Price differentiation identify \({\cal J}_r(N)=N^{(r)}(0)\).
At \(h=0\), use independent standard Gaussians

\[
 A,G_1,\ldots,G_L,B_1,\ldots,B_{L-1},
\]

with

\[
 \xi_{\ell,0}=\xi_{\ell,1}=\xi_{\ell,2}=G_\ell,
 \qquad
 \chi_{\ell,0}=\chi_{\ell,1}
 =d^{(L-\ell+1)/2}B_{\ell-1}.
 \tag{3.3}
\]

Thus every value in (3.2) is a finite product-Gaussian integral of
\(\phi,\ldots,\phi^{(12)}\).  Equivalently, expansion reduces it to finitely
many one-dimensional activation integrals

\[
 I_{a,\alpha}(\phi)=
 \mathbb E\left[G^a\prod_{r=0}^{12}\phi^{(r)}(G)^{\alpha_r}\right]
 \tag{3.4}
\]

and elementary Gaussian moments.  Define, before identifying any output
derivative,

\[
 \boxed{
 \kappa_{\phi,L}=
 \frac{{\cal J}_3(F_{2,L})-8{\cal J}_3(F_{1,L})}{6}.}
 \tag{3.5}
\]

The nodewise Price theorem then proves

\[
 6\kappa_{\phi,L}=F_{2,L}^{(3)}(0)-8F_{1,L}^{(3)}(0).
 \tag{3.6}
\]

The sign change

\[
 h\mapsto-h,\qquad A\mapsto-A,\qquad
 \chi_{\ell,s}\mapsto-\chi_{\ell,s}
 \tag{3.7}
\]

leaves every feature and feature Gram fixed and negates every cotangent,
response, learned-plus-response coefficient, and output.  Hence both
outputs are odd.  Direct first-order evaluation of the same Price calls
gives

\[
 {\cal J}_1(F_{1,L})=\Theta_L,\qquad
 {\cal J}_1(F_{2,L})=2\Theta_L.
 \tag{3.8}
\]

Therefore \(\Delta_L^{(j)}(0)=0\) for \(j=0,1,2,4\), and
\(\Delta_L^{(3)}(0)=6\kappa_{\phi,L}\).  None of these identities imports
an initialization jet from the opposite limit order.

## 4. Exact activation-envelope constants

For completeness, an exact depth-specific compiler is as follows.  An
envelope \((C,p)\) means \(|g(x)|\le C(1+\|x\|)^p\).  Propagate sums and
products by

\[
 (C,p)\oplus(D,q)=(C+D,\max\{p,q\}),\qquad
 (C,p)\odot(D,q)=(CD,p+q),
 \tag{4.1}
\]

and use

\[
 {\cal E}(\phi(g))=(M_\phi(1+C),p),\qquad
 {\cal E}(\phi^{(r)}(g))=(M_\phi,0),\quad1\le r\le12.
 \tag{4.2}
\]

For a \(D\)-dimensional call, set

\[
 \mu_{D,p}(v)=
 \sum_{r=0}^p{p\choose r}v^{r/2}2^{r/2}
 \frac{\Gamma((D+r)/2)}{\Gamma(D/2)}.
 \tag{4.3}
\]

If \(\bar c_j\) bounds the entrywise norm of \(\Sigma^{(j)}\), initialize
the envelopes of every
\(\partial_h^j\partial_Y^\alpha\psi\) with
\(j+\lceil|\alpha|/2\rceil\le5\), and recurse by

\[
 P^{(q+1)}_{j,s}=P^{(q)}_{j+1,s}
 \oplus\bigoplus_{a=0}^j
 \left[
 \left(\tfrac12{j\choose a}\bar c_{a+1},0\right)
 \odot P^{(q)}_{j-a,s+2}
 \right].
 \tag{4.4}
\]

If \(P^{(q)}_{0,0}=(C_q,p_q)\), set

\[
 \overline{\cal J}_q(N)=C_q\mu_{D,p_q}(\bar c_0).
 \tag{4.5}
\]

Covariance bounds are entrywise sums of already compiled Gram bounds; a
response uses its differentiated integrand; and

\[
 \overline{(S+hQ)}_j=\bar S_j+\bar Q_j+j\bar Q_{j-1}.
 \tag{4.6}
\]

The \(3L-2\) calls in Section 3 make (4.1)--(4.6) a finite recursion.
Because \(j+s\le10\) and a response begins with at most \(\phi''\), no
derivative above \(\phi^{(12)}\) occurs.  It proves \(C^5\) regularity at
the singular covariance and returns activation-defined numbers

\[
 \overline{\cal J}_5(F_{1,L}),\qquad
 \overline{\cal J}_5(F_{2,L}).
\]

Define the sharper depth-specific remainder constant

\[
 \mathfrak B_{\phi,L}=
 \frac{\overline{\cal J}_5(F_{2,L})
       +32\overline{\cal J}_5(F_{1,L})}{120}.
 \tag{4.7}
\]

For every Gram in (1.13), let \(D_{G,L}\) be the explicit fourth-derivative
determinant bound obtained from the same compiler and Leibniz's rule.  With
the leading coefficient \(a_{G,L}\) from (2.8), define

\[
 \mathfrak h_{\phi,L}=
 \min\left\{\frac12,
 \min_G\min\left(1,\sqrt{\frac{12a_{G,L}}{1+D_{G,L}}}\right)\right\}.
 \tag{4.8}
\]

Evenness and Taylor's theorem give

\[
 \det G(h)\ge\frac12a_{G,L}h^2>0,
 \qquad0<|h|\le\mathfrak h_{\phi,L}.
 \tag{4.9}
\]

Thus (4.8) supplies exactly the ranks required by the already-proved
fixed-\(h\) identification.  Both (4.7) and (4.8) are terminating formulas
from activation data; neither is output-defined.

## 5. Separating activation and depth

The finite syntax count underlying the numerical constants below is Lemma
6.1 of `COMPILER_GENERAL.md`; in particular, that lemma explicitly counts
the ordered spatial multiindices and every covariance contraction.

Define universal integers

\[
 c_0=128,\qquad c_{r+1}=8(c_r+1)^2\quad(0\le r<20),
 \qquad C_*=c_{20},\qquad q_*=2C_*.
 \tag{5.1}
\]

Expanding the eight local templates (the seven depth-\(L\) call types and
the \(L=1\) scalar call) gives respective maximum syntax sizes
\(19,19,33,55,79,77,47,47\).  Ten formal derivatives, one initial
response derivative, and five Price/Leibniz assemblies are dominated by
the twenty-step recursion in (5.1).  Consequently, if every incoming token
and covariance derivative is at most \(S\ge2\), every returned bar is at
most

\[
 A_*S^{q_*},\qquad
 A_*=2^{C_*}M_\phi^{C_*}\mu_{5,C_*}(25C_*^2).
 \tag{5.2}
\]

Now set

\[
 \boxed{
 B_\phi=\max\{32,M_\phi^2,\lambda_\phi^{-1},A_*\},
 \qquad h_\phi=B_\phi^{-1}.}
 \tag{5.3}
\]

These two bases are independent of depth.  Put

\[
 e_L=(2L+1)q_*^{3L},
 \qquad
 \boxed{E_L=2e_L+2L+1.}
 \tag{5.4}
\]

The initial covariance tokens are at most \(B_\phi^{2L}\).  Iterating the
one-call estimate through \(3L-2\) calls yields

\[
 \overline{\cal J}_5(F_{1,L}),
 \overline{\cal J}_5(F_{2,L})\le B_\phi^{e_L},
 \qquad
 D_{G,L}\le B_\phi^{3e_L}.
 \tag{5.5}
\]

Equations (2.10), (5.3), and (5.5) imply

\[
 h_\phi^{E_L}\le\mathfrak h_{\phi,L},
 \qquad
 \mathfrak B_{\phi,L}\le B_\phi^{E_L}.
 \tag{5.6}
\]

Thus for each fixed nonzero \(|\eta|\le h_\phi^{E_L}\), Section 1 first
identifies the actual width limit with the Gaussian DAG.  Sections 3--4
then give \(C^5\) regularity and

\[
 |\Delta_L^{(5)}(\eta)|
 \le\overline{\cal J}_5(F_{2,L})
 +32\overline{\cal J}_5(F_{1,L}).
\]

Oddness, the direct linear cancellation, and (3.5)--(3.6) give Taylor's
integral remainder

\[
 \Delta_L(\eta)-\kappa_{\phi,L}\eta^3
 =\frac1{24}\int_0^\eta(\eta-t)^4\Delta_L^{(5)}(t)\,dt.
 \tag{5.7}
\]

Equations (4.7), (5.5)--(5.7) prove (T.4).  Under (T.6),

\[
 B_\phi^{E_L}|\eta|^2
 \le\frac{B_\phi^{E_L}}{1+B_\phi^{E_L}}\varepsilon
 \le\varepsilon,
\]

which proves (T.5).

If \(d=0\), continuity and Gaussian full support imply \(\phi'\equiv0\),
so normalization gives \(\phi\equiv\pm1\).  Then
\(F_{k,L}(h)=kh\) exactly and \(\Delta_L\equiv0\).  One may take
\(\kappa_{\phi,L}=0\), \(B_\phi=1\), \(h_\phi=1/2\), and any positive
\(E_L\).  This also completes the exceptional case.
