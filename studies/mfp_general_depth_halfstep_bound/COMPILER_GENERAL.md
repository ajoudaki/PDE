# The general-depth singular-Price compiler and explicit depth factors

This note treats only the regularity, cubic coefficient, and quantitative
remainder in the width-first Gaussian DAG.  The finite-width identification
of that DAG and the two-time rank calculation are separate lemmas.  No
finite-width Taylor expansion is used here.

Fix a hidden depth \(L\geq1\), let \(G\sim N(0,1)\), and assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
 \tag{1.1}
\]

\[
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
 \tag{1.2}
\]

Write

\[
 d=\mathbb E\phi'(G)^2.
 \tag{1.3}
\]

The case \(d=0\) is dealt with in Section 7.  Until then \(d>0\).

## 1. The inverse-free population nodes

The hidden activation, preactivation, and cotangent at layer
\(\ell\in\{1,\ldots,L\}\) and time \(s\in\{0,1,2\}\) are denoted by
\(X_{\ell s},Z_{\ell s},D_{\ell s}\).  The output weight is \(A_s\).
For the matrix taking layer \(\ell-1\) to layer \(\ell\),
\(2\le\ell\le L\), let

\[
 \xi_{\ell s}\quad\hbox{and}\quad\chi_{\ell s}
 \tag{1.4}
\]

be respectively its forward and transpose raw Gaussian sources.  Sources
belonging to different matrices or different directions are independent.
Their time covariances are

\[
 \mathbb E\xi_{\ell r}\xi_{\ell s}
   =Q^{\ell-1}_{rs}:=\mathbb E[X_{\ell-1,r}X_{\ell-1,s}],
 \tag{1.5}
\]

\[
 \mathbb E\chi_{\ell r}\chi_{\ell s}
   =K^\ell_{rs}:=\mathbb E[D_{\ell r}D_{\ell s}].
 \tag{1.6}
\]

For \(r<s\), and for \(r\le s\), respectively, define the response
nodes

\[
 \rho^\ell_{sr}
 =\mathbb E\,\partial_{\chi_{\ell r}}X_{\ell-1,s},
 \qquad
 \sigma^\ell_{sr}
 =\mathbb E\,\partial_{\xi_{\ell r}}D_{\ell s},
 \tag{1.7}
\]

and the full learned-plus-response coefficients

\[
 R^\ell_{sr}=\rho^\ell_{sr}+hQ^{\ell-1}_{rs}\quad(r<s),
 \tag{1.8}
\]

\[
 T^\ell_{sr}=\sigma^\ell_{sr}+hK^\ell_{rs}\quad(r<s),
 \qquad T^\ell_{ss}=\sigma^\ell_{ss}.
 \tag{1.9}
\]

The inverse-free DAG is

\[
 Z_{1,0}=U,\qquad X_{1,s}=\phi(Z_{1,s}),
 \qquad Z_{1,s+1}=Z_{1,s}+hD_{1,s},
 \tag{1.10}
\]

\[
 Z_{\ell s}=\xi_{\ell s}
       +\sum_{r<s}R^\ell_{sr}D_{\ell r},
 \qquad X_{\ell s}=\phi(Z_{\ell s})
 \quad(2\le\ell\le L),
 \tag{1.11}
\]

\[
 A_s=A+h\sum_{r<s}X_{Lr},
 \qquad D_{Ls}=A_s\phi'(Z_{Ls}),
 \tag{1.12}
\]

and, downward for \(\ell=L-1,\ldots,1\),

\[
 H_{\ell s}=\chi_{\ell+1,s}
       +\sum_{r\le s}T^{\ell+1}_{sr}X_{\ell r},
 \qquad
 D_{\ell s}=H_{\ell s}\phi'(Z_{\ell s}).
 \tag{1.13}
\]

At time zero all responses in (1.7) vanish: the derivative contains a
centered, independent upper carrier.  Consequently

\[
 Q^\ell_{00}=1,\qquad K^\ell_{00}=d^{L-\ell+1},
 \quad 1\le\ell\le L,
 \tag{1.14}
\]

where \(Q^L\) is not used as a matrix input.  The limiting outputs are

\[
 F_{s,L}(h)=\mathbb E[A_sX_{Ls}],\qquad s=1,2.
 \tag{1.15}
\]

Equations (1.5)--(1.13) contain no covariance inverse.  They therefore
remain meaningful when all repeated-time covariances coalesce at \(h=0\).

## 2. The \(3L-2\) chronological calls

Here is a complete acyclic evaluation order for \(L\ge2\).  A bracket
\([m]\) on a Gram means the principal block with times \(0,\ldots,m\).
Every expectation and response displayed in a call is compiled before the
next call starts.

1. **First bottom call.**  On
   \((U,\chi_{2,0})\), with covariance
   \([1]\oplus[d^{L-1}]\), compute
   \(Z_{1,0},Z_{1,1},X_{1,0},X_{1,1}\), then
   \(Q^1[1],\rho^2_{10},R^2_{10}\).

2. **First interior forward calls.**  For
   \(\ell=2,\ldots,L-1\), in increasing order, use
   \((\xi_{\ell,0},\xi_{\ell,1},\chi_{\ell+1,0})\), with covariance
   \(Q^{\ell-1}[1]\oplus[d^{L-\ell}]\).  Reconstruct
   \(D_{\ell,0}=\chi_{\ell+1,0}\phi'(\xi_{\ell,0})\), form
   \(Z_{\ell,0},Z_{\ell,1},X_{\ell,0},X_{\ell,1}\), and compute
   \(Q^\ell[1],\rho^{\ell+1}_{10},R^{\ell+1}_{10}\).

3. **First top call.**  On
   \((A,\xi_{L,0},\xi_{L,1})\), with covariance
   \([1]\oplus Q^{L-1}[1]\), compute the time-zero and time-one top
   fields, \(A_1,D_{L,0},D_{L,1}\), \(K^L[1]\),
   \(\sigma^L_{10},\sigma^L_{11},T^L_{10},T^L_{11}\), and
   \({\cal O}_{1,L}=F_{1,L}\).

4. **First backward calls.**  For
   \(\ell=L-1,\ldots,2\), in decreasing order, use
   \((\xi_{\ell,0},\xi_{\ell,1},
      \chi_{\ell+1,0},\chi_{\ell+1,1})\), with covariance
   \(Q^{\ell-1}[1]\oplus K^{\ell+1}[1]\).  Reconstruct the two
   forward fields and form
   \(H_{\ell,0},H_{\ell,1},D_{\ell,0},D_{\ell,1}\).  Compute
   \(K^\ell[1]\), \(\sigma^\ell_{10},\sigma^\ell_{11}\), and
   \(T^\ell_{10},T^\ell_{11}\).

5. **Second bottom call.**  On
   \((U,\chi_{2,0},\chi_{2,1})\), with covariance
   \([1]\oplus K^2[1]\), reconstruct the time-zero and time-one
   bottom fields, then form \(Z_{1,2},X_{1,2}\).  Compute
   \(Q^1_{r2},\rho^2_{2r},R^2_{2r}\), \(0\le r\le2\) for the Gram
   and \(0\le r<2\) for the responses.

6. **Terminal interior forward calls.**  For
   \(\ell=2,\ldots,L-1\), in increasing order, use
   \((\xi_{\ell,0},\xi_{\ell,1},\xi_{\ell,2},
      \chi_{\ell+1,0},\chi_{\ell+1,1})\), with covariance
   \(Q^{\ell-1}[2]\oplus K^{\ell+1}[1]\).  Reconstruct the time-zero
   and time-one forward and cotangent fields, form \(Z_{\ell,2},X_{\ell,2}\),
   and compute \(Q^\ell_{r2}\) for \(0\le r\le2\), and
   \(\rho^{\ell+1}_{2r},R^{\ell+1}_{2r}\) for \(0\le r<2\).

7. **Final top call.**  On
   \((A,\xi_{L,0},\xi_{L,1},\xi_{L,2})\), with covariance
   \([1]\oplus Q^{L-1}[2]\), reconstruct the time-zero and time-one
   top fields and form

   \[
    A_2=A+h(X_{L0}+X_{L1}),\qquad
    Z_{L2}=\xi_{L2}+R^L_{20}D_{L0}+R^L_{21}D_{L1},
   \]

   then compile \({\cal O}_{2,L}=F_{2,L}=\mathbb E[A_2\phi(Z_{L2})]\).

The number of calls is

\[
 1+(L-2)+1+(L-2)+1+(L-2)+1=3L-2.
 \tag{2.1}
\]

Every Gaussian dimension is at most five.  For \(L=1\), the single call
uses independent \((A,U)\) and the exact scalar recursion

\[
 A_{s+1}=A_s+h\phi(Z_s),\qquad
 Z_{s+1}=Z_s+hA_s\phi'(Z_s),\quad s=0,1,
 \tag{2.2}
\]

and compiles both \(\mathbb E[A_1\phi(Z_1)]\) and
\(\mathbb E[A_2\phi(Z_2)]\).  Thus (2.1) also holds for \(L=1\).

## 3. Singular Price differentiation

An envelope is a pair \((C,p)\), meaning

\[
 |g(x)|\le C(1+\|x\|)^p.
 \tag{3.1}
\]

Use

\[
 (C,p)\oplus(D,q)=(C+D,\max\{p,q\}),\qquad
 (C,p)\odot(D,q)=(CD,p+q).
 \tag{3.2}
\]

Initialize \({\cal E}(1)={\cal E}(h)=(1,0)\),
\({\cal E}(x_i)=(1,1)\), and use

\[
 {\cal E}(\phi(g))=(M_\phi(1+C),p),\qquad
 {\cal E}(\phi^{(r)}(g))=(M_\phi,0),\quad1\le r\le12,
 \tag{3.3}
\]

when \({\cal E}(g)=(C,p)\).  Products, sums, and formal derivatives are
expanded exactly.  For an earlier scalar node \(S\), introduce tokens
\(S^{[j]}\), with

\[
 \partial_hS^{[j]}=S^{[j+1]},\qquad
 {\cal E}(S^{[j]})=(\bar S_j,0).
 \tag{3.4}
\]

For \(D\ge1,p\ge0,v\ge0\), put

\[
 \mu_{D,p}(v)
 =\sum_{r=0}^p\binom pr v^{r/2}2^{r/2}
   \frac{\Gamma((D+r)/2)}{\Gamma(D/2)}.
 \tag{3.5}
\]

Consider one call

\[
 N(h)=\mathbb E_{Y\sim N(0,\Sigma(h))}\psi(h,Y),
 \tag{3.6}
\]

where \(\Sigma(h)\) is positive semidefinite but may change rank.  Fourier
differentiation of the Gaussian characteristic function gives

\[
 N'(h)=\mathbb E\left[\partial_h\psi
 +\frac12\Sigma'(h):D_Y^2\psi\right].
 \tag{3.7}
\]

For completeness, (3.7) does not require an inverse.  Here is a
singular-valid approximation argument with all domination made explicit.
Put

\[
 v=\sup_{|h|\le1}\sum_{a,b}|\Sigma_{ab}(h)|
\]

and \(\Sigma_\epsilon(h)=\Sigma(h)+\epsilon I\).  For
\(\epsilon>0\), differentiation of the nondegenerate Gaussian density
and two integrations by parts give

\[
 N_\epsilon'(h)=\mathbb E\left[\partial_h\psi(h,Y_{\epsilon,h})
 +\frac12\Sigma'(h):D_Y^2\psi(h,Y_{\epsilon,h})\right],
 \qquad Y_{\epsilon,h}\sim N(0,\Sigma_\epsilon(h)).       \tag{3.7a}
\]

All boundary terms vanish because every mixed derivative used below has a
common polynomial envelope.  Couple
\(Y_{\epsilon,h}=\Sigma_\epsilon(h)^{1/2}G\) and
\(Y_h=\Sigma(h)^{1/2}G\).  The positive-semidefinite square-root
inequality gives

\[
 \|\Sigma_\epsilon(h)^{1/2}-\Sigma(h)^{1/2}\|_{\rm op}
 \le\sqrt\epsilon,                                      \tag{3.7b}
\]

uniformly in \(h\).  Moreover, for \(0<\epsilon\le1\),
\(\|Y_{\epsilon,h}\|\le\sqrt{v+1}\,\|G\|\).  Hence for every
integer \(p\),

\[
 \lim_{R\to\infty}
 \mathbb E\!\left[(1+\sqrt{v+1}\,\|G\|)^p
 \mathbf1_{\{\|G\|>R\}}\right]=0.                       \tag{3.7c}
\]

On \(\{\|G\|\le R\}\), (3.7b) gives
\(\sup_h\|Y_{\epsilon,h}-Y_h\|\le\sqrt\epsilon R\), while both
arguments lie in the fixed ball of radius \(\sqrt{v+1}R\).  Uniform
continuity of each relevant mixed derivative of \(\psi\) therefore gives
uniform-in-\(h\) convergence on this event.  On its complement, the common
polynomial envelope is bounded by the integrand in (3.7c), uniformly in
\(h,\epsilon\).  First letting \(\epsilon\downarrow0\) and then
\(R\to\infty\) proves uniform convergence of both \(N_\epsilon\to N\)
and the right side of (3.7a) on \([-1,1]\).  Integrating (3.7a) between
two values of \(h\) and passing to the limit proves (3.7), also when
\(\Sigma(h)\) is singular.  Repeating the same two-region argument for
each derived integrand in (3.11) is legitimate because (3.1)--(3.4) give
the same common polynomial envelope for every mixed derivative used.

In particular, the uniform moment bound

\[
 \sup_{|h|\le1}\mathbb E(1+\|Y_h\|)^p
 \le\mu_{D,p}\left(
   \sup_{|h|\le1}\sum_{a,b}|\Sigma_{ab}(h)|\right)
 \tag{3.8}
\]

supplies all domination required in this iteration.

Here is the numerical constructor.  Given

\[
 \bar c_j\ge\sup_{|h|\le1}
 \sum_{a,b}|\Sigma^{(j)}_{ab}(h)|,\qquad0\le j\le5,
 \tag{3.9}
\]

let \({\cal I}_{D,s}=\{1,\ldots,D\}^s\) and set

\[
 P^{(0)}_{j,s}
 =\bigoplus_{\mathbf i\in{\cal I}_{D,s}}
 {\cal E}(\partial_h^j\partial_{Y_{\mathbf i}}\psi),
 \qquad j+\lceil s/2\rceil\le5.
 \tag{3.10}
\]

When \(q+j+\lceil s/2\rceil<5\), recurse by

\[
 P^{(q+1)}_{j,s}=P^{(q)}_{j+1,s}
 \oplus\bigoplus_{a=0}^j
 \left[
  \left(\tfrac12\binom ja\bar c_{a+1},0\right)
  \odot P^{(q)}_{j-a,s+2}
 \right].
 \tag{3.11}
\]

If \(P^{(q)}_{0,0}=(C_q,p_q)\), define

\[
 \overline{\cal J}_q(N)=C_q\mu_{D,p_q}(\bar c_0).
 \tag{3.12}
\]

Repeated Leibniz expansion of (3.7) proves directly

\[
 |N^{(q)}(h)|\le\overline{\cal J}_q(N),
 \qquad |h|\le1,\quad0\le q\le5.
 \tag{3.13}
\]

For a new covariance, (3.9) is the sum of the already compiled entry
bounds.  A response is compiled by applying (3.10)--(3.12) to its
spatially differentiated integrand.  Finally,

\[
 \overline{(S+hQ)}_j
 =\bar S_j+\bar Q_j+j\bar Q_{j-1},\qquad \bar Q_{-1}=0.
 \tag{3.14}
\]

Apply (3.10)--(3.14), in the exact order of Section 2, to every Gram,
response, full coefficient, and terminal output.  The hypotheses needed
for each Price call follow inductively.  The first covariance block is
constant, positive semidefinite, and \(C^\infty\).  Suppose the first
\(m\) calls have produced \(C^5\) scalar nodes with the displayed
envelopes.  The covariance of call \(m+1\) is a direct sum of constant
blocks and Gram matrices of fields produced in those calls.  It is
therefore positive semidefinite for every \(h\in[-1,1]\); its entries are
\(C^5\), and (3.9) bounds all five derivatives.  The local integrand and
all mixed derivatives required in (3.10) have the polynomial envelopes
generated by (3.1)--(3.4).  The regularization proof of (3.7), iterated at most
five times under those same envelopes, therefore makes every node returned
by call \(m+1\) \(C^5\).  Its newly formed Gram is again positive
semidefinite by its definition as an expectation of outer products.  This
closes the induction without assuming positive definiteness or a
covariance inverse.

The algorithm is finite: there are \(3L-2\) calls, dimension at most
five, and only indices satisfying
\(q+j+\lceil s/2\rceil\le5\).  Hence \(j+s\le10\).  A response starts
with an activation derivative of order at most two, so no derivative above
\(\phi^{(12)}\) occurs.  In particular every node is \(C^5\) on
\([-1,1]\), including at the coalesced covariance \(h=0\).

## 4. Exact Price jets and the activation-integral coefficient

The exact counterpart of (3.10)--(3.12) is also recursive.  In a call
(3.6), set

\[
 {\cal P}_\Sigma=\partial_h+\frac12\Sigma'(h):D_Y^2,
 \qquad \Psi_0=\psi,\qquad
 \Psi_{r+1}={\cal P}_\Sigma\Psi_r,
 \tag{4.1}
\]

where \(\partial_h\) acts on every covariance-derivative and earlier-node
token.  Earlier tokens obey

\[
 \partial_hS^{[j]}=S^{[j+1]},\qquad
 S^{[j]}|_{h=0}={\cal J}_j(S).
 \tag{4.2}
\]

Define, in the order of Section 2,

\[
 {\cal J}_r(N)=
 \mathbb E_{Y\sim N(0,\Sigma(0))}\Psi_r(0,Y),
 \qquad0\le r\le5.
 \tag{4.3}
\]

This is an acyclic definition by Gaussian integration, not a derivative
of an unknown output.  The already-proved singular Price identity gives,
only afterwards,

\[
 {\cal J}_r(N)=N^{(r)}(0).
 \tag{4.4}
\]

At \(h=0\), use independent standard Gaussians

\[
 A,G_1,\ldots,G_L,B_1,\ldots,B_{L-1}
 \tag{4.5}
\]

and the signed coalesced realization

\[
 \xi_{\ell,0}=\xi_{\ell,1}=\xi_{\ell,2}=G_\ell,
 \qquad
 \chi_{\ell,0}=\chi_{\ell,1}
 =d^{(L-\ell+1)/2}B_{\ell-1}.
 \tag{4.6}
\]

Thus every value in (4.3) is an explicit finite Gaussian integral of
\(\phi,\ldots,\phi^{(12)}\).  If a literal list of one-dimensional
integrals is desired, expand the finite expression and replace each factor
belonging to one \(G_j\) by

\[
 I_{a,\alpha}(\phi)
 :=\mathbb E\left[G^a
   \prod_{r=0}^{12}\phi^{(r)}(G)^{\alpha_r}\right],
 \tag{4.7}
\]

and each monomial in \(A,B_j\) by its elementary Gaussian moment.  The
expansion has finitely many terms because (4.1) is applied only three times
in each of finitely many calls.  Equation (4.7), together with
(2.1) and (4.1)--(4.3), is therefore a terminating activation-integral
formula.

Define

\[
 \boxed{
 \kappa_{\phi,L}
 =\frac{{\cal J}_3({\cal O}_{2,L})
           -8{\cal J}_3({\cal O}_{1,L})}{6}.}
 \tag{4.8}
\]

Notice the order: (4.8) first defines a number through the nodewise
Gaussian recursion, and (4.4) then proves

\[
 6\kappa_{\phi,L}=F_{2,L}^{(3)}(0)-8F_{1,L}^{(3)}(0).
 \tag{4.9}
\]

No initialization derivative obtained in the opposite order of limits is
used.

## 5. Parity and the linear jet

In every call make the signed change

\[
 h\mapsto-h,\qquad A\mapsto-A,\qquad
 \chi_{\ell,s}\mapsto-\chi_{\ell,s}\quad(2\le\ell\le L),
 \tag{5.1}
\]

leaving all forward sources fixed.  Induction through (1.8)--(1.13)
shows that all \(Z,X,Q,K\) are unchanged, while
\(A_s,D,H,\rho,R,\sigma,T\) change sign.  The primitive Gaussian laws
are invariant, so

\[
 F_{1,L}(-h)=-F_{1,L}(h),\qquad
 F_{2,L}(-h)=-F_{2,L}(h).
 \tag{5.2}
\]

The order-one evaluation can also be done inside the same compiler.
Put

\[
 \Theta_0=1,\qquad \Theta_j=1+d\Theta_{j-1}
 =\sum_{r=0}^j d^r.
 \tag{5.3}
\]

For \(L=1\), direct differentiation of the scalar recursion (2.2) gives
\({\cal J}_1({\cal O}_{1,1})=1+d=\Theta_1\) and
\({\cal J}_1({\cal O}_{2,1})=2(1+d)\).  Now let \(L\ge2\).
At the coalesced source, direct differentiation of the first bottom call
gives \((R^2_{10})'(0)=\Theta_1\).  If
\((R^\ell_{10})'(0)=\Theta_{\ell-1}\), differentiating the next
forward call gives a learned term \(1\) and a response term
\(d\Theta_{\ell-1}\), hence
\((R^{\ell+1}_{10})'(0)=\Theta_\ell\).  At the top call this gives

\[
 {\cal J}_1({\cal O}_{1,L})=1+d\Theta_{L-1}=\Theta_L.
 \tag{5.4}
\]

This induction is a differentiation of the already-constructed Price
nodes.  The second-bottom and terminal-forward calls have two identical
time-zero contributions at \(h=0\).  Induction upward therefore gives
\(\dot X_{\ell,2}=2\dot X_{\ell,1}\), and at the terminal call

\[
 {\cal J}_1({\cal O}_{2,L})=2\Theta_L.
 \tag{5.5}
\]

Consequently, for

\[
 \Delta_L(\eta)=F_{2,L}(\eta)-F_{1,L}(2\eta),
 \tag{5.6}
\]

the linear coefficient vanishes.  Equations (5.2), (4.8), and (4.9)
give

\[
 \Delta_L^{(j)}(0)=0\quad(j=0,1,2,4),
 \qquad \Delta_L^{(3)}(0)=6\kappa_{\phi,L}.
 \tag{5.7}
\]

## 6. A depth-uniform activation base and an explicit depth factor

This section turns the exact compiler into a deliberately coarse closed
depth estimate.  It uses no output-derived supremum.

First define the universal integers

\[
 c_0=128,\qquad c_{r+1}=8(c_r+1)^2\quad(0\le r<20),
 \tag{6.1}
\]

\[
 C_*=c_{20},\qquad q_*=2C_*.
 \tag{6.2}
\]

The reason for these numbers is recorded in the following finite syntax
lemma.

**Lemma 6.1 (one-call majorant).**  Suppose every incoming scalar token,
every derivative of such a token through order five, and every covariance
entry derivative through order five is at most \(S\ge2\).  For any one of
the seven depth-\(L\) call types in Section 2, or the \(L=1\) scalar call,
every number returned by
(3.10)--(3.14) is at most

\[
 A_* S^{q_*},\qquad
 A_*=2^{C_*}M_\phi^{C_*}\mu_{5,C_*}(25C_*^2).
 \tag{6.3}
\]

*Proof.*  Give a leaf size one, a unary activation node size one plus its
child size, and a sum or product size one plus the sizes of its children.
Expanding the local definitions (but retaining earlier scalar nodes as
tokens) gives the following upper bounds for the largest returned
integrand before the one derivative defining a response:

\[
\begin{array}{c|cccccccc}
\text{call type}
 &\text{bottom 1}&\text{interior 1}&\text{top 1}
 &\text{backward 1}&\text{bottom 2}&\text{interior 2}
 &\text{top 2}&L=1\\ \hline
\text{syntax size}&19&19&33&57&81&81&47&47 .
\end{array}
\tag{6.3a}
\]

The maximizing returned integrands in these eight columns are,
respectively,

\[
 Q^1_{11},\quad Q^\ell_{11},\quad K^L_{11},\quad
 K^\ell_{11},\quad Q^1_{22},\quad Q^\ell_{22},\quad
 {\cal O}_{2,L},\quad {\cal O}_{2,1}.                    \tag{6.3b}
\]

For example, the worst second-bottom chain has successive size bounds
\(1,4,8,9,18,28,39,40\) for
\(Z_{10},D_{10},Z_{11},X_{11},H_{11},D_{11},Z_{12},X_{12}\);
the largest Gram integrand has size \(1+40+40=81\).
The worst terminal-interior chain is bounded by
\(1,4,8,9,18,28,39,40\), and its largest Gram integrand has size
\(81\).  The remaining six columns follow by deleting nodes from one of
these two chains, except the scalar \(L=1\) recursion, whose direct
two-step expansion has size \(47\).  Hence \(c_0=128\) is a verified
uniform starting value.

We now include the two multiplicities that must be counted in addition to
these base trees.  Expand every positive integer coefficient as repeated
unit sums and every covariance contraction over its coordinate pairs;
binarize all sums and products.  If \(|e|\) is the resulting tree size
and \(|\partial e|\) is the size after one fully expanded formal
derivative, then

\[
 |\partial e|\le2|e|^2.                                  \tag{6.3c$_0$}
\]

Indeed this holds for a leaf.  Assuming it for the children, the tree-size
recurrences for a sum, product, and unary activation composition are

\[
\begin{aligned}
 |\partial(u+v)|&=1+|\partial u|+|\partial v|,\\
 |\partial(uv)|&=3+|\partial u|+|\partial v|+|u|+|v|,\\
 |\partial(\phi^{(k)}(u))|&=2+|u|+|\partial u|.
\end{aligned}                                             \tag{6.3c$_1$}
\]

Substitution of the inductive bounds shows that each right side is at
most twice the square of, respectively,
\(1+|u|+|v|\), \(1+|u|+|v|\), and \(1+|u|\).  This proves
(6.3c\(_0\)) by structural induction.  Consequently, if tree size,
incoming-token degree, and polynomial-envelope exponent are at most
\(c_r\), all three quantities after one formal differentiation are bounded
by

\[
 2c_r^2\le1+2c_r(c_r+1)<8(c_r+1)^2=c_{r+1}.              \tag{6.3c}
\]

A response costs one such derivative.  Each individual term in (3.10)
then costs at most \(j+s\le10\) further derivative levels.  If \(s>0\)
and \(r\le11\) derivative levels have been used, then \(r\ge s\) and
the recursion (6.1) gives \(c_r\ge5^r\ge5^s\).  The direct sum over the
at most \(D^s\le5^s\) ordered spatial multiindices consequently has size
at most

\[
 1+5^s(c_r+1)
 \le1+c_r(c_r+1)
 \le c_{r+1}.                                             \tag{6.3d}
\]

For \(s=0\) there is only one term.  Padding smaller bounds by
monotonicity, every base object \(P^{(0)}_{j,s}\) is bounded by \(c_{12}\).

At one Price level there are at most seven outer summands.  Expanding the
contraction over \(D^2\le25\) coordinate pairs and every binomial
multiplicity gives at most

\[
 1+25\sum_{a=0}^j\binom ja\le801                         \tag{6.3e}
\]

summands.  If each input is bounded by \(c\ge c_{12}\), their total size,
token degree, and envelope exponent are bounded by

\[
 801(2c+2)\le8(c+1)^2.                                   \tag{6.3f}
\]

Thus each of the five Price levels in (3.11) costs one \(c\)-level.
Rule (3.14), including its integer \(j\le5\), costs one further level.
The complete worst-case ledger is

\[
 1\ \text{response derivative}
 +10\ \text{mixed derivatives}
 +1\ \text{multiindex aggregation}
 +5\ \text{Price levels}
 +1\ \text{full-coefficient assembly}
 =18<20.                                                  \tag{6.3g}
\]

The two remaining levels absorb covariance-block and direct-sum
bookkeeping.  Hence \(C_*=c_{20}\) bounds every expanded tree size,
incoming-token degree, and polynomial-envelope exponent.  This proves
termination as well as the claimed complexity bound.

The entrywise covariance norm is at most \(25S\).  Since all
multiplicities have been expanded, a tree with at most \(C_*\) nodes is
consequently bounded by

\[
 2^{C_*}M_\phi^{C_*}S^{C_*}(1+\|Y\|)^{C_*}.
\]

For \(S\ge1\), (3.5) gives

\[
 \mu_{D,C_*}(25S)
 \le S^{C_*/2}\mu_{5,C_*}(25)
 \le S^{C_*}\mu_{5,C_*}(25C_*^2),
\]

for every \(D\le5\).  The covariance-derivative factors, their binomial
coefficients, and (3.14) were counted explicitly in (6.3e)--(6.3g).
Hence the result is at most
\(A_*S^{2C_*}=A_*S^{q_*}\).  \(\square\)

To include a completely explicit lower rank scale, put

\[
 u=\mathbb E\phi'(G)^4,\qquad
 \ell_0=\mathbb E[\phi(G)^2\phi'(G)^2],\qquad
 s=\mathbb E\phi''(G)^2,
 \tag{6.4}
\]

\[
 \widehat s=\begin{cases}s,&s>0,\\1,&s=0,\end{cases}
 \qquad
 \lambda_\phi=\min\{1,d,u,\ell_0,\widehat s\}>0.
 \tag{6.5}
\]

Strict positivity follows from \(d>0\), continuity, and full support of
Gaussian measure.  If \(s=0\), then \(\phi\) is nonconstant affine.

Define the depth-uniform activation constants

\[
 \boxed{
 B_\phi=\max\left\{32,M_\phi^2,\lambda_\phi^{-1},A_*\right\},
 \qquad h_\phi=B_\phi^{-1}.}
 \tag{6.6}
\]

Finally set

\[
 e_L=(2L+1)q_*^{3L},
 \qquad
 \boxed{E_L=2e_L+2L+1.}
 \tag{6.7}
\]

Both \(B_\phi,h_\phi\) are independent of depth; all depth dependence is
in the explicit integer \(E_L\).

We now verify the bounds.  The initial variances in (1.14) are at most
\(M_\phi^{2L}\le B_\phi^{2L}\).  Starting with
\(S_0=B_\phi^{2L}\), Lemma 6.1 permits the recursion

\[
 S_{m+1}=B_\phi S_m^{q_*}.
 \tag{6.8}
\]

Writing \(S_m=B_\phi^{a_m}\), one has

\[
 a_0=2L,\qquad a_{m+1}=1+q_*a_m,
\]

so, for \(m\le3L-2\),

\[
 a_m=q_*^m(2L)+\frac{q_*^m-1}{q_*-1}
 \le(2L+1)q_*^{3L}=e_L.
 \tag{6.9}
\]

Thus every derivative bar returned by the compiler is at most
\(B_\phi^{e_L}\), in particular

\[
 \overline{\cal J}_5(F_{1,L}),
 \overline{\cal J}_5(F_{2,L})\le B_\phi^{e_L}.
 \tag{6.10}
\]

The determinant fourth-derivative bound for any required two-time Gram is
a sum of one diagonal term and five Leibniz products.  Since the sum of
the binomial coefficients is \(16\), the all-node bound proved in
(6.9), (1.14), and
\(B_\phi\ge32\) imply the common bound

\[
 D_{G,L}\le B_\phi^{3e_L}.
 \tag{6.11}
\]

The rank-tangent induction gives, for every one of the \(2(L-1)\)
nonterminal two-time Grams,

\[
 a_{G,L}:=\lim_{h\to0}\frac{\det G(h)}{h^2}
 \ge\lambda_\phi^{4L}\ge B_\phi^{-4L}.
 \tag{6.12}
\]

For reference, the two ingredients behind (6.12) are: forward tangent
variances satisfy \(V_1=d^{L-1}u\),
\(V_j\ge dV_{j-1}\), hence \(V_j\ge\lambda_\phi^{2L}\)
at every required feature Gram.  For \(L\ge2\), at the top the sharper
same recursion gives

\[
 V_{L-1}\ge d^{2L-3}u\ge\lambda_\phi^{2L-2}.             \tag{6.12a}
\]

If \(s>0\), the fresh orthogonal component in \(\beta_L\) therefore gives
\(\beta_L\ge V_{L-1}s\ge\lambda_\phi^{2L-1}\); if \(s=0\), then
\(\phi\) is affine and \(\beta_L=d\ge\lambda_\phi^{2L-1}\).  The
reverse tangent variances then satisfy
\(\beta_j\ge d\beta_{j+1}\), hence
\(\beta_j\ge\lambda_\phi^{3L}\) at every required cotangent Gram.
Multiplication by the time-zero
cotangent variance \(d^{L-j+1}\) gives (6.12).  The rank note proves
these inequalities from the fresh orthogonal Gaussian components, rather
than by dropping possibly signed cross terms.

Parity makes every determinant even.  Taylor's formula and (6.11) give

\[
 \det G(h)\ge\frac12a_{G,L}h^2>0
 \tag{6.13}
\]

whenever

\[
 0<|h|\le
 \sqrt{\frac{12a_{G,L}}{1+D_{G,L}}}.
 \tag{6.14}
\]

Indeed,

\[
\sqrt{\frac{12B_\phi^{-4L}}{1+B_\phi^{3e_L}}}
\ge \sqrt6\,B_\phi^{-2L-\frac32e_L}
\ge B_\phi^{-(2L+2e_L)} ,
\tag{6.14a}
\]

where \(B_\phi\ge32\) and \(e_L\ge1\).  Thus the right side of
(6.14) is at least \(B_\phi^{-(2L+2e_L)}\).  Since

\[
 h_\phi^{E_L}
 =B_\phi^{-(2e_L+2L+1)}
 \le\min\left\{\frac12,
 B_\phi^{-(2L+2e_L)}\right\},
 \tag{6.15}
\]

all Grams required by the fixed-\(h\) width identification are positive
definite throughout the punctured claimed interval.

Finally define the exact envelope remainder constant

\[
 \mathfrak B_{\phi,L}
 =\frac{\overline{\cal J}_5(F_{2,L})
       +2^5\overline{\cal J}_5(F_{1,L})}{120}.
 \tag{6.16}
\]

Because \(33/120<1\), (6.10) gives

\[
 \mathfrak B_{\phi,L}\le B_\phi^{e_L}\le B_\phi^{E_L}.
 \tag{6.17}
\]

For \(|\eta|\le h_\phi^{E_L}\), also \(|2\eta|\le1\).  Equations
(3.13), (5.7), and Taylor's integral remainder therefore prove

\[
 \boxed{
 \left|F_{2,L}(\eta)-F_{1,L}(2\eta)
       -\kappa_{\phi,L}\eta^3\right|
 \le B_\phi^{E_L}|\eta|^5,
 \qquad |\eta|\le h_\phi^{E_L}.}
 \tag{6.18}
\]

In particular, for every \(\varepsilon>0\),

\[
 |F_{2,L}(\eta)-F_{1,L}(2\eta)|
 \le(|\kappa_{\phi,L}|+\varepsilon)|\eta|^3
 \tag{6.19}
\]

whenever

\[
 |\eta|\le
 \min\left\{h_\phi^{E_L},
 \sqrt{\frac{\varepsilon}{1+B_\phi^{E_L}}}\right\}.
 \tag{6.20}
\]

Every constant in (6.18)--(6.20) is either activation data or the explicit
depth integer (6.7).  No supremum of a limiting output, no trained
trajectory, and no unspecified continuity modulus appears.

## 7. The constant-activation case

If \(d=0\), continuity and Gaussian full support give \(\phi'\equiv0\).
Normalization gives \(\phi\equiv\pm1\).  Every hidden feature is fixed,
only the top weights move, and \(F_{k,L}(h)=kh\).  Hence

\[
 F_{2,L}(\eta)-F_{1,L}(2\eta)=0.
\]

One may take \(\kappa_{\phi,L}=0\), \(B_\phi=1\), \(h_\phi=1/2\),
and any positive \(E_L\).
