# Four fine steps versus two coarse steps at arbitrary depth

## Theorem

Fix an integer hidden depth \(L\ge1\).  For common hidden width \(n\),
scalar input \(1\), and no biases, let

\[
 Z_1^s=u^s,\qquad X_1^s=\phi(Z_1^s),                    \tag{0.1}
\]

\[
 Z_\ell^s=\frac{W_\ell^sX_{\ell-1}^s}{\sqrt n},\qquad
 X_\ell^s=\phi(Z_\ell^s),\quad2\le\ell\le L,            \tag{0.2}
\]

\[
 f_{n,L}^s=\frac1n(a^s)^TX_L^s.                         \tag{0.3}
\]

All entries of \(u^0,a^0,W_2^0,\ldots,W_L^0\) are mutually independent
standard Gaussians.  With recomputed cotangents \(C_\ell^s\), one ascent
step of size \(h\) is

\[
 a^{s+1}=a^s+hX_L^s,\qquad
 W_\ell^{s+1}=W_\ell^s+\frac h{\sqrt n}
 C_\ell^s(X_{\ell-1}^s)^T,\qquad
 u^{s+1}=u^s+hC_1^s.                                    \tag{0.4}
\]

Assume, for \(G\sim N(0,1)\),

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,                                 \tag{0.5}
\]

\[
 M_\phi=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty.
 \tag{0.6}
\]

At every fixed nonzero \(h\) with

\[
 |h|\le \frac1{8\sqrt{\mathcal S_{4,L}}}
 =2h_{\phi,42}(L),
\]

the
limits

\[
 F_{k,L}(h)=\lim_{n\to\infty}\mathbb E f_{n,L}^k(h),
 \qquad k=2,4,                                           \tag{0.7}
\]

exist.  The width limit in (0.7) is taken before any limit in \(h\).

The following finite recursions define the constants.  Put

\[
 b_{4,0}=16,\qquad
 b_{4,t+1}=64\cdot6^2(b_{4,t}+1)^2,\quad0\le t<4,      \tag{0.8}
\]

\[
 D_4=9,\qquad s_4=8(b_{4,4}+1),                        \tag{0.9}
\]

\[
 A_4^{\rm op}=64(1+9^{10}+32\cdot9^2),                 \tag{0.10}
\]

\[
 c_{4,0}=\max\{128,s_4\},\qquad
 c_{4,r+1}=A_4^{\rm op}(c_{4,r}+1)^2,\quad0\le r<24, \tag{0.11}
\]

\[
 C_4=c_{4,24},\qquad q_4=2C_4,                          \tag{0.12}
\]

\[
 \mu_{D,p}(v)=\sum_{r=0}^p{p\choose r}v^{r/2}2^{r/2}
 \frac{\Gamma((D+r)/2)}{\Gamma(D/2)},                  \tag{0.13}
\]

\[
 g_4=2^{C_4}\mu_{9,C_4}(81C_4^2),\qquad
 b_\phi=\max\{2,M_\phi\}.                             \tag{0.14}
\]

Finally let

\[
 N_{4,L}=7L-6,\qquad
 A_{4,L}=\frac{q_4^{N_{4,L}}-1}{q_4-1},                 \tag{0.15}
\]

\[
 E_{4,L}=2Lq_4^{N_{4,L}}+C_4A_{4,L},                    \tag{0.16}
\]

\[
 \mathcal S_{4,L}=g_4^{A_{4,L}}b_\phi^{E_{4,L}},        \tag{0.17}
\]

so the dependence can also be written with one absolute activation base:

\[
 \widehat b_\phi=\max\{g_4,b_\phi\},\qquad
 \mathcal S_{4,L}\le
 \widehat b_\phi^{D_{4,L}},\qquad
 D_{4,L}=A_{4,L}+E_{4,L}.                               \tag{0.17a}
\]

Thus all depth dependence is in the displayed integer \(D_{4,L}\); the
base \(\widehat b_\phi\) is independent of depth.

A slightly coarser form using only this one base is

\[
 B_{\phi,42}^*(L)=\widehat b_\phi^{D_{4,L}},\qquad
 h_{\phi,42}^*(L)=\widehat b_\phi^{-(D_{4,L}+4)}.        \tag{0.17b}
\]

Because \(\widehat b_\phi\ge2\), (0.17b) has
\(B_{\phi,42}^*(L)\ge\mathcal S_{4,L}\) and
\(h_{\phi,42}^*(L)\le1/(16\sqrt{\mathcal S_{4,L}})\).
Thus (0.20)--(0.22) remain true if the exact pair in (0.18) is replaced by
the coarser pair (0.17b).  This is the requested depth-uniform-base form.

and define

\[
 \boxed{
 B_{\phi,42}(L)=\mathcal S_{4,L},\qquad
 h_{\phi,42}(L)=\frac1{16\sqrt{\mathcal S_{4,L}}}.}    \tag{0.18}
\]

The cubic coefficient is also explicit.  Apply the exact signed Price
ledger (2.10a)--(2.10g) of `COMPILER_AND_CONSTANTS.md`—equivalently the
finite nodewise recursion (3.1)--(3.5) below—to the inverse-free Gaussian DAG
(1.4)--(1.12), and denote its third-jet outputs by
\({\cal J}_3(F_{4,L})\) and \({\cal J}_3(F_{2,L})\).  Set

\[
 \boxed{
 \kappa_{42,\phi,L}
 =\frac{{\cal J}_3(F_{4,L})-8{\cal J}_3(F_{2,L})}{6}.}  \tag{0.19}
\]

This is a terminating expression in Gaussian activation integrals, not a
definition through a derivative of an unknown output.

Then, for every \(|\eta|\le h_{\phi,42}(L)\),

\[
 \boxed{
 \left|F_{4,L}(\eta)-F_{2,L}(2\eta)
 -\kappa_{42,\phi,L}\eta^3\right|
 \le B_{\phi,42}(L)|\eta|^5.}                           \tag{0.20}
\]

Consequently, for every \(\varepsilon>0\),

\[
 |F_{4,L}(\eta)-F_{2,L}(2\eta)|
 \le(|\kappa_{42,\phi,L}|+\varepsilon)|\eta|^3        \tag{0.21}
\]

whenever

\[
 |\eta|\le
 \min\left\{h_{\phi,42}(L),
 \sqrt{\frac{\varepsilon}{1+B_{\phi,42}(L)}}\right\}. \tag{0.22}
\]

For \(L=3\), the explicit depth factors simplify to

\[
 N_{4,3}=15,\qquad
 A_{4,3}=\frac{q_4^{15}-1}{q_4-1},\qquad
 E_{4,3}=6q_4^{15}+C_4A_{4,3}.                          \tag{0.23}
\]

If \(\phi\equiv\pm1\), take
\(\kappa_{42,\phi,L}=0\), \(B_{\phi,42}(L)=1\), and
\(h_{\phi,42}(L)=1/2\); the discrepancy is exactly zero.

## 1. Exact finite-width identities and the population DAG

Let

\[
 C_L^s=a^s\odot\phi'(Z_L^s),\qquad
 B_{\ell-1}^s=\frac{(W_\ell^s)^TC_\ell^s}{\sqrt n},
 \qquad C_{\ell-1}^s=B_{\ell-1}^s\odot\phi'(Z_{\ell-1}^s).
 \tag{1.1}
\]

Writing only the initialization-matrix actions as

\[
 Y_\ell^s=\frac{W_\ell^0X_{\ell-1}^s}{\sqrt n},\qquad
 R_{\ell-1}^s=\frac{(W_\ell^0)^TC_\ell^s}{\sqrt n},     \tag{1.2}
\]

the exact accumulated updates are

\[
 Z_\ell^s=Y_\ell^s+h\sum_{r<s}Q_{\ell-1,rs}^{(n)}C_\ell^r,
 \qquad
 B_{\ell-1}^s=R_{\ell-1}^s
 +h\sum_{r<s}K_{\ell,rs}^{(n)}X_{\ell-1}^r.            \tag{1.3}
\]

The time-four chronology is four forward/backward sweeps followed by the
terminal forward sweep.  It has exactly \(9(L-1)\) adaptive actions and
inverts at most \(Q_{\ell-1}^{[3]}\) and \(K_\ell^{[3]}\).

For each connector introduce forward Gaussian sources
\(\xi_{\ell,0:4}\) and transpose sources \(\chi_{\ell,0:3}\), with

\[
 \mathbb E\xi_{\ell,r}\xi_{\ell,s}
 =Q_{\ell-1,rs}=\mathbb E[X_{\ell-1}^rX_{\ell-1}^s],    \tag{1.4}
\]

\[
 \mathbb E\chi_{\ell,r}\chi_{\ell,s}
 =K_{\ell,rs}=\mathbb E[C_\ell^rC_\ell^s].             \tag{1.5}
\]

With independent \(U,A\sim N(0,1)\), construct chronologically

\[
 Z_1^0=U,\qquad X_1^s=\phi(Z_1^s),                      \tag{1.6}
\]

\[
 \rho_{\ell,sr}=\mathbb E[\partial_{\chi_{\ell,r}}X_{\ell-1}^s],
 \qquad
 Z_\ell^s=\xi_{\ell,s}
 +\sum_{r<s}(\rho_{\ell,sr}+hQ_{\ell-1,rs})C_\ell^r,  \tag{1.7}
\]

\[
 X_\ell^s=\phi(Z_\ell^s),\qquad
 a^s=A+h\sum_{r<s}X_L^r,
 \qquad C_L^s=a^s\phi'(Z_L^s),                          \tag{1.8}
\]

\[
 \sigma_{\ell,sr}=\mathbb E[\partial_{\xi_{\ell,r}}C_\ell^s],
 \tag{1.9}
\]

\[
 B_{\ell-1}^s=\chi_{\ell,s}
 +\sum_{r\le s}\sigma_{\ell,sr}X_{\ell-1}^r
 +h\sum_{r<s}K_{\ell,rs}X_{\ell-1}^r,                 \tag{1.10}
\]

\[
 C_{\ell-1}^s=B_{\ell-1}^s\phi'(Z_{\ell-1}^s),
 \qquad Z_1^{s+1}=Z_1^s+hC_1^s.                        \tag{1.11}
\]

At terminal time \(k\),

\[
 F_{k,L}(h)=\mathbb E\left[
 \left(A+h\sum_{r<k}X_L^r\right)X_L^k\right].          \tag{1.12}
\]

This DAG contains no covariance inverse and is defined even when all
time covariances coalesce at \(h=0\).

## 2. Width-first identification at each fixed step

For a reused standard Gaussian matrix with old row and column queries
\(H,C\), exact adaptive Gaussian conditioning gives

\[
 M=P_CM+MP_H-P_CMP_H+P_C^\perp\widetilde MP_H^\perp.   \tag{2.1}
\]

The fresh residual remains independent across all interlaced connectors.
The exact row and transpose regressions involve the old feature and
cotangent Grams and the rectangular cross block

\[
 {\cal R}=C^T(MH/\sqrt n)/n=(M^TC/\sqrt n)^TH/n.        \tag{2.2}
\]

At population level, write the old raw actions as

\[
 y=\xi+Pc,\qquad d=\chi+Sx.                             \tag{2.3}
\]

Gaussian integration by parts gives

\[
 {\cal R}=SQ+KP^T,\qquad
 \mathbb E[dX_*]=K\rho+Sq,\qquad
 \mathbb E[yC_*]=Q\sigma+Pk.                           \tag{2.4}
\]

Substituting (2.4) in the exact regressions cancels every old-action cross
projection and leaves precisely the \(\rho\)- and \(\sigma\)-terms in
(1.7) and (1.10).

The only ranks required are the time-history Grams stated above.  For every
fixed nonzero

\[
 |h|\le\frac1{8\sqrt{\mathcal S_{4,L}}},                \tag{2.5}
\]

they are positive definite.  The proof is chronological.  A fresh
transpose innovation at the bottom enters \(Z_1^{s+1}\) with coefficient
\(h\phi'(Z_1^s)\), opening the new bottom feature direction.  Fresh
forward innovations then open the feature Grams upward.  If \(\phi'\) is
nonconstant, the fresh top forward innovation opens the new top
cotangent; if \(\phi\) is affine, the new \(hX_L^s\) term in \(a^{s+1}\)
does so.  Fresh transpose innovations open all remaining cotangent Grams
downward.  The only quantitative nonvanishing needed in the non-affine top
case is

\[
 \|a^s-A\|_2\le4|h|\sqrt{\mathcal S_{4,L}}\le\frac12.   \tag{2.6}
\]

Condition on the global filtration and couple all residuals to one
compatible iid ideal coordinate array.  A finite induction over the
\(9(L-1)\) actions proves, simultaneously at every finite moment order,
field convergence, convergence of every Gram/cross block/overlap, and
convergence of every regression coefficient.  The good event includes
both old-Gram eigenvalue bounds and every new-query Schur-complement bound.
Rosenthal's inequality controls ideal coordinate averages, while the
finite-rank Gaussian projection estimate controls the removed old
subspaces.  Running the induction at arbitrary high moment order makes the
bad-event probability \(O(n^{-m})\) for every fixed \(m\).

The raw finite network is bounded by a finite polynomial in the initial
Gaussian vector norms and normalized Gaussian matrix operator norms.
These have moments of every order, so Hölder removes the stopping and gives
uniform integrability of the terminal output.  This proves (0.7) at each
fixed step before any small-step analysis.  Every ledger entry and every
estimate in this paragraph is written explicitly in `WIDTH_AND_RANK.md`.

## 3. Singular regularity and the exact coefficient

For one local Gaussian call

\[
 N(h)=\mathbb E_{Y\sim N(0,\Sigma(h))}\psi(h,Y),         \tag{3.1}
\]

define

\[
 {\cal P}_\Sigma=\partial_h+\frac12\Sigma'(h):D_Y^2,
 \qquad \Psi_0=\psi,\qquad
 \Psi_{r+1}={\cal P}_\Sigma\Psi_r.                      \tag{3.2}
\]

Earlier scalar nodes are tokens \(S^{[j]}\) satisfying
\(\partial_hS^{[j]}=S^{[j+1]}\).  In the chronological order of the
\(7L-6\) local calls, define

\[
 {\cal J}_r(N)=
 \mathbb E_{Y\sim N(0,\Sigma(0))}\Psi_r(0,Y),
 \qquad0\le r\le5.                                      \tag{3.3}
\]

At a singular covariance, apply (3.2) first to
\(\Sigma+\epsilon I\).  Coupling its Gaussian with the singular Gaussian,
truncating on \(\{\|G\|\le R\}\), and controlling the complement by the
polynomial Gaussian envelope proves the Price identity uniformly as
\(\epsilon\downarrow0\).  Iteration proves

\[
 {\cal J}_r(N)=N^{(r)}(0),\qquad0\le r\le5.             \tag{3.4}
\]

Only indices satisfying \(j+\lceil|\alpha|/2\rceil\le5\) occur.  A
response begins with at most \(\phi''\), so \(C^{12}\) is sufficient.
At \(h=0\), every repeated forward source coalesces to one standard
Gaussian and every repeated transpose source to one Gaussian with variance
\(d^{L-\ell+1}\).  Expanding (3.2)--(3.3) therefore reduces (0.19) to a
finite sum of

\[
 \mathbb E\left[G^a\prod_{j=0}^{12}
 \phi^{(j)}(G)^{\alpha_j}\right]                        \tag{3.5}
\]

and elementary Gaussian moments.  This proves the promised explicit
activation-integral description.

The sign change \(h\mapsto-h\), \(A\mapsto-A\), and
\(\chi\mapsto-\chi\) proves that every \(F_{k,L}\) is odd.  Direct
first-order evaluation of (3.2) gives

\[
 F_{k,L}'(0)=k\sum_{j=0}^Ld^j.                           \tag{3.6}
\]

Hence the discrepancy has no terms of degrees \(0,1,2,4\), and (0.19) is
its cubic coefficient.

## 4. Explicit envelope and remainder

The grammar recursion (0.8) bounds every raw local expression through time
four.  A response costs one spatial derivative, mixed derivatives cost at
most ten, multiindex aggregation costs one level, five Price assemblies
cost five, full-coefficient assembly costs one, and covariance/direct-sum
bookkeeping costs two.  The twenty required levels fit inside the twenty-four
iterations in (0.11).

If all incoming scalar and covariance-derivative bars are at most
\(S\ge2\), the resulting expanded tree has at most \(C_4\) nodes, token
degree at most \(C_4\), and envelope exponent at most \(C_4\).  Gaussian
integration using (0.13) gives the one-call bound

\[
 g_4b_\phi^{C_4}S^{q_4}.                                \tag{4.1}
\]

The initial cotangent variances are powers of
\(d\le M_\phi^2\), so the initial bar is at most \(b_\phi^{2L}\).
Solving (4.1) through \(7L-6\) calls gives exactly
\(\mathcal S_{4,L}\) in (0.17).  Thus

\[
 \overline{\cal J}_5(F_{4,L}),
 \overline{\cal J}_5(F_{2,L})\le\mathcal S_{4,L}.       \tag{4.2}
\]

Taylor's integral remainder, (0.19), parity, and (4.2) give

\[
 \begin{aligned}
 &|F_{4,L}(\eta)-F_{2,L}(2\eta)
 -\kappa_{42,\phi,L}\eta^3|\\
 &\quad\le\frac{1+2^5}{120}\mathcal S_{4,L}|\eta|^5
 \le\mathcal S_{4,L}|\eta|^5.                          \tag{4.3}
 \end{aligned}
\]

The choice (0.18) puts both the fine step \(\eta\) and the coarse step
\(2\eta\) inside the fixed-step rank and \(C^5\) intervals.  This proves
(0.20).  Finally,

\[
 B_{\phi,42}(L)|\eta|^2
 \le\frac{B_{\phi,42}(L)}{1+B_{\phi,42}(L)}\varepsilon
 <\varepsilon                                           \tag{4.4}
\]

under (0.22), which proves (0.21).

## 5. Status of the sharper factorization

The direct coefficient (0.19) is unconditional and is sufficient for the
theorem.  A natural stronger identity is

\[
 \kappa_{42,\phi,L}\stackrel{?}=6\kappa_{21,\phi,L}.    \tag{5.1}
\]

The universal gradient-Euler algebra would imply (5.1), and the candidate
activation recursions are recorded in `CUBIC_COEFFICIENT.md`.  However, two
independent hostile audits of `TEMPORAL_CUBIC_LAW.md` found that the marked
adjoint sums do not yet include the full enlarged marked source histories;
equivalently, differentiated response terms such as
\(2\rho'_jc'_j\) have not been generated and paired.  Thus (5.1) is
**open in this study under the demanded proof standard** and is not used
anywhere in (0.20).
