# Width-first time doubling at arbitrary hidden depth

## The theorem

Let \(L,t\ge1\) be integers. All \(L\) hidden layers have width \(n\),
the input is the scalar \(1\), and there are no biases. Let
\(G\sim N(0,1)\), and assume

\[
 \phi\in C^{12}(\mathbb R),\qquad \mathbb E\phi(G)^2=1,
 \tag{T.1}
\]

\[
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
 \tag{T.2}
\]

For the exact network and updates in Section 1, let

\[
 F_{N,n,L}(h)=\mathbb E f_{n,L}^N,
 \qquad
 F_{N,L}(h)=\lim_{n\to\infty}F_{N,n,L}(h)
 \tag{T.3}
\]

where the limit in (T.3) is taken at each fixed \(h\). Define

\[
 D_{t,L}(\eta)=F_{t,L}(2\eta)-F_{2t,L}(\eta).
 \tag{T.4}
\]

The exact Price compiler in Section 3 defines, before any output derivative
is invoked, finite activation-integral numbers

\[
 \mathcal J^{\mathrm{PJ}}_{r,N,L}(\phi),
 \qquad 0\le r\le5.
 \tag{T.5}
\]

It does so by traversing the inverse-free Gaussian DAG in chronological
order and applying the displayed Price recursion (3.1) at each Gaussian
call. Define the unconditional cubic coefficient

\[
 \boxed{
 \kappa_{\phi,L,t}
 =\frac{8\mathcal J^{\mathrm{PJ}}_{3,t,L}(\phi)
 -\mathcal J^{\mathrm{PJ}}_{3,2t,L}(\phi)}6.}
 \tag{T.6}
\]

This is a terminating formula in Gaussian integrals of
\(\phi,\ldots,\phi^{(12)}\), not a definition through an unknown output
derivative.

We next define a deliberately coarse but closed remainder constant.  Put

\[
 B_\phi=\max\{4,M_\phi\}.
 \tag{T.7}
\]

For an integer \(N\ge1\), let \(D_N=2N+2\) and define the numerical
recursions

\[
 R_{N,0}=1,\qquad
 R_{N,k+1}=16(N+2)(R_{N,k}+1),
 \quad0\le k<8(N+1),
 \tag{T.8}
\]

\[
 c_{N,0}=4(R_{N,8(N+1)}+1),
 \tag{T.9}
\]

\[
 c_{N,q+1}=64(D_N+1)^{10}(c_{N,q}+1)^2,
 \quad0\le q<24,
 \qquad C_N=c_{N,24}.
 \tag{T.10}
\]

For

\[
 \mu_{D,p}(w)=
 \sum_{q=0}^p{p\choose q}w^{q/2}2^{q/2}
 \frac{\Gamma((D+q)/2)}{\Gamma(D/2)},
 \tag{T.11}
\]

put

\[
 \nu_N=\mu_{D_N,C_N}((D_N+1)^2),\qquad
 \alpha_N=\left\lceil\log_2(2^{C_N}\nu_N)\right\rceil,
 \tag{T.12}
\]

\[
 p_N=2C_N,\qquad r_N=C_N+\alpha_N,
 \tag{T.13}
\]

\[
 M_{L,N}=\begin{cases}(2N+1)(L-1),&L\ge2,\\1,&L=1,
 \end{cases}
 \tag{T.14}
\]

and

\[
 \boxed{
 E_{L,N}=2L\,p_N^{M_{L,N}}
 +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}.}
 \tag{T.15}
\]

All upper indices in (T.8)--(T.15) are finite. Thus \(E_{L,N}\) is a
computable integer depending only on \((L,N)\), while all activation
dependence is in \(B_\phi\).

Then the actual width-first outputs obey

\[
 \boxed{
 \left|D_{t,L}(\eta)
 -\kappa_{\phi,L,t}\eta^3\right|
 \le B_\phi^{E_{L,2t}}|\eta|^5,
 \qquad |\eta|\le\frac12.}
 \tag{T.16}
\]

Consequently, for every \(\varepsilon>0\),

\[
 |D_{t,L}(\eta)|
 \le\left(|\kappa_{\phi,L,t}|+\varepsilon\right)
       |\eta|^3
 \tag{T.17}
\]

whenever

\[
 |\eta|\le
 \eta_0(\phi,L,t,\varepsilon)
 :=\min\left\{\frac12,
 \sqrt{\frac{\varepsilon}{1+B_\phi^{E_{L,2t}}}}\right\}.
 \tag{T.18}
\]

No quantity above is defined from a supremum of \(F_{N,L}\), a trained
trajectory, a continuity modulus, or a finite-width small-step expansion.

### Compact coefficient

The fixed bounded-operator bridge in Section 4 constructs the common
singular \(C^3\) gradient germ and proves that the exact compiler
coefficient (T.6) reduces to nine activation moments. With

\[
 g=\phi(G),\qquad p=\phi'(G),\qquad q=\phi''(G),
 \qquad r_3=\phi'''(G),
\]

put

\[
\begin{array}{lll}
 d=\mathbb Ep^2,&u=\mathbb Ep^4,&v=\mathbb E[gq],\\
 m=\mathbb E[gp^2q],&r=\mathbb E[pr_3],&s=\mathbb Eq^2,\\
 j=\mathbb E[p^3r_3],&e=\mathbb E[p^2q^2],
 &\ell=\mathbb E[g^2p^2].
\end{array}
 \tag{C.1}
\]

If \(d>0\), define

\[
 \Theta_0=1,
 \qquad \Theta_a=1+d\Theta_{a-1},
 \qquad b_a=d^{L-a},
 \qquad \pi_a=db_a.
 \tag{C.2}
\]

Starting from \(V_0=M_0=T_0=0\), run, for \(a=1,\ldots,L\),

\[
 V_a=dV_{a-1}+\Theta_{a-1}^2b_au,
 \tag{C.3}
\]

\[
 M_a=vV_{a-1}+\Theta_{a-1}^2b_am+(d+v)M_{a-1},
 \tag{C.4}
\]

\[
\begin{aligned}
 T_a={}&3\Theta_{a-1}V_{a-1}r
 +3\Theta_{a-1}^3b_aj
 +3\Theta_{a-1}M_{a-1}(r+s)\\
 &+d(T_{a-1}+3M_{a-1}).
\end{aligned}
 \tag{C.5}
\]

Starting from \((\beta_{L+1},\gamma_{L+1})=(0,1)\), run backwards for
\(a=L,\ldots,1\):

\[
\begin{aligned}
 \beta_a={}&b_aV_{a-1}s+3\Theta_{a-1}^2b_a^2e+d\beta_{a+1}
 +\gamma_{a+1}^2\ell\\
 &+2\Theta_{a-1}\gamma_{a+1}b_am,
\end{aligned}
 \tag{C.6}
\]

\[
 \gamma_a=\pi_a+\Theta_{a-1}b_a(r+s)
 +\gamma_{a+1}(v+d).
 \tag{C.7}
\]

Set

\[
 \mathsf S_{\phi,L}=T_L+3M_L,
 \qquad
 \mathsf H_{\phi,L}=V_L+\beta_1
 +\sum_{a=2}^L(\beta_a+\pi_aV_{a-1}),
 \tag{C.8}
\]

\[
 J_{\phi,L}=\mathsf S_{\phi,L}+4\mathsf H_{\phi,L}.
 \tag{C.9}
\]

If \(d=0\), set these three quantities to zero. The bounded-operator
intertwining theorem and the nodewise contractions in
`CUBIC_DEPTH_TIME.md` prove

\[
 \boxed{
 \kappa_{\phi,L,t}
 =-\frac{t(2t-1)}2J_{\phi,L}.}
 \tag{C.10}
\]

Equations (T.6) and (C.10) are the proved intertwining identity

\[
 \frac{8\mathcal J^{\mathrm{PJ}}_{3,t,L}(\phi)
 -\mathcal J^{\mathrm{PJ}}_{3,2t,L}(\phi)}6
 =-\frac{t(2t-1)}2J_{\phi,L}.
 \tag{C.10i}
\]

Equivalently, the unconditional quantitative theorem is

\[
 \boxed{
 \left|D_{t,L}(\eta)
 +\frac{t(2t-1)}2J_{\phi,L}\eta^3\right|
 \le B_\phi^{E_{L,2t}}|\eta|^5,
 \qquad |\eta|\le\frac12.}
 \tag{C.10a}
\]

Thus (T.17) has the explicitly quadratic form

\[
 |D_{t,L}(\eta)|
 \le\left(\frac{t(2t-1)}2|J_{\phi,L}|+\varepsilon\right)|\eta|^3.
 \tag{C.11}
\]

The depth dependence of the cubic coefficient can also be bounded using
one shared activation-only base. Define

\[
 A_\phi=\max\{4,4M_\phi^4\}.
 \tag{M.1}
\]

Put

\[
 A=A_\phi,
 \qquad \overline\Theta=A^{2L},
 \qquad \overline b=A^L,
 \qquad \overline\pi=A^{L+1},
\]

initialize
\(\overline V_0=\overline M_0=\overline T_0=0\), and for
\(a=1,\ldots,L\) set

\[
 \overline V_a=A\overline V_{a-1}
 +\overline\Theta^2\overline bA,
\]

\[
 \overline M_a=A\overline V_{a-1}
 +\overline\Theta^2\overline bA
 +2A\overline M_{a-1},
\]

\[
\begin{aligned}
 \overline T_a={}&3\overline\Theta\overline V_{a-1}A
 +3\overline\Theta^3\overline bA
 +6\overline\Theta\overline M_{a-1}A\\
 &+A(\overline T_{a-1}+3\overline M_{a-1}).
\end{aligned}
 \tag{M.2}
\]

Starting from
\((\overline\beta_{L+1},\overline\gamma_{L+1})=(0,1)\), run backwards:

\[
\begin{aligned}
 \overline\beta_a={}&
 \overline b\,\overline V_{a-1}A
 +3\overline\Theta^2\overline b^2A
 +A\overline\beta_{a+1}
 +A\overline\gamma_{a+1}^2\\
 &+2\overline\Theta\overline\gamma_{a+1}\overline bA,
\end{aligned}
\]

\[
 \overline\gamma_a
 =\overline\pi+2A\overline\Theta\overline b
 +2A\overline\gamma_{a+1}.
 \tag{M.3}
\]

Finally define

\[
 \overline S_L=\overline T_L+3\overline M_L,
\]

\[
 \overline H_L=\overline V_L+\overline\beta_1
 +\sum_{a=2}^L
 (\overline\beta_a+\overline\pi\,\overline V_{a-1}),
\]

\[
 \overline J_L=\overline S_L+4\overline H_L.
 \tag{M.4}
\]

Every activation moment in (C.1) has absolute value at most \(A_\phi\).
Termwise induction through (C.3)--(C.9) therefore proves

\[
 \boxed{
 |J_{\phi,L}|\le\overline J_L,
 \qquad
 |\kappa_{\phi,L,t}|
 \le\frac{t(2t-1)}2\overline J_L.}
 \tag{M.5}
\]

The recursion terminates after one forward and one reverse pass of length
\(L\). Thus all activation dependence is in \(A_\phi\), while every
depth and time operation is explicit.

### The requested \(L=3\) specialization

For three hidden layers,

\[
 b_1=d^2,\qquad b_2=d,\qquad b_3=1,
\]

and (C.3)--(C.7) contain exactly three forward and three reverse
assignments. Explicitly,

\[
 J_{\phi,3}=T_3+3M_3
 +4\{V_3+\beta_1+\beta_2+d^2V_1+\beta_3+dV_2\}.
 \tag{C.12}
\]

Unconditionally, \(M_{3,2t}=8t+2\), and therefore

\[
 E_{3,2t}=6p_{2t}^{8t+2}
 +r_{2t}\frac{p_{2t}^{8t+2}-1}{p_{2t}-1}.
 \tag{T.19}
\]

Thus

\[
 \boxed{
 \left|F_{t,3}(2\eta)-F_{2t,3}(\eta)
 +\frac{t(2t-1)}2J_{\phi,3}\eta^3\right|
 \le B_\phi^{E_{3,2t}}|\eta|^5,
 \quad |\eta|\le\frac12.}
 \tag{T.20}
\]

In particular, for \(t=2\),

\[
 \left|F_{2,3}(2\eta)-F_{4,3}(\eta)
 +3J_{\phi,3}\eta^3\right|
 \le B_\phi^{E_{3,4}}|\eta|^5.
 \tag{T.21}
\]

Here \(\kappa_{\phi,3,t}=-t(2t-1)J_{\phi,3}/2\); in particular,
\(\kappa_{\phi,3,2}=-3J_{\phi,3}\).

## 1. Exact finite-width network

At time \(s\), set

\[
 Z_1^s=u^s,\qquad X_1^s=\phi(Z_1^s),
\]

\[
 Z_\ell^s=\frac{W_\ell^sX_{\ell-1}^s}{\sqrt n},
 \qquad X_\ell^s=\phi(Z_\ell^s),
 \quad2\le\ell\le L,
 \tag{1.1}
\]

\[
 f_{n,L}^s=\frac1n(a^s)^TX_L^s.
 \tag{1.2}
\]

All entries of \(u^0,a^0,W_2^0,\ldots,W_L^0\) are mutually independent
standard Gaussians.  Define

\[
 D_L^s=a^s\odot\phi'(Z_L^s),
\]

\[
 R_{\ell-1}^s=\frac{(W_\ell^s)^TD_\ell^s}{\sqrt n},
 \qquad
 D_{\ell-1}^s=R_{\ell-1}^s\odot\phi'(Z_{\ell-1}^s).
 \tag{1.3}
\]

One simultaneous ascent step is

\[
 \theta^{s+1}=\theta^s+hn\nabla_\theta f_{n,L}^s,
\]

or, exactly,

\[
 a^{s+1}=a^s+hX_L^s,
 \tag{1.4}
\]

\[
 W_\ell^{s+1}=W_\ell^s+
 \frac h{\sqrt n}D_\ell^s(X_{\ell-1}^s)^T,
 \quad2\le\ell\le L,
 \tag{1.5}
\]

\[
 Z_1^{s+1}=Z_1^s+hD_1^s.
 \tag{1.6}
\]

If

\[
 Q^a_{rs}=\frac1n(X_a^r)^TX_a^s,
 \qquad K^a_{rs}=\frac1n(D_a^r)^TD_a^s,
\]

then, with only the initialization matrices retained in the raw actions,

\[
 Z_\ell^s=\frac{W_\ell^0X_{\ell-1}^s}{\sqrt n}
 +h\sum_{r<s}Q^{\ell-1}_{rs}D_\ell^r,
 \tag{1.7}
\]

\[
 R_{\ell-1}^s=\frac{(W_\ell^0)^TD_\ell^s}{\sqrt n}
 +h\sum_{r<s}K^\ell_{rs}X_{\ell-1}^r.
 \tag{1.8}
\]

Every learned term is strictly past-time.  The raw initialization-matrix
chronology through terminal time \(N\) is

\[
 \bigl[
  (W_2X_1^s,\ldots,W_LX_{L-1}^s);
  (W_L^TD_L^s,\ldots,W_2^TD_2^s)
 \bigr]_{s=0}^{N-1},
\]

followed by the terminal forward sweep.  It has exactly

\[
 (2N+1)(L-1)
 \tag{1.9}
\]

predictable actions.  A current query may depend on every earlier action,
including earlier transpose actions of the same matrix.

## 2. Fixed-step width identification

For each connector \(2\le\ell\le L\), introduce independent forward and
transpose Gaussian history blocks \((\xi_\ell,\chi_\ell)\) with

\[
 \mathbb E\xi_{\ell,r}\xi_{\ell,s}
 =\mathbb E[X_{\ell-1,r}X_{\ell-1,s}],
 \qquad
 \mathbb E\chi_{\ell,r}\chi_{\ell,s}
 =\mathbb E[D_{\ell,r}D_{\ell,s}].
 \tag{2.1}
\]

Define

\[
 \rho^\ell_{sr}=\mathbb E\partial_{\chi_{\ell,r}}X_{\ell-1,s},
 \quad r<s,
 \qquad
 \sigma^\ell_{sr}=\mathbb E\partial_{\xi_{\ell,r}}D_{\ell,s},
 \quad r\le s.
 \tag{2.2}
\]

The inverse-free population recursion is

\[
 Z_{1,0}=U,\qquad X_{1,s}=\phi(Z_{1,s}),\qquad
 Z_{1,s+1}=Z_{1,s}+hD_{1,s},
 \tag{2.3}
\]

\[
 Z_{\ell,s}=\xi_{\ell,s}
 +\sum_{r<s}(\rho^\ell_{sr}+hQ^{\ell-1}_{rs})D_{\ell,r},
 \qquad X_{\ell,s}=\phi(Z_{\ell,s}),
 \tag{2.4}
\]

\[
 A_s=A+h\sum_{r<s}X_{L,r},
 \qquad D_{L,s}=A_s\phi'(Z_{L,s}),
 \tag{2.5}
\]

\[
 R_{\ell-1,s}=\chi_{\ell,s}
 +\sum_{r\le s}\sigma^\ell_{sr}X_{\ell-1,r}
 +h\sum_{r<s}K^\ell_{rs}X_{\ell-1,r},
 \tag{2.6}
\]

\[
 D_{\ell-1,s}=R_{\ell-1,s}\phi'(Z_{\ell-1,s}),
 \qquad
 F_{N,L}(h)=\mathbb E[A_NX_{L,N}].
 \tag{2.7}
\]

The complete proof that the actual finite-width network converges to
(2.3)--(2.7) at each fixed \(h\ne0\) is
`WIDTH_DEPTH_TIME.md`.  Its indispensable steps are the following.

1. For every globally interlaced predictable row or column action, the
   reused Gaussian matrix has the exact residual conditional law

   \[
   W=P_CW+WP_H-P_CWP_H+P_C^\perp\widetilde W P_H^\perp.
   \tag{2.8}
   \]

2. Gaussian integration by parts gives the old cross block and the two
   new-query identities

   \[
   \mathcal R=SQ+KP^T,\qquad
   \mathbb E[dX_*]=K\rho+Sq,\qquad
   \mathbb E[yD_*]=Q\sigma+Pk.
   \tag{2.9}
   \]

   Substitution into the exact row and column regressions cancels both
   cross-projection terms and leaves precisely (2.4) and (2.6).

3. If \(\phi\) is nonconstant and \(h\ne0\), every finite population
   feature and cotangent history Gram is positive definite.  Chronologically,
   a fresh forward innovation opens every next feature Schur complement;
   the fresh top forward innovation opens the top cotangent Gram when
   \(\phi'\) is nonconstant; a separate affine calculation opens it when
   \(\phi'\) is a nonzero constant; and fresh descending transpose
   innovations open every remaining cotangent Gram.  This is a pointwise
   fixed-\(h\) argument, not a small-\(h\) rank expansion.

4. One stopped raw/extended/ideal coupling is run through all (1.9)
   actions.  Its explicit moment tower starts at

   \[
   2m\,8^{3(2N+1)(L-1)+1}
   \tag{2.10}
   \]

   for failure exponent \(m\). It gives \(O(n^{-1/2})\) field, Gram,
   cross-moment, and response errors in every finite moment, stopping
   probability \(O(n^{-m})\), and a raw polynomial energy majorant.
   Stopping removal and terminal uniform integrability then prove (T.3).

If \(\phi\equiv\pm1\), the identity \(F_{N,n,L}(h)=Nh\) holds for every
\(n\). Thus all branches are covered.

## 3. Singular regularity and explicit fifth-order envelope

The recursion (2.3)--(2.7) contains no covariance inverse. It remains
defined at \(h=0\), where every repeated-time covariance coalesces.

For a local Gaussian expectation

\[
 \mathcal N(h)=\mathbb E_{Y\sim N(0,C(h))}\psi(h,Y),
\]

set

\[
 \mathcal P_C=\partial_h+\frac12C'(h):D_Y^2,
 \qquad \Psi_0=\psi,\qquad \Psi_{r+1}=\mathcal P_C\Psi_r.
 \tag{3.1}
\]

Regularize \(C\) by \(C+\delta I\), apply Price differentiation, couple by
the positive-semidefinite square root, truncate the common Gaussian vector,
and use the weighted \(C^{12}\) envelope (T.2). Letting
\(\delta\downarrow0\) proves, through five iterations,

\[
 \mathcal N^{(r)}(h)=\mathbb E\Psi_r(h,Y),
 \qquad0\le r\le5,
 \tag{3.2}
\]

even at a changing-rank covariance.

This also gives a non-circular definition of the exact jets used in (T.5).
Traverse the Gaussian calls of (2.3)--(2.7) in their displayed
forward/backward chronology. Whenever an earlier scalar node \(S\) is used
in a later call, introduce formal tokens \(S^{[j]}\), \(0\le j\le5\),
with

\[
 \partial_hS^{[j]}=S^{[j+1]}.
 \tag{3.3}
\]

For a new call \(T(h)=\mathbb E\psi(h,Y_h)\), define, in order,

\[
 \mathcal J^{\mathrm{PJ}}_{r}(T)
 :=\mathbb E\Psi_r(0,Y_0),
 \qquad 0\le r\le5,
 \tag{3.4}
\]

and then set \(S^{[j]}(0)=\mathcal J^{\mathrm{PJ}}_j(S)\) whenever
that token is subsequently used. Every covariance entry and response
coefficient is an earlier scalar node in this chronology, so the
construction is triangular. At the terminal call, define

\[
 \mathcal J^{\mathrm{PJ}}_{r,N,L}(\phi)
 :=\mathcal J^{\mathrm{PJ}}_r(F_{N,L}).
 \tag{3.5}
\]

Only after these numbers have been constructed does (3.2) prove

\[
 \mathcal J^{\mathrm{PJ}}_{r,N,L}(\phi)=F_{N,L}^{(r)}(0).
 \tag{3.6}
\]

`COMPILER_DEPTH_TIME.md` applies (3.1)--(3.2) in exactly
\((2N+1)(L-1)\) chronological Gaussian calls, each of dimension at most
\(D_N=2N+2\). It expands every formal derivative, ordered spatial
multiindex, covariance contraction, response derivative, and binomial
multiplicity.  The reachable derivative budget is

\[
 2r+j+q\le10;
\]

a response begins at activation order at most two, so no derivative above
\(\phi^{(12)}\) occurs. The explicit envelope recursion proves

\[
 F_{N,L}\in C^5([-1,1]),
 \qquad
 |F_{N,L}^{(5)}(h)|\le\overline{\mathcal J}_5(F_{N,L})
 \le B_\phi^{E_{L,N}}.
 \tag{3.7}
\]

At \(h=0\), every exact Price jet is a finite product-Gaussian integral
of \(\phi,\ldots,\phi^{(12)}\). This constructs all derivatives before
identifying them with output jets; (3.7) uses no output-defined constant.

## 4. Fixed bounded-operator bridge and cubic coefficient

The original finite-list oracle did not construct one compatible action on
moving singular queries. The repaired bridge instead fixes a genuine
bounded operator before training; `AUDIT_CUBIC_REAUDIT.md` independently
audits this replacement and finds no remaining gap.

For each hidden layer put \(\mathcal H_a=L^2(\Omega_a)\), where the first
Gaussian chaos of \(\Omega_a\) is infinite dimensional. Split that chaos
into mutually orthogonal infinite-dimensional blocks for its incident
connectors and endpoint seed. For \(2\le a\le L\), choose onto isometries

\[
 I_a:\mathcal H_{a-1}\to\mathcal G_a^{\to},
 \qquad
 J_a:\mathcal H_a\to\mathcal G_{a-1}^{\leftarrow},
\]

and define

\[
 \boxed{
 W_{a,0}=I_a+J_a^*,
 \qquad W_{a,0}^*=I_a^*+J_a.}
 \tag{4.1}
\]

These are fixed bounded operators with norm at most two, not trainable
Hilbert--Schmidt parameters. Isometry gives the required raw Gaussian
source Grams. Orthogonality of the allocated first-chaos blocks gives the
primitive source independence.

The adjoint pieces are exactly the nonlinear responses. If

\[
 x=\Psi(J_ac_1,\ldots,J_ac_m,\zeta),
\]

where \(\zeta\) is independent of the allocated \(J_a\)-block, Gaussian
integration by parts and Riesz uniqueness give

\[
 J_a^*x=\sum_{r=1}^m\mathbb E[\partial_r\Psi]c_r.
 \tag{4.2}
\]

Symmetrically, \(I_a^*c\) is the corresponding sum over exposed forward
queries. These identities use no Gram inverse, remain valid at singular
histories, and are literally compatible under history enlargement because
the operators in (4.1) never change. Bounded linearity also lets them act
on full nonlinear query curves and commute with their scalar derivatives.

At time \(s\), let

\[
 \mathcal K_{a,s}=h\sum_{r<s}D_{a,r}\otimes X_{a-1,r}.
\]

Using (4.2) and its transpose analogue,

\[
 (W_{a,0}+\mathcal K_{a,s})X_{a-1,s}
 =I_aX_{a-1,s}
 +\sum_{r<s}(\rho^a_{sr}+hQ^{a-1}_{rs})D_{a,r},
 \tag{4.3}
\]

\[
 (W_{a,0}+\mathcal K_{a,s})^*D_{a,s}
 =J_aD_{a,s}
 +\sum_{r\le s}\sigma^a_{sr}X_{a-1,r}
 +h\sum_{r<s}K^a_{rs}X_{a-1,r}.
 \tag{4.4}
\]

These are exactly the two temporal nodes (2.4) and (2.6). Chronological
induction therefore identifies the bounded-operator construction with the
complete inverse-free DAG for every finite step vector, not only at the
origin.

On every finite scalar slice generated by \(\mathbf g\) and its first two
variations, bounded activation derivatives, linear growth, Gaussian
moments, and the finite response sums give a common \(L^p\) dominator.
Repeated scalar difference quotients hence give a common \(C^3\) germ with
commuting mixed derivatives. Reverse differentiation with the genuine
adjoints in (4.1) gives

\[
 D\mathcal F[v]=\langle\mathbf g,v\rangle,
 \qquad
 \mathbf g=(X_L,D_L\otimes X_{L-1},\ldots,D_2\otimes X_1,D_1).
 \tag{4.5}
\]

Consequently the temporal dynamics is exactly

\[
 \theta_{s+1}=\theta_s+h\mathbf g(\theta_s)
 \tag{4.6}
\]

on the fixed width-first population construction. No finite-width Taylor
expansion and no exchange of limits occurs.

Put

\[
 \mathbf h=D\mathbf g[\mathbf g],\qquad
 \mathsf S=D^3\mathcal F[\mathbf g,\mathbf g,\mathbf g],
 \qquad \mathsf H=\|\mathbf h\|^2.
\]

Direct differentiation of (4.6) gives

\[
 \theta_N'=N\mathbf g,qquad
 \theta_N''=N(N-1)\mathbf h,
 \tag{4.7}
\]

\[
 \theta_N'''=6{N\choose3}D\mathbf g[\mathbf h]
 +\frac{N(N-1)(2N-1)}2
 D^2\mathbf g[\mathbf g,\mathbf g].
 \tag{4.8}
\]

The scalar mixed-derivative symmetry of the common germ gives

\[
 D^2\mathcal F[\mathbf h,\mathbf g]=\mathsf H,
 \quad
 D\mathcal F[D\mathbf g[\mathbf h]]=\mathsf H,
 \quad
 D\mathcal F[D^2\mathbf g[\mathbf g,\mathbf g]]=\mathsf S.
 \tag{4.9}
\]

The third-order chain rule therefore yields

\[
 F_{N,L}^{(3)}(0)
 =\frac{N(4N^2-3N+1)}2\mathsf S
 +2N(N-1)(2N-1)\mathsf H.
 \tag{4.10}
\]

The nodewise forward and reverse contractions in this same fixed-operator
DAG give exactly (C.1)--(C.9). In particular,

\[
 \mathsf S=\mathsf S_{\phi,L},\qquad
 \mathsf H=\mathsf H_{\phi,L}.
 \tag{4.11}
\]

Finally,

\[
 8\frac{t(4t^2-3t+1)}2
 -\frac{2t(16t^2-6t+1)}2=-3t(2t-1),
\]

\[
 16t(t-1)(2t-1)-4t(2t-1)(4t-1)
 =-12t(2t-1),
 \tag{4.12}
\]

This proves (C.10). Both Section 3 and this calculation compute the third
derivative of the same width-first DAG, so uniqueness of that derivative
also proves the intertwining identity between the exact Price-compiler
coefficient (T.6) and the compact nine-moment formula.

## 5. Taylor remainder and parity

Under

\[
 h\mapsto-h,\qquad A\mapsto-A,
 \qquad \chi_{\ell,s}\mapsto-\chi_{\ell,s},
\]

all forward preactivations, features, and Grams remain fixed, while all
cotangents, responses, accumulated response coefficients, and outputs
change sign. Hence every \(F_{N,L}\) is odd. Put
\(d_\phi=\mathbb E\phi'(G)^2\). The exact compiler gives the direct linear
jet

\[
 F_{N,L}'(0)=N\Theta_L,
 \qquad \Theta_L=\sum_{r=0}^Ld_\phi^r.
 \tag{5.1}
\]

Thus \(D_{t,L}\) has zero derivatives of orders \(0,1,2,4\) at the
origin, and (3.6) plus (T.6) gives

\[
 D_{t,L}^{(3)}(0)=6\kappa_{\phi,L,t}.
\]

For \(|\eta|\le1/2\), both \(\eta\) and \(2\eta\) lie in the compiler
interval. Equation (3.7) gives

\[
 |D_{t,L}^{(5)}(x)|
 \le32B_\phi^{E_{L,t}}+B_\phi^{E_{L,2t}}
 \le33B_\phi^{E_{L,2t}}.
 \tag{5.2}
\]

Taylor's integral remainder through order four is

\[
 D_{t,L}(\eta)-\kappa_{\phi,L,t}\eta^3
 =\frac1{24}\int_0^\eta(\eta-x)^4D_{t,L}^{(5)}(x)\,dx.
 \tag{5.3}
\]

Since \(33/120<1\), (5.2)--(5.3) prove (T.16). Under (T.18),

\[
 B_\phi^{E_{L,2t}}|\eta|^2
 \le\frac{B_\phi^{E_{L,2t}}}
          {1+B_\phi^{E_{L,2t}}}\varepsilon
 \le\varepsilon,
\]

which proves (T.17).

If \(d_\phi=0\), continuity and Gaussian full support imply
\(\phi'\equiv0\), and normalization gives \(\phi\equiv\pm1\). Then
\(F_{N,L}(h)=Nh\) exactly, the exact compiler coefficient is zero, and
every discrepancy vanishes. This completes
all branches.

## 6. What the theorem does and does not claim

The theorem is unconditional for every fixed finite pair \((L,t)\). It
uses the required order

\[
 n\to\infty\text{ at fixed }\eta,
 \qquad\text{then }\eta\to0.
\]

It gives the activation-only bases \(B_\phi\) and \(A_\phi\), a terminating
nine-moment depth recursion for the cubic coefficient, the exact quadratic
time factor \(-t(2t-1)/2\), the explicit shared-depth majorant
\(\overline J_L\), and a completely explicit depth--time exponent for the
fifth-order remainder. The fixed bounded-operator bridge proves that this
compact coefficient equals the independently constructed Price-compiler
jet, so neither definition is circular.

It does not assert the sharper all-time estimate

\[
 |D_{t,L}(\eta)-\kappa_{\phi,L,t}\eta^3|
 \le C_{\phi,L}t^4|\eta|^5,
 \qquad |\eta|\le c_{\phi,L}/t.
\]

Such a statement requires a uniform-in-time stability theorem for the
actual reused-matrix population dynamics. A terminating fixed-\(t\)
compiler does not supply it. Moreover, the identity-activation calculation
at \(L=2\) has a nonzero quartic polynomial in \(t\) as its fifth-order
coefficient, so no shared power below \(t^4\) can hold in general. The
explicit fixed-\((L,t)\) theorem (T.16) is the
unconditional general result proved here.
