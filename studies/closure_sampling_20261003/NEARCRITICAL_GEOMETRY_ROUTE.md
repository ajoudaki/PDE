# Near-critical Gaussian initialization: depth gains and an unbounded activation

2026-10-04. Author: scoped agent `nearcritical_geometry`.

This is a self-contained initialization derivation, not an all-time training
or compression theorem. The assigned scientific inputs were the prompt and
the four notes listed at the end. No other study, book material, linked
scientific dependency, experiment, or external source was consulted. The
canonical-notation, neural-network reference, rigorous-proof, and research
process instructions were applied. Only this assigned file is written.

The principal conclusions are exact. With unit forward Gaussian second
moment and derivative second moment `chi`, the depth-`L` limiting tangent
second moment is `chi^L`. A fixed `chi>1` therefore produces exponential
initialized tangent sensitivity. The weaker assertion that `chi` is merely
close to one does not change that conclusion. A two-sided tolerance of order
`1/L` controls this gain and the inverse population Gram gap by constants
and a polynomial, respectively; order `log(L)/L` still gives polynomial
bounds. An explicit unbounded, nonlinear, analytic, globally Lipschitz
family below has a stable real variance map throughout a nontrivial interval
of derivative gains on both sides of one. Its complex Gaussian moment tube
has radius of order `(sum_{j=0}^{L-1} chi^j)^(-1/2)`.

## 1. Model and precise limits

Let `d>=2`, let `x` range over the ordinary Euclidean unit sphere in
`R^d`, and let every hidden layer have width `n`. At initialization put

\[
z^{(1)}(x)=W^{(1)}x,\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
h^{(\ell)}(x)=\phi(z^{(\ell)}(x)),
\tag{1}
\]

where `W^(1)` has independent `N(0,1)` entries, the subsequent matrices
have independent `N(0,1/n)` entries, and the matrices are independent across
layers. Thus the first-layer preactivation variance is one. This is
equivalent to first-layer variance `1/d` and input `sqrt(d)x`.
For the canonical source convention `v=x_source/sqrt(d)`, where
`||x_source||=sqrt(d)`, the unit argument called `x` in this note is
exactly `v`, and `W^(1)=A`. The first-layer scaling is unchanged.

Initially assume that `phi:R->R` is smooth and globally Lipschitz, with

\[
\mathbb E\phi(Z)^2=1,\qquad
\chi=\mathbb E\phi'(Z)^2>0,\qquad Z\sim N(0,1).
\tag{2}
\]

Let `(X,Y)` be jointly standard real Gaussian with correlation `c`. Define

\[
F(c)=\mathbb E[\phi(X)\phi(Y)],\qquad
K_0(c)=c,\qquad K_{\ell+1}(c)=F(K_\ell(c)),\qquad -1\le c\le1.
\tag{3}
\]

For each fixed finite depth and fixed finite set of real inputs, the
normalized empirical feature Gram of (1) converges in probability to
`K_L(x^T y)`. Indeed, conditional on preceding layers, each new row of
preactivations is Gaussian with covariance the preceding empirical Gram.
Lipschitz growth bounds the conditional fourth moments locally in that
covariance. Conditional Chebyshev then controls empirical second moments,
and Gaussian dominated convergence makes their conditional expectations
continuous in the covariance. Induction proves the assertion and preserves
unit diagonal by (2). This proof takes `n->infinity` at each fixed `L`;
it does not interchange the width and depth limits.

## 2. General near-critical covariance geometry

Define the normalized probabilists' Hermite polynomials by

\[
e^{tx-t^2/2}=\sum_{k\ge0}H_k(x)t^k/k!,\qquad h_k=H_k/\sqrt{k!}.
\]

They form an orthonormal basis of Gaussian `L^2`. Here are the facts needed
for that statement and its use. Taking expectations of two generating
functions gives
`E h_j(X)h_k(Y)=1_{j=k}c^k`. Completeness can be proved as follows: if
`g` is orthogonal to all polynomials, the function
`M(z)=E[g(Z)e^(zZ)]` is entire by Cauchy--Schwarz and Gaussian exponential
integrability; all its derivatives at zero vanish. Its restriction to the
imaginary axis is the Fourier transform of the integrable Gaussian-weighted
function `g`, so that transform vanishes. Convolution with each Gaussian
density is then zero by its explicit Fourier integral and Fubini. These
convolutions tend in `L^1` to the original function, proving it is zero.
The last convergence follows from continuity of translations in `L^1`
and concentration of Gaussian densities at zero. This establishes
completeness without an additional scientific dependency.

Write `a_k=E[phi(Z)h_k(Z)]` and `p_k=a_k^2`. Integration by parts and
`xh_j-h_j'=sqrt(j+1)h_(j+1)` give
`E[phi'(Z)h_j(Z)]=sqrt(j+1)a_(j+1)`. To justify integration by parts,
insert a smooth cutoff on `[-2R,2R]` equal to one on `[-R,R]`, with
derivative bounded by `C/R`, and then use Cauchy--Schwarz and Gaussian
polynomial moments to send `R` to infinity. Parseval and the correlated
Hermite identity consequently give

\[
F(c)=\sum_{k\ge0}p_kc^k,\qquad
\sum_{k\ge0}p_k=1,\qquad
\sum_{k\ge1}kp_k=\chi.
\tag{4}
\]

If additionally `phi''` has finite Gaussian second moment, the same
argument gives

\[
\kappa:=\mathbb E\phi''(Z)^2
=\sum_{k\ge2}k(k-1)p_k=F''(1-).
\tag{5}
\]

Thus `F(1)=1` and `F'(1-)=chi`. Define the finite geometric sum

\[
S_L=\sum_{j=0}^{L-1}\chi^j
=\begin{cases}(\chi^L-1)/(\chi-1),&\chi\ne1,\\L,&\chi=1,\end{cases}
\qquad L\ge1.
\tag{6}
\]

The exact depth identities are

\[
K_L'(1)=\chi^L,\qquad
K_L''(1)=\kappa\chi^{L-1}S_L.
\tag{7}
\]

For proof, let `A_l=K_l'(1)` and `B_l=K_l''(1)`. The chain rule gives
`A_(l+1)=chi A_l` and
`B_(l+1)=kappa A_l^2+chi B_l`, starting from `A_0=1`, `B_0=0`.
Solving the first recursion and substituting it into the second yields
`B_L=kappa sum_(j=0)^(L-1) chi^(L-1+j)`, which is (7).
The endpoint chain rules also follow by composing the one-sided quadratic
Taylor expansions supplied by (4)--(5).

Each `K_L` has nonnegative power-series coefficients summing to one;
write them as `p_(L,k)`. A deterministic realization of the kernel is

\[
\Phi_L(x)=\bigoplus_{k\ge0}\sqrt{p_{L,k}}\,x^{\otimes k},\qquad
\langle\Phi_L(x),\Phi_L(y)\rangle=K_L(x^\top y).
\tag{8}
\]

The direct sum uses the ordinary tensor inner products, and `x^(tensor 0)=1`.
If `v` is a unit tangent at `x`, set `x(theta)=x cos(theta)+v sin(theta)`.
The degree-`k` first derivative has squared norm `k`. Its second derivative
has one radial term of squared norm `k^2` and two copies of each placement
of two tangent vectors, contributing `4 binom(k,2)`. These tensor terms
are mutually orthogonal. Equations (7)--(8) therefore prove

\[
\|D\Phi_L(x)[v]\|^2=\chi^L,\qquad
\left\|\frac{d^2}{d\theta^2}\Phi_L(x(\theta))\bigg|_{\theta=0}\right\|^2
=\chi^L+3\kappa\chi^{L-1}S_L.
\tag{9}
\]

These are actual Hilbert-space derivatives: the corresponding first and
second derivative norms of each degree are constant along the circle,
and their sums in (7) are finite. Integral difference quotients followed
by dominated convergence justify differentiation of the direct sum.

For an activation whose real derivatives through order two are bounded,
the two corresponding normalized squared derivatives of the finite network
in (1) converge in probability to (9), at each fixed angle and depth.
For completeness, augment the layer variables by their first two angle
derivatives. A fresh linear layer makes each row of this finite vector
conditionally jointly Gaussian. Applying the scalar chain rule gives the
next activation vector and jets as functions of that Gaussian vector.
Bounded activation derivatives and linear activation growth bound their
fourth moments by finite Gaussian polynomial moments. Conditional
Chebyshev and induction give convergence of their empirical Gram, including
the diagonal jet entries in (9). The explicit family in Section 4 satisfies
these hypotheses. No uniform-in-angle or trained-network assertion is made.

In particular, for a fixed `chi>1`, the first norm in (9) is `chi^(L/2)`.
Any estimate that would bound this initialized observable uniformly by a
polynomial in depth is false. This is a statement about that observable,
not a lower bound against a compressor of the network prediction.

## 3. The population Gram gap and quantitative tolerance

Let `x_1,...,x_m` have positive-definite input Gram `C_0`, with
`gamma_0=lambda_min(C_0)>0`. Let
`C_L=(K_L(x_a^T x_b))_(a,b)`. For finite `kappa`,

\[
\lambda_{\min}(C_L)
\ge\frac{\chi^L}{\gamma_0^{-1}+(\kappa/\chi)S_L}.
\tag{10}
\]

Here is the matrix and scalar argument. If a unit-diagonal positive
semidefinite matrix `C` satisfies `C>=eta I`, then `B=C-eta I` is
positive semidefinite with diagonal `1-eta`. For each `k>=1`,

\[
C^{\circ k}=B^{\circ k}+[1-(1-\eta)^k]I.
\]

Every entrywise power of `B` is positive semidefinite because it is a
Gram of tensor powers of Gram vectors of `B`. The zeroth power is the
positive semidefinite all-ones matrix. Summing with the weights in (4)
therefore gives `F[C]>=[1-F(1-eta)]I`. Define
`eta_0=gamma_0`, `eta_(l+1)=1-F(1-eta_l)` and iterate this matrix bound.

For `0<eta<=1`, integer `k>=1`,

\[
1-(1-\eta)^k\ge\frac{k\eta}{1+(k-1)\eta}.
\]

For `eta<1`, this follows on rearrangement from
`(1-eta)^(-(k-1))>=1+(k-1)eta`; that inequality follows by integrating
its derivative bound `k-1`. The endpoint is immediate. Apply the convex
function `u->1/(1+u)` to the probability weights `kp_k/chi`. Their
mean value of `k-1` is `kappa/chi`. It gives

\[
1-F(1-\eta)\ge
\frac{\chi\eta}{1+(\kappa/\chi)\eta},\qquad
\eta_{\ell+1}^{-1}\le
\chi^{-1}\eta_\ell^{-1}+\kappa\chi^{-2}.
\]

Solving the last linear inequality gives (10). Positivity of `eta_l`
follows since (4) has positive mass at positive degrees. This also proves
that (10) does not assume an unstated finite-width Gram event.

For a fixed subcritical `0<chi<1`, a polynomial bound on the inverse
population gap is generally false. Take two input vectors with inner
product `c` in `[0,1)`. Then their gap is
`delta_L=1-K_L(c)`. Since `F'<=chi` on `[0,1]`,
`0<delta_(l+1)<=chi delta_l`. Also `F(c)>c` for `c<1`, because
`1-F(c)<=chi(1-c)<1-c`. Taylor expansion at one gives

\[
\delta_{\ell+1}=\chi\delta_\ell
 -\frac\kappa2\delta_\ell^2+o(\delta_\ell^2).
\]

It follows that `delta_L/chi^L` tends to a finite strictly positive
constant depending on the activation and `c`: each ratio
`delta_(l+1)/(chi delta_l)=1+O(delta_l)` is positive, and the sum of
`delta_l` is finite, so the product of the ratios has a positive limit.
Thus the inverse gap grows exponentially for this elementary data set.

These formulas quantify what “near one” must mean when depth is allowed
to vary. For a family of activations with uniformly bounded `kappa`:

* If `|chi-1|<=C/L` and `L>=2C`, then
  `e^(-2C)<=chi^L<=e^C` and `S_L<=Le^C`. Equation (9) gives bounded
  first-derivative second moment and a second-derivative second moment
  of order at most `1+L`. Equation (10) gives an inverse gap of order
  at most `gamma_0^(-1)+L`, with constants depending on `C` and `kappa`.
* If `|chi-1|<=C log(L)/L` and this tolerance is at most `1/2`, then
  `L^(-2C)<=chi^L<=L^C`, `S_L<=L^(C+1)`, and both (9) and the inverse
  of (10) have polynomial bounds. For instance the inverse gap is at
  most `L^(2C)(gamma_0^(-1)+2 kappa L)`.

The inequalities use `log(1+u)<=u` and
`log(1-u)>=-2u` for `0<=u<=1/2`. The last gap bound also uses
`chi^(-L)S_L=sum_(r=1)^L chi^(-r)`.
For an exact first-tangent target `chi^L<=M`, the equivalent condition
is `log chi<=log(M)/L`; for `chi^L<=L^p`, it is
`log chi<=p log(L)/L`. A fixed activation has a fixed `chi`; it does
not satisfy a shrinking tolerance at every depth unless `chi=1`.
No assertion here bounds other activation constants by these two moments.

## 4. Explicit unbounded, nonlinear and variance-stable activations

Let

\[
\psi(z)=\operatorname{erf}(z/\sqrt2)
=\sqrt{\frac2\pi}\int_0^z e^{-u^2/2}\,du,
\qquad g(z)=\alpha z+\psi(z),\qquad \alpha>0.
\tag{11}
\]

The parameter `alpha` is fixed. The function is entire, odd, strictly
increasing on the real line, globally Lipschitz there, and unbounded.
Define the explicit positive constants

\[
\begin{aligned}
Q&=\alpha^2+\frac{2\alpha}{\sqrt\pi}+\frac13,\\
D&=\alpha^2+\frac{2\alpha}{\sqrt\pi}+\frac2{\pi\sqrt3},\\
N&=\alpha^2+\frac{3\alpha}{2\sqrt\pi}+\frac1{\pi\sqrt3}.
\end{aligned}
\tag{12}
\]

For any `0<chi<=D/Q`, take either sign in

\[
s=\sqrt{\chi/D},\qquad
b=\pm\sqrt{1-\chi Q/D},\qquad
\phi_\chi(z)=s g(z)+b.
\tag{13}
\]

Both signs coincide when `chi=D/Q`. The parameter interval includes one
strictly in its interior since `D-Q=2/(pi sqrt(3))-1/3>0`. The resulting
activation is nonlinear and unbounded at every fixed `alpha>0` and
`chi>0`, and it satisfies exactly

\[
\mathbb E\phi_\chi(Z)^2=1,\qquad
\mathbb E\phi_\chi'(Z)^2=\chi.
\tag{14}
\]

To verify all the constants, let `k=sqrt(2/pi)`, so
`psi'(z)=k e^(-z^2/2)` and `psi''(z)=-kz e^(-z^2/2)`.
Gaussian integration gives `E psi'(Z)=1/sqrt(pi)`,
`E psi'(Z)^2=2/(pi sqrt(3))`, and Gaussian integration by parts gives
`E[Z psi(Z)]=1/sqrt(pi)`. Also
`psi(Z)=2 Phi(Z)-1` is uniform on `(-1,1)`, hence
`E psi(Z)^2=1/3` and `E psi(Z)=0`. Expansion of `g^2` and `g'^2`
proves `E g(Z)^2=Q` and `E g'(Z)^2=D`, proving (14).

The correlation map and curvature are

\[
\begin{aligned}
F(c)&=1-\frac{\chi Q}{D}
 +\frac\chi D\left[
 \left(\alpha^2+\frac{2\alpha}{\sqrt\pi}\right)c
 +\frac2\pi\arcsin(c/2)\right],\\
F'(c)&=\frac\chi D\left[
 \alpha^2+\frac{2\alpha}{\sqrt\pi}
 +\frac2{\pi\sqrt{4-c^2}}\right],\\
\kappa=F''(1)&=\frac{2\chi}{3\pi\sqrt3 D}.
\end{aligned}
\tag{15}
\]

For derivation, Gaussian integration by parts gives
`E[X psi(Y)]=c/sqrt(pi)`. At fixed equal marginal variance `q`,
differentiate `E psi(X)psi(Y)` in the covariance `c`. Differentiating
the Gaussian density and integrating twice by parts gives

\[
\frac d{dc}\mathbb E[\psi(X)\psi(Y)]
=\mathbb E[\psi'(X)\psi'(Y)]
=\frac2{\pi\sqrt{(1+q)^2-c^2}}.
\]

Diagonalizing the covariance matrix evaluates the last Gaussian integral.
At `c=0` the expectation is zero by oddness and independence. Integrating
from zero to `c` proves `(2/pi)arcsin(c/(1+q))`, including degenerate
endpoints by bounded dominated convergence. For `q=1` this gives (15).
Bounded real derivatives justify the Gaussian differentiations on the
nondegenerate interval. Finally
`E[Z^2 e^(-Z^2)]=1/(3 sqrt(3))` verifies the curvature in (15)
directly from `phi''`.

The entire real variance map is explicit:

\[
V(q):=\mathbb E\phi_\chi(\sqrt q Z)^2
=b^2+\frac\chi D\left[
\alpha^2q+2\alpha\sqrt{\frac2\pi}\frac q{\sqrt{1+q}}
 +\frac2\pi\arcsin\frac q{1+q}\right],\qquad q\ge0.
\tag{16}
\]

The cross term follows from
`E[sqrt(q)Z psi(sqrt(q)Z)]=q E psi'(sqrt(q)Z)`; the last term
was just derived. Differentiating (16) at one gives

\[
V(1)=1,\qquad a:=V'(1)=\frac{\chi N}{D},\qquad 0<a<1.
\tag{17}
\]

The strict upper bound holds throughout the full interval in (13):

\[
a\le\frac NQ<1,
\quad Q-N=\frac\alpha{2\sqrt\pi}+\frac13-\frac1{\pi\sqrt3}>0.
\]

Thus the deterministic variance fixed point is locally attracting: by
continuity of `V'`, it has a neighborhood with `|V'|<=a_*<1`, and
`|V(q)-1|<=a_*|q-1|` keeps that neighborhood invariant. In particular
local variance stability does not require a subcritical angular gain.
The signs of `b` give the same maps (15)--(16), since the odd part has
zero Gaussian mean at each real variance.

The complex-strip hypothesis in the earlier unbounded-activation source
also holds quantitatively. For any strip width `w>0`,

\[
\sup_{|\operatorname{Im}z|<w}|\phi_\chi'(z)|
\le\sqrt{\chi/D}\left(\alpha+\sqrt{2/\pi}\,e^{w^2/2}\right).
\tag{18}
\]

This follows from `|e^(-(x+iy)^2/2)|=e^(-x^2/2+y^2/2)`.
All real derivatives of positive order are bounded. The bound in (18)
is an actual strip bound and is not replaced by the root-mean-square
quantity `sqrt(chi)`.

## 5. What real variance stability says about finite width

For a fixed input define
`q_(n,l)=n^(-1)||h^(l)||^2`, with `q_(n,0)=1`, and put
`H(z)=phi_chi(z)^2`. Fresh Gaussian rows give exactly the scalar Markov
transition law

\[
q_{n,\ell}\ \stackrel{\rm law}{=}
\frac1n\sum_{i=1}^n H(\sqrt{q_{n,\ell-1}}Z_{\ell i}),
\tag{19}
\]

with a fresh independent standard Gaussian array at each layer. Let
`sigma^2=Var(H(Z))`, which is finite and strictly positive. Positivity
follows since a continuous function with square constant one would be
constant, whereas `phi_chi'` is strictly positive.

For each fixed `L`,

\[
\sqrt n(q_{n,L}-1)\ \Longrightarrow
N\left(0,\sigma^2\sum_{j=0}^{L-1}a^{2j}\right),\qquad
\lim_{n\to\infty}n\operatorname{Var}(q_{n,L})
=\sigma^2\frac{1-a^{2L}}{1-a^2}.
\tag{20}
\]

Here is a short proof with the moment issue included. Let
`eta_(n,l)=sqrt(n)[q_(n,l)-V(q_(n,l-1))]`. On every compact interval
of variances around one, the centered summands in (19) have uniformly
bounded third moments. Taylor's formula for their characteristic functions
therefore gives, conditionally on preceding layers,

\[
\mathbb E[e^{it\eta_{n,\ell}}\mid\mathcal F_{n,\ell-1}]
=\exp\{-t^2\operatorname{Var}(H(\sqrt{q_{n,\ell-1}}Z))/2
 +O_t(n^{-1/2})\}.
\]

The variance in this expression is continuous in `q`. Inductively the
preceding fluctuation is tight, so `q_(n,l-1)->1` in probability.
The conditional characteristic functions then converge in probability
and, being bounded, in `L^1` to that of `N(0,sigma^2)`. Conditioning
the joint characteristic function proves that each limiting innovation
is independent of the preceding limiting fluctuations. Differentiability
of `V` at one gives

\[
\sqrt n(q_{n,\ell}-1)
=a\sqrt n(q_{n,\ell-1}-1)+\eta_{n,\ell}+o_{\mathbb P}(1).
\]

Indeed the Taylor remainder is the preceding tight fluctuation times
a function tending to zero. This proves the first limit in (20) by
induction and the characteristic-function continuity criterion.

For the second limit, `H''=2[(phi')^2+phi phi'']` is globally bounded:
`phi` has linear growth and `phi''` is a polynomial times a decaying
Gaussian. Gaussian integration by parts consequently gives a global
Lipschitz bound on `V`. Also `H(sqrt(q)Z)<=C(1+qZ^2)` implies
`sup_n E q_(n,l)^4<infinity` at every fixed depth. The fourth moment
of a normalized sum of centered independent summands is
`n^(-1)E X^4+3(1-n^(-1))(E X^2)^2`, bounded here by `C(1+q^4)`.
It follows that each innovation has bounded fourth moment. The global
Lipschitz bound on `V` and induction now bound the fourth moment of each
`sqrt(n)(q_(n,l)-1)`. This is uniform integrability of their squares,
so their means and variances converge to those of the displayed Gaussian.
This proves the second limit. Its coefficient is bounded over depth by
`sigma^2/(1-a^2)`, but the proof itself still takes width to infinity at
each fixed depth.

## 6. Exact complex moments and the depth-dependent query radius

For this section use the explicit family (13). Let
`U=X+iY`, with independent centered real Gaussians satisfying

\[
\operatorname{Var}(X)=(r+1)/2,\qquad
\operatorname{Var}(Y)=(r-1)/2,\qquad 1\le r<2.
\]

Thus `E U^2=1` and `E|U|^2=r`. The exact identities are

\[
\mathbb E\phi_\chi(U)^2=1,\qquad
\mathbb E|\phi_\chi(U)|^2=F(r),\qquad
\mathbb E|\phi_\chi'(U)|^2=F'(r),
\tag{21}
\]

where the explicit real formulas in (15) extend to `1<=r<2`.

For a direct proof, integrating `psi'` vertically gives

\[
|\psi(X+iY)|\le1+\sqrt{2/\pi}\,|Y|e^{-X^2/2+Y^2/2}.
\tag{22}
\]

On every compact subinterval of `r<2`, this bound and its differentiated
versions make the products used below integrable. The activation and its
fixed-order derivatives even have a uniformly finite moment of order
`2+epsilon` for some positive `epsilon`. If `G(X,Y)`
is any one of these functions, differentiating its Gaussian expectation
in `r` and integrating by parts gives
`d E G/dr=(1/4)E(Delta G)`: both component variances have derivative
`1/2`. For holomorphic `phi`, the Laplacian of `phi^2` is zero and
the Laplacian of `|phi|^2` is `4|phi'|^2`. This keeps the first moment
in (21) at its value one and identifies the derivative of the second.

The remaining derivative moment is an elementary integral. Absolute
integrability holds in the stated interval, and integration first in `X`
and then in `Y` gives `E e^(-U^2/2)=1/sqrt(2)`; explicitly the first
integration leaves
`(1+Var(X))^(-1/2) exp(Y^2/[2(1+Var(X))])`, and the second gives
`(1+Var(X)-Var(Y))^(-1/2)=1/sqrt(2)`. Also

\[
\mathbb E|e^{-U^2/2}|^2
=\mathbb E e^{-X^2+Y^2}=\frac1{\sqrt{4-r^2}}.
\]

Expanding `|s(alpha+sqrt(2/pi)e^(-U^2/2))|^2` therefore gives
exactly `F'(r)` in (15). Integrating from `r=1` proves the second
identity of (21). At `r>=2`, the derivative moment is infinite because
`E e^(Y^2)=infinity`. Adding the constant `alpha` cannot cancel this:
`|alpha+z|^2>=|z|^2/2-alpha^2`.

For the complex great-circle input
`x(i tau)=cosh(tau)e_1+i sinh(tau)e_2`, the first preactivation has
pseudo-second-moment one and Hermitian second moment `cosh(2tau)`.
Consequently the fixed-depth Gaussian initialization moment recursion is

\[
r_0=\cosh(2\tau),\qquad r_{j+1}=F(r_j),
\quad e_j=r_j-1,
\tag{23}
\]

as long as all required input moments satisfy `r_j<2`. Its
pseudo-second-moment remains one. At fixed depth, convergence of the
finite-network empirical complex moments follows from conditional Gaussian
rows and a truncated law of large numbers. To see why truncation is valid,
the limiting covariance parameters stay in a compact subset of the
strict integrability region; the `2+epsilon` bound after (22) persists
in a neighborhood of those parameters and makes the products uniformly
integrable. Conditional means are continuous there by domination, and
induction proves convergence. No assertion is made once a necessary
Gaussian moment is lost. Finite networks remain entire functions of the
input even when these limiting Gaussian derivative moments diverge.
This is convergence in probability after restricting preceding empirical
covariances to high-probability integrability neighborhoods. It does not
assert finiteness or convergence of the unconditional finite-width complex
second moments: rare covariance realizations are not controlled by this
argument.

Define

\[
B=\frac{24\chi}{7\pi\sqrt7 D}.
\tag{24}
\]

From (15), `F''(r)=(chi/D)(2/pi)r/(4-r^2)^(3/2)` is increasing on
`[1,2)`. Thus `F''(r)>=kappa` there and `F''(r)<=B` on `[1,3/2]`.
Taylor's formula gives

\[
e_{j+1}\ge\chi e_j+\frac\kappa2e_j^2,
\quad\text{and if }0\le e_j\le\tfrac12,\quad
e_{j+1}\le\chi e_j+\frac B2e_j^2.
\tag{25}
\]

Here is a quantitative sufficient radius. If

\[
e_0\le\min\left\{
\frac1{4\max(1,\chi^L)},\ \frac\chi{4BS_L}\right\},
\tag{26}
\]

then

\[
e_j\le2\chi^j e_0\le\tfrac12\quad(0\le j\le L),\qquad
\chi^L\le\prod_{j=0}^{L-1}F'(r_j)
\le e^{1/2}\chi^L.
\tag{27}
\]

To prove the first part, set `u_j=e_j/chi^j`. Assuming the stated
bound through layer `j`, (25) gives
`u_(j+1)<=u_j+(B/(2chi))chi^j u_j^2`. Summing these increments and
using `u_j<=2e_0` gives
`u_(j+1)<=e_0+(2B/chi)e_0^2 S_L<=3e_0/2`.
The first condition of (26) ensures every required `e_j<=1/2`, so
the induction is valid. Finally
`chi<=F'(1+e_j)<=chi+B e_j`. Taking logarithms and summing gives
the product bound because
`(B/chi)sum e_j<=2Be_0 S_L/chi<=1/2`.
This product is the derivative of the scalar Hermitian moment recursion;
it is not an arbitrary trained response norm.

There is also a matching necessary scale. Suppose `tau!=0`, `L>=2`,
and the derivative moments through all `L` activation layers are finite,
so `0<e_j<1` for `0<=j<=L-1`. From the lower bound in (25),

\[
\frac1{\chi e_j}-\frac1{e_{j+1}}
\ge\frac{\kappa}{2\chi(\chi+\kappa e_j/2)}
\ge\frac{\kappa}{2\chi(\chi+\kappa/2)}.
\]

Multiply the rearranged inequality by `chi^(j+1)` and sum from
`j=0` through `L-2`. Positivity of the final reciprocal gives

\[
e_0<\frac{2\chi+\kappa}{\kappa S_{L-1}},\qquad
|\tau|<\sqrt{\frac{2\chi+\kappa}{2\kappa S_{L-1}}},
\tag{28}
\]

where the second inequality uses `cosh(2tau)-1>=2tau^2`.

For fixed `alpha>0` and `chi` in any fixed compact subinterval of
`(0,D/Q]` containing one, (26) is implied by
`e_0<=c_alpha/S_L` with the explicit constant
`c_alpha=min{1/[4 max(1,D/Q)], 7 pi sqrt(7)D/96}`.
Indeed `B/chi` is constant in this family and
`max(1,chi^L)<=max(1,D/Q)S_L`. For `|tau|<=1/2`, the power series
gives `cosh(2tau)-1<=4tau^2`, so a sufficiently small constant times
`S_L^(-1/2)` suffices. Conversely (28) bounds every admissible radius
by a constant times `S_(L-1)^(-1/2)`. These sums are comparable for
`L>=2` when `chi` lies in that compact interval, since
`S_L=1+chi S_(L-1)`.

The complex Gaussian derivative-moment radius is therefore of order
`S_L^(-1/2)`, with constants depending on `alpha` and that compact
interval. At exact criticality it is of order `L^(-1/2)`. For a fixed
`chi>1` it is of order `chi^(-L/2)`. Under `|chi-1|<=C/L`, it remains
of order `L^(-1/2)`; under `|chi-1|<=C log(L)/L`, its reciprocal is
at most polynomial in depth. A fixed subcritical `chi<1` instead admits
a depth-independent small complex moment radius, while its two-point
population inverse gap still grows exponentially as in Section 3.

## 7. Exact scope and remaining obligations

The family (13) supplies an explicit unbounded analytic activation with
unit forward scale, a tunable derivative gain around one, finite explicit
curvature, stable real variance, and a fully computed complex moment map.
It does not require small output magnitude or a linear activation. All
derived initialization statements are valid at each fixed depth, with
the width limit specified before any subsequent depth comparison.

Smooth global Lipschitz continuity and (2), by themselves, do not imply
finite `kappa`, a complex analytic extension, or bounds on all response
orders. The curvature conclusions assumed (5), and the complex conclusions
used the specific entire family with its displayed integrability bounds.
For example an entire real Lipschitz function may have a rapidly growing
second derivative; analyticity alone cannot replace these checks.

The canonical network's zero initialized readout gives identically zero
prediction initially, regardless of the feature geometry. A compressor may
also retain the reference initialization. Consequently the exponential
feature derivative in (9), inverse gap behavior in Section 3, and shrinking
complex moment radius are not prediction-error or compression lower bounds.

An all-time autonomous theorem for the trained dense network still needs
control of the actual evolving joint law, mixed query/training responses,
all required higher moments, the whole query sphere, the trained Gram gap,
and the perturbation/stability error of the proposed compressed dynamics.
Neither (17) nor (27) supplies those missing trained estimates. In
particular, the initialized Gaussian derivative second moment cannot be
substituted for a pathwise strip bound or for an adaptive trained moment.
No universal depth-polynomial all-time theorem is proved or disproved here.

Status: complete author derivation, with no independent reconstruction yet.
No experiment or Git mutation was performed. The source-input SHA-256 values
read for this scoped continuation were:

* `CRITICAL_NORMALIZATION_GEOMETRY_ROUTE.md`:
  `410da51621c61e2f4b5785b6a26c24a3d4c3c3464a2599daf65aaed17b5b3d6e`.
* `NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md`:
  `8368603ca1a6bd449dc478810befce7aa62dc8cc1dc05869c9a68114a19599ef`.
* `NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md`:
  `1e14c318bb8352007c8326d601cd654b865cf40c71d7f0156c2d50305510b4b8`.
* `NORMALIZED_VARIANCE_FLUCTUATIONS_ROUTE.md`:
  `2debe995c6f02d92f26f992a6c9d643fa4ef0c2bcf72ec63ed2068ac984d2406`.
