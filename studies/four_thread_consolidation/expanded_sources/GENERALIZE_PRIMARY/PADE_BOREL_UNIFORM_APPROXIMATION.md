# Uniform approximation from initialization jets: Padé and Borel

Date: 2026-09-06. This note gives sufficient theorems and distinguishes them
from the still-open neural reconstruction assumptions. It does not assert
that the population kernel has a Stieltjes representation or is Borel summable.

## 1. The approximation problem

Write the initialization expansion of a scalar observable as
\(F(t)\sim\sum_{p\ge0}a_p t^p\), where \(a_p=F^{(p)}(0)/p!\) if the
actual derivatives exist. A normalized Padé approximant of type [L/M] is
\(P_L/Q_M\), with degree bounds L,M and Q_M(0)=1, satisfying the formal
condition

\[
Q_M(t)\sum_{p\ge0}a_p t^p-P_L(t)=O(t^{L+M+1}).
\]

Thus its coefficients are obtained from finitely many initialization
coefficients, not positive-time samples. Normalized approximants need not
exist for every table entry; rational degeneracies also need care. The
positive-measure constructions below avoid this problem (finite support
terminates in an exact rational function).

Every continuous function on [0,T] admits uniform polynomial approximation.
That statement neither promises approximation by its Taylor truncations nor
by its one-point Padé table. For a smooth flat function, all initialization
coefficients can vanish although the function is nonzero at positive time.
All its normalized one-point Padé approximants are zero. Some identification
of the actual function by its jet is therefore indispensable.

## 2. A quantitative genuine Padé theorem

Suppose

\[
F(t)=\int_{[0,R]}\frac{d\mu(x)}{1+tx},\qquad
\mu\ge0,\quad m_0=\mu([0,R])<\infty,\quad R>0.
\]

Its coefficients are \(a_p=(-1)^p m_p\), with
\(m_p=\int x^p d\mu(x)\). Assume first that the support is infinite.
The M-node Gaussian quadrature rule for this measure has positive weights
\(w_j\), nodes \(x_j\in[0,R]\), and is exact for polynomials through
degree 2M-1. Define

\[
R_M(t)=\sum_{j=1}^M\frac{w_j}{1+tx_j}.
\]

It is the [M-1/M] Padé approximant: the numerator has degree at most M-1,
the denominator at most M, and exactness of moments 0 through 2M-1 gives
formal agreement through degree 2M-1. These moments determine the orthogonal
polynomial, quadrature nodes and weights. Every pole is negative, so there
are no poles on [0,infinity).

For every finite T,

\[
\sup_{0\le t\le T}|F(t)-R_M(t)|
\le 2m_0\left(\frac{RT}{2+RT}\right)^{2M}.                 (1)
\]

Proof of the error bound: expand the integrand in powers of x-R/2,

\[
\frac1{1+tx}=\frac1{1+tR/2}\frac1{1+t(x-R/2)/(1+tR/2)}.
\]

The inner ratio has absolute value at most q_t=tR/(2+tR)<1.
Its degree-(2M-1) geometric polynomial has uniform remainder at most
q_t^(2M), because (1+tR/2)(1-q_t)=1. Both integration against mu and
the quadrature have positive mass m_0 and agree on that polynomial. Their
difference is therefore bounded by twice m_0 times its remainder.

If the measure has finite support, its finite atomic formula is already
rational and the Padé sequence can be taken exact once the order reaches
the support size. The zero measure is trivial.

This is a concrete epsilon guarantee: for 0<epsilon<2m_0, any integer

\[
M\ge\frac{\log(2m_0/\varepsilon)}
 {2\log((2+RT)/(RT))}
\]

suffices. It is not restricted to RT<1. For example,
F(t)=log(1+t)/t (F(0)=1) comes from uniform measure on [0,1]; its Taylor
series cannot converge at t>1, while (1) holds on every finite [0,T].

The Padé/Gaussian quadrature identity is classical; see Allen, Chui, Madych,
Narcowich and Smith, [Padé approximation and Gaussian quadrature](https://doi.org/10.1017/S0004972700043641).
Bound (1) was derived explicitly above rather than inferred from an
unspecified convergence theorem.

## 3. A genuinely divergent Taylor series

Compact support is unnecessary for qualitative Stieltjes convergence if
the measure is uniquely determined by its moments. For a finite positive
measure on [0,infinity) with every moment finite and a determinate moment
problem, [M-1/M] Padé approximants converge to its Stieltjes integral at
positive t; the convergence is locally uniform away from the negative ray.
This is Theorem 6 in [Barry Simon's moment-problem paper](https://arxiv.org/pdf/math-ph/9906008).

Uniformity up to t=0 follows as well. Each positive quadrature measure has
mass m_0 and first moment m_1, so

\[
|R_M(t)-R_M(s)|\le m_1|t-s|,
\qquad |F(t)-F(s)|\le m_1|t-s|.
\]

Pointwise convergence and this common Lipschitz bound give uniform
convergence on [0,T] by a finite mesh argument. A sufficient determinacy
condition is Carleman's condition; the simpler moment bound
\(m_p\le C A^p p!\) also suffices (Simon, Proposition 1.5).

The explicit example

\[
F(t)=\int_0^\infty\frac{e^{-x}}{1+tx}\,dx
\sim\sum_{p\ge0}(-1)^p p!\,t^p
\]

has zero Taylor radius. Its right derivatives satisfy
F^(p)(0)=(-1)^p(p!)^2 by dominated differentiation. Its moments m_p=p!
obey the sufficient determinacy bound. Thus genuine ordinary Padé
approximants converge uniformly on every finite [0,T].

Its ordinary Borel transform is B(xi)=1/(1+xi), and
F(t)=integral_0^infinity e^(-u) B(tu)du. Padé in the Borel plane recovers
B exactly at type [0/1]. This example distinguishes direct Padé, which
approximates F by rational functions, from Borel-Padé, whose exact Laplace
integral need not be rational.

## 4. A general Borel-Padé transfer theorem

Suppose, for a fixed sigma>0, the ACTUAL function satisfies

\[
F(t)=\int_0^\infty e^{-u}B(tu^\sigma)du,
\quad B(\xi)=\sum_{p\ge0}\frac{a_p}{\Gamma(1+\sigma p)}\xi^p
\quad\hbox{near }0.                                      (2)
\]

Assume B continues along the positive ray, and for C>0 and b>=0,
\(|B(\xi)|\le C\exp(b\xi^{1/\sigma})\) there. Fix T with
lambda=1-b T^(1/sigma)>0. Let R_M be declared Padé approximants of B and
assume they converge uniformly on every finite positive-ray segment.

For a cutoff U define F_(M,U)(t)=integral_0^U e^(-u)R_M(tu^sigma)du.
Then directly subtracting (2) gives

\[
\sup_{t\le T}|F_{M,U}(t)-F(t)|
\le \sup_{0\le\xi\le TU^\sigma}|R_M(\xi)-B(\xi)|
 +\frac C\lambda e^{-\lambda U}.                         (3)
\]

Choose U first to control the tail, then M to control the compact
approximation. For these fixed U,M, finite quadrature approximates the
remaining integral uniformly in t: its integrand is continuous on the
compact rectangle [0,T]x[0,U]. A finite approximation is

\[
F_{M,U,J}(t)=\sum_{j=1}^J w_j R_M(tu_j^\sigma).
\]

It is rational in t and uses finite initialization data, with nodes/weights
chosen by a declared quadrature rule. It is generally not the direct
[L/M] Padé approximant of F: the Padé matching condition was imposed on B.

No common growth bound for R_M is needed for (3), because it is only
integrated up to U. If instead full Laplace integrals of R_M are desired,
it suffices to assume
\(|R_M(\xi)|+|B(\xi)|\le C e^{b\xi^{1/\sigma}}\) uniformly in M.
The same splitting proof then proves uniform convergence of the full
Laplace reconstructions.

## 5. Explicit sufficient structure for the Borel transform

If

\[
B(\xi)=\int_{[0,R]}\frac{d\nu(x)}{1+\xi x},\qquad \nu\ge0,
\]

then Section 2 applies to B, not necessarily to F. Its Padé approximants
and B are bounded between 0 and nu_0 on the entire positive ray. Consequently,
assuming the actual identity (2), for every finite T and every U>0,

\[
\sup_{t\le T}\left|\int_0^\infty e^{-u}R_M(tu^\sigma)du-F(t)\right|
\le 2\nu_0\left(\frac{RTU^\sigma}{2+RTU^\sigma}\right)^{2M}
 +2\nu_0 e^{-U}.                                         (4)
\]

This gives a finite epsilon guarantee, first choosing U and then M. It
allows original coefficients growing like Gamma(1+sigma p), hence zero
Taylor radius. It is stronger than mere convergence of the Borel series.

An explicit coefficient condition can imply this structure: let
\(m_p=(-1)^p a_p/\Gamma(1+\sigma p)\). Require both moment matrices
\((m_{i+j})_{i,j=0}^q\) and \((m_{i+j+1})_{i,j=0}^q\) to be positive
definite for every q, and a bound \(m_p\le C R^p\). The moment existence
theorem supplies a positive measure on [0,infinity); the growth bound
forces support in [0,R], since any mass above R would violate it at high
order. This proves the required representation of the analytic Borel germ.
Finite-support cases can be handled separately. All-order positivity is
essential: checking finitely many matrices does not certify the condition.
This condition does not itself identify F with (2).

There is also a direct bridge back to genuine Padé of F when
0<sigma<=2. Under (2) and the positive compact-support representation of B,
Tonelli's theorem gives

\[
F(t)=\int\!\int\frac{e^{-u}\,du\,d\nu(x)}{1+t u^\sigma x}
     =\int_{[0,\infty)}\frac{d\rho(v)}{1+tv},
\]

where rho is the pushforward under v=u^sigma x. Its moments are
\(\widetilde m_p=\Gamma(1+\sigma p)\int x^p d\nu(x)
\le\nu_0 R^p\Gamma(1+\sigma p)\).
Stirling's estimate yields
\(\widetilde m_p^{-1/(2p)}\ge c p^{-\sigma/2}\) for large p (zero moments are
trivial cases). Thus the Stieltjes Carleman series diverges for sigma<=2.
The representing measure is determinate, and Section 3 proves uniform
convergence of the genuine [M-1/M] Padé approximants of F on every [0,T].
For sigma>2 this particular determinacy argument gives no conclusion;
the Borel-Padé guarantee (4) remains valid under the same stated hypotheses.

## 6. Guarantees without a positive measure

For genuine ordinary Padé a different classical theorem is de Montessus:
if a germ extends meromorphically to |t|<r with exactly q poles counted
with multiplicity, then the fixed-denominator row [L/q] converges locally
uniformly away from those poles as L grows. This covers a real interval
[0,T] with T<r avoiding those poles, even if complex poles make the Taylor
radius smaller than T. It is not a theorem about arbitrary diagonals.

More general analytic-continuation theorems for diagonal Padé often yield
convergence in capacity, which does not bound the maximum error on a real
interval: a spurious pole can destroy that bound. Analyticity or Borel
summability alone should not be reported as a universal diagonal uniform
convergence theorem. Relevant sources and precise scope are collected in
PADE_ANALYTIC_GUARANTEES.md.

If a broader finite-jet rational method is acceptable, there is a simple
alternative without moment positivity. Suppose B is analytic in
Re xi>−a, a>0. Let

\[
w=\frac{\xi}{\xi+2a},\qquad
G(w)=B\left(\frac{2aw}{1-w}\right)=\sum_{p\ge0}g_p w^p.
\]

This maps the half-plane to the unit disk. The first M+1 coefficients of
G use only the first M+1 coefficients of B. The rational functions

\[
R_M(\xi)=\sum_{p=0}^M g_p\left(\frac{\xi}{\xi+2a}\right)^p
\]

converge uniformly on every finite [0,L]. In fact, q=L/(L+2a)<1, and for
any q<rho<1, Cauchy's coefficient bound gives

\[
\sup_{\xi\le L}|B(\xi)-R_M(\xi)|
\le\left(\max_{|w|=\rho}|G(w)|\right)
\frac{(q/\rho)^{M+1}}{1-q/\rho}.
\]

Together with (2), the true tail bound and cutoff transfer (3), this proves
uniform finite-jet rational approximation of F. These are conformal Taylor
rational approximants, not conventional [M/M] Padé: they match only M+1
coefficients rather than 2M+1. For a wider reconstruction framework see
Costin--Dunne, [Uniformization and Constructive Analytic Continuation of Taylor Series](https://arxiv.org/pdf/2009.01962), Theorem 8.

## 7. Consequence for the population GF program

Apply the above to the canonical one-input output-dependent kernel kappa,
or to a separately specified time-dependent prediction/kernel observable.
The scalar independent variable in the former application is the output
increment, not physical time; the prior local scalar comparison theorem
transfers uniform kernel accuracy to prediction/loss accuracy. Multiple
inputs require the separately stated matrix reconstruction hypothesis.

The GF theorem supplies the actual population target and its fixed
positive existence interval. To use Borel-Padé, one still needs: actual
all-order jets; identity of the population observable with its Borel sum;
continuation/growth; and a valid rational approximation mechanism. Positive
Stieltjes structure is one sufficient route, not a necessary assumption of
the earlier general conjecture and not an established property of our
nonlinear kernel. Known complex-domain analyticity plus a declared
conformal method offers another conditional route.

A theorem on each fixed [0,T], T<T_*, gives finite order for every desired
accuracy on that interval. The order may depend on T and accuracy but not
width or the vanishing GD step. Neither coefficient matching nor a stable
numerical Padé fit alone certifies these premises.

An independent mathematical check of the synthesis verified (1), (3),
(4), the coefficient criterion and the direct Padé consequence for
0<sigma<=2. The review requested explicitly b>=0 in the tail estimate;
that assumption is now stated above.
