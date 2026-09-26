# Direct Gaussian peeling of the actual p=1 projected kernel

Scoped theory attempt, 2026-09-21. This document uses only
`docs/observable_p1.md`, the supplied portions of
`docs/gaussian_calculus.md` (Sections 1–4, 7.1, E.1), and
`docs/global_nonlinear.md` (Section 3, H3.1, C5.27–31). It does not use
other study results, training experiments, or a replacement Gaussian kernel.
The mathematical statements below are internally derived and unpromoted.

The exact finite source contraction can be completed. It leaves two explicit
compositions. Both compositions can then be removed by convergent expansions
whose individual terms are finite expectations of activation powers or
derivatives at jointly Gaussian arguments. The resulting representation is an
exact limit with a certified truncation error, rather than a proved finite
terminating formula for the complete tanh kernel. No obstruction based on the
non-Gaussianity of an intermediate observable is asserted.

## 1. Complete finite contraction

Write \(\varphi=\tanh\), and use the supplied initialization, with independent
standard Gaussian coordinates \(G_i,Z_i,X_i\), \(i=1,2\):

\[
h_i=\varphi(G_i),\quad v=E\varphi(G)^2,\quad
H_i=\varphi(\sqrt vX_i),\quad \tau=EH_i^2,\quad \alpha=1-\tau,
\]
\[
\zeta_i=\sqrt\tau Z_i,\quad R_i=\zeta_i+\alpha h_i,\quad
k_i=\varphi(R_i),\quad \beta=Eh_ik_i,\quad
s=Ek_i^2,\quad \gamma=1-s=E\varphi'(R_i).
\]

Here \(0<v,\tau,\alpha<1\). The lower and upper populations are separate.
For any input \(u\in\mathbb R^2\), put

\[
U_u=G\cdot u,\qquad
m_i(u)=E[h_i\varphi(U_u)],\qquad
n_i(u)=E[k_i\varphi(U_u)].
\]

These definitions cover unit-circle inputs \(u=u_\theta\), zero inputs,
and arbitrary finite inputs. Simultaneous sign symmetry makes the constant
entry of \(E_1[b_1\varphi(U_u)]\) zero.

The source contraction H3.1 is, in the present notation,

\[
E_2[B A_0F]
=\sum_jE_1[Fh_j]E_2[\partial_{\Xi_j}B]
+\sum_jE_1[\partial_{\zeta_j}F]E_2[BH_j].
\tag{1}
\]

For \(B=H_i\), \(F=h_j\), its two sums are respectively
\(\alpha v\delta_{ij}\) and zero. For \(F=k_j\), they are
\(\alpha\beta\delta_{ij}\) and \(\tau\gamma\delta_{ij}\), since
\(\partial_{\zeta_\ell}k_j=\delta_{j\ell}\varphi'(R_j)\).
Constant rows and columns vanish. Thus this calculation retains the reverse
response and yields precisely the supplied raw contraction \(C\).

Set, with the canonical \(\eta=1/4096\),

\[
a^2=v+\eta,\quad
b^2=s+\eta-\frac{\beta^2}{v+\eta},\quad
c^2=\tau+\eta,\quad
\delta=\frac\beta{v+\eta},\quad
\rho=\frac{\alpha\beta\eta}{v+\eta}+\tau\gamma.
\]

In particular \(b^2\ge\eta+s\eta/(v+\eta)>0\), by
\(\beta^2\le vs\). The normalized lower pairing has entries
\(m_i/a\) and \((n_i-\delta m_i)/b\); the upper feature is \(H_i/c\).
Multiplying the exact two nonzero bands of \(D\), including its right
inverse transpose, therefore gives

\[
q_u=b_2^TD E_1[b_1\varphi(U_u)]
=t_1(u)H_1+t_2(u)H_2,
\tag{2}
\]
\[
t_i(u)=\frac1{\tau+\eta}
\left\{\frac{\alpha v}{v+\eta}m_i(u)
+\frac\rho{b^2}\big[n_i(u)-\delta m_i(u)\big]\right\}.
\tag{3}
\]

Consequently the actual target is exactly

\[
K(u,w)=E\!\left[
\varphi\!\left(\sum_i t_i(u)\varphi(\sqrt vX_i)\right)
\varphi\!\left(\sum_i t_i(w)\varphi(\sqrt vX_i)\right)\right].
\tag{4}
\]

Equation (4) is already a useful exact finite reduction: all lower and
reverse population integrations have been compressed into scalar constants
and two input-dependent coefficients. It is not yet a terminal formula of
the requested simple Gaussian-activation type, because \(n_i\), \(s\),
\(\beta\), and the two outer activations still contain compositions.

## 2. Eliminate the lower nested activation with a convergent derivative expansion

Define only simple Gaussian atoms:

\[
\mu_j(\sigma^2)=E[\varphi(\sigma Z)^j],\qquad
d_j(\sigma^2)=E[\varphi^{(j)}(\sigma Z)],
\]
\[
\nu_j(u_i,|u|^2)
=E[\varphi(A)^j\varphi(B)],\qquad
\operatorname{Cov}(A,B)=
\begin{pmatrix}1&u_i\\u_i&|u|^2\end{pmatrix}.
\tag{5}
\]

The last matrix is positive semidefinite because \(u_i^2\le|u|^2\).
At axis or zero inputs it may be singular; the realization
\((A,B)=(G_i,G\cdot u)\) defines it without an inverse. In particular
\(m_i(u)=\nu_1(u_i,|u|^2)\). All covariance data are known before these
integrations: the scalar variances are \(1\), then
\(v=\mu_2(1)\), then \(\tau=\mu_2(v)\); the remaining covariance
entries are the supplied input coordinates.

For every real \(z\) and \(|h|\le1\), the analytic Taylor expansion gives

\[
\varphi(z+\alpha h)
=\sum_{j=0}^{\infty}\frac{\alpha^j h^j}{j!}\varphi^{(j)}(z).
\tag{6}
\]

Here is a uniform proof and bound, so (6) is not a formal Taylor claim.
The poles of \(\tanh z\) have imaginary parts \(\pi/2+\pi\mathbb Z\).
On the complex strip \(|\operatorname{Im}z|\le1\),

\[
|\tanh(x+iy)|^2
=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}
\le\tan^2(1),\qquad
|\operatorname{sech}^2(x+iy)|\le\sec^2(1).
\]

For the first bound, the ratio lies between 1 and \(\tan^2 y\), and
\(\tan^2(1)>1\). Cauchy's coefficient formula on the unit circle about
any real \(z\) consequently bounds
\(|\varphi^{(j)}(z)|/j!\le M_0=\tan(1)\), and
\(|\varphi^{(j+1)}(z)|/j!\le M_1=\sec^2(1)\).
Since \(0<\alpha<1\), both expansions are uniformly absolutely
convergent, with tails at degree \(J\) bounded by

\[
\epsilon_{0,J}=\frac{M_0\alpha^{J+1}}{1-\alpha},\qquad
\epsilon_{1,J}=\frac{M_1\alpha^{J+1}}{1-\alpha}.
\tag{7}
\]

Independence of \(\zeta_i\) and \(G\), boundedness of the remaining
activation factors, and the summable uniform bound now justify taking
expectations term by term. The exact lower coefficients are

\[
n_i(u)=\sum_{j=0}^{\infty}
\frac{\alpha^j}{j!}d_j(\tau)\nu_j(u_i,|u|^2),
\tag{8}
\]
\[
\beta=\sum_{j=0}^{\infty}
\frac{\alpha^j}{j!}d_j(\tau)\mu_{j+1}(1),
\tag{9}
\]
\[
\gamma=\sum_{j=0}^{\infty}
\frac{\alpha^j}{j!}d_{j+1}(\tau)\mu_j(1),
\qquad s=1-\gamma.
\tag{10}
\]

The errors in degree-\(J\) truncations of (8), (9) are at most
\(\epsilon_{0,J}\), uniformly over all inputs. The error in (10) is at
most \(\epsilon_{1,J}\). Oddness eliminates the even \(j\) terms in
(8), (9); evenness eliminates the odd \(j\) terms in (10).

These formulas contain no nested activation inside any Gaussian expectation.
Derivative atoms themselves have a finite recursion if desired. Set
\(P_0(x)=x\), \(P_{j+1}(x)=(1-x^2)P_j'(x)\). Then
\(\varphi^{(j)}(z)=P_j(\varphi(z))\), so \(d_j(\tau)\) is a finite
linear combination of \(\mu_k(\tau)\). This recursion follows directly
by differentiating and using \(\varphi'=1-\varphi^2\).

## 3. Eliminate the outer nested activation without assuming a small argument

A Taylor series for \(\tanh q_u\) about zero needs
\(|q_u|<\pi/2\); no such condition is imposed here. A polynomial
construction with a global explicit error avoids an unproved radius claim.

For \(N\ge1\), \(0\le r\le N\), and \(-1\le h\le1\), define

\[
w_{N,r}(h)=\binom Nr\left(\frac{1+h}{2}\right)^r
                    \left(\frac{1-h}{2}\right)^{N-r},
\qquad z_r=2r/N-1.
\]

For a two-dimensional index \(r=(r_1,r_2)\), put

\[
A_u(r)=\varphi\big(t_1(u)z_{r_1}+t_2(u)z_{r_2}\big),
\]
\[
P_{N,u}(H)=\sum_{r_1,r_2=0}^{N}A_u(r)
                    w_{N,r_1}(H_1)w_{N,r_2}(H_2).
\tag{11}
\]

All arguments in \(A_u\) are deterministic real numbers. In particular,
there is no nested random activation in these coefficients. The polynomial
in (11) is bounded by 1 because its nonnegative weights sum to 1.

To prove the approximation bound, condition on \(H\) and introduce
independent \(R_i\sim\operatorname{Binomial}(N,(1+H_i)/2)\).
Equation (11) is the conditional expectation of
\(\varphi(\sum_i t_i(u)(2R_i/N-1))\). Since \(\varphi\) is
1-Lipschitz and \(E[(2R_i/N-1-H_i)^2\mid H]=(1-H_i^2)/N\),
Cauchy–Schwarz gives

\[
\sup_{H\in[-1,1]^2}|P_{N,u}(H)-\varphi(q_u)|
\le\frac{|t_1(u)|+|t_2(u)|}{\sqrt N}.
\tag{12}
\]

Independence of \(H_1,H_2\) yields the following finite terminal formula:

\[
K_N(u,w)=E[P_{N,u}(H)P_{N,w}(H)]
=\sum_{r,s\in\{0,\ldots,N\}^2}
A_u(r)A_w(s)\prod_{i=1}^2 J_N(r_i,s_i),
\tag{13}
\]
\[
J_N(r,s)=\binom Nr\binom Ns\,2^{-2N}
E[(1+\varphi(\sqrt vX))^{r+s}
  (1-\varphi(\sqrt vX))^{2N-r-s}].
\tag{14}
\]

Expanding the two polynomials makes (14) an explicit finite combination of
\(\mu_j(v)\), \(0\le j\le2N\). Thus its covariance and every required
Gaussian atom can be precomputed, independently of \(u,w\). The only
input-dependent work in (13) is forming the deterministic coefficients
\(A_u,A_w\) from (3).

Because both \(P_{N,u}\) and \(\varphi(q_u)\) are bounded by 1,
\(|ab-cd|\le|a-c|+|b-d|\) applies to their products. Equations (12)–(14)
therefore prove

\[
K(u,w)=\lim_{N\to\infty}K_N(u,w),\qquad
|K-K_N|\le\frac{\|t(u)\|_1+\|t(w)\|_1}{\sqrt N}.
\tag{15}
\]

The coefficient norm is finite by (3) and the strictly positive ridge
denominators. This proves a convergent terminal-Gaussian calculation for the
actual projected kernel for every finite input pair, without any Gaussian
replacement of \(q_u\). Equations (7) and (15) control separate lower-series
and outer-polynomial truncations. A fully numerical implementation must also
propagate the lower coefficient errors through (3) and control its scalar
quadrature errors; that implementation and a cost guarantee are not supplied
by this theory attempt. Positivity of the exact denominators ensures
continuity and convergence as all lower truncation errors tend to zero.

## 4. What terminates, and the exact remaining finite-order expression

The Gaussian-source operation itself terminates at (2)–(4). Section E.1's
Stein rule terminates when there are finitely many explicit Gaussian
polynomial factors, reducing their number with each contraction. At (4),
there is no such Gaussian polynomial factor to remove: the Gaussian roots
occur inside the supplied activation expressions. This observation describes
the next operation of that particular recurrence; it is not a proof that no
other finite identity can exist.

The lower Taylor construction gives a finite identity with an explicit
remaining integral. For example, let
\(T_J(z,h)=\sum_{j=0}^J\alpha^jh^j\varphi^{(j)}(z)/j!\). Then

\[
\varphi(\zeta+\alpha h)-T_J(\zeta,h)
=\frac{(\alpha h)^{J+1}}{J!}
  \int_0^1(1-r)^J\varphi^{(J+1)}(\zeta+r\alpha h)\,dr.
\tag{16}
\]

Multiplying (16) by \(\varphi(U_u)\) and taking expectation is the exact
remainder after the finite simple-Gaussian sum in (8). The analogous
formula with \(\varphi'\) gives the remainder in (10). Formula (7) is
a sharper convenient geometric bound on these particular remainders.

Likewise, if \(e_{N,u}(H)=\varphi(q_u)-P_{N,u}(H)\), the exact finite
outer remainder is

\[
K-K_N=E[e_{N,u}P_{N,w}+P_{N,u}e_{N,w}+e_{N,u}e_{N,w}],
\tag{17}
\]

with the direct bound (15). Neither (16) nor (17) has been shown to vanish
at finite order for this tanh problem. Thus the present result establishes
an exact convergent, recursively calculable reduction to simple Gaussian
activation/derivative moments, together with exact finite-order remainders.
It does not establish a finite terminal formula of the E.1 polynomial-jet
kind, and it does not claim such a formula impossible.

For polynomial activations substituted consistently into the model, the
same substitutions would be finite polynomial algebra: the lower
composition and outer composition then have finite degree, and the
Gaussian moment recurrence from Section 4 would terminate. That fact
identifies why the E.1 mechanism terminates in its stated polynomial
factor algebra; it does not change the activation in the present target.
