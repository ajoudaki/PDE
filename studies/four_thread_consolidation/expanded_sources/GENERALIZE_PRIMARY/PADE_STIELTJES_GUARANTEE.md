# Explicit Padé and Borel–Padé uniform guarantees

Prepared 2026-09-06. This note supplies sufficient conditions and complete proofs; it does not assert that the neural population kernel satisfies any Stieltjes condition.

Throughout, [p/q] means numerator degree at most p and denominator degree at most q, with denominator normalized to 1 at the origin. Some older papers reverse this convention.

## 1. Compactly supported Stieltjes functions: explicit uniform rate

Let μ be a finite positive measure supported in [0,R], with R>0 and mass m₀. Put

\[
F(t)=\int_{[0,R]}\frac{d\mu(x)}{1+tx},\qquad
m_p=\int x^p\,d\mu(x).
\]

The Taylor coefficients at 0 are c_p=(-1)^p m_p. For infinite support, its [M−1/M] Padé approximant exists for every M≥1 and has the form

\[
R_M(t)=\sum_{j=1}^M\frac{w_j}{1+t x_j},
\quad 0<x_j<R,\quad w_j>0,\quad\sum_jw_j=m_0.
\]

The x_j,w_j are the M-point Gaussian quadrature nodes and weights for μ. Only moments m₀,…,m_(2M−1), equivalently the first 2M Taylor coefficients, are needed. There are no poles on [0,∞). For every T<∞,

\[
\sup_{0\le t\le T}|F(t)-R_M(t)|
\le 2m_0\left(\frac{RT}{2+RT}\right)^{2M}.
\tag{1}
\]

Thus for any ε>0, a finite M suffices on any prescribed compact positive interval, even when T exceeds the radius of the original Taylor expansion. When μ has finitely many support points, its Stieltjes transform is already rational and the hierarchy terminates with exact recovery (allowing deficient degrees).

**Proof of the quadrature and Padé assertions.** Form the monic orthogonal polynomial p_M of degree M. It is determined by its M orthogonality equations against 1,x,…,x^(M−1), whose coefficients involve precisely moments through degree 2M−1. Positive definiteness of the moment matrix follows because a nonzero polynomial cannot vanish on infinite support.

The usual sign-change argument puts M distinct roots x_j in the interior of the convex hull of the support: if there were fewer sign-changing roots there, multiply p_M by the product of their linear factors. The resulting integrand has constant sign and is nonzero on a positive-mass set, while orthogonality says its integral is zero. This contradiction supplies all M distinct roots.

Let ℓ_j be the Lagrange polynomial of degree M−1 at these roots and set w_j=∫ℓ_j dμ. For every polynomial p of degree at most 2M−1, divide p=q p_M+r with deg q,deg r≤M−1. Orthogonality kills the q p_M integral, and interpolation of r gives

\[
\int p\,d\mu=\sum_jw_jp(x_j).
\]

Apply this identity to ℓ_j²: w_j=∫ℓ_j²dμ>0. Apply it to 1 to obtain the mass identity. Expanding each 1/(1+tx_j) formally at zero shows that R_M matches coefficients through degree 2M−1, hence is [M−1/M]. Its rational numerator and denominator have the stated degree bounds. The nodes are positive, so all poles lie on the negative real axis.

**Proof of (1).** For t≥0, put a=1+tR/2 and y=t(x−R/2)/a. Then |y|≤q_t=tR/(2+tR)<1, and the degree-(2M−1) polynomial

\[
p_t(x)=a^{-1}\sum_{j=0}^{2M-1}(-y)^j
\]

satisfies

\[
\sup_{x\in[0,R]}\left|\frac1{1+tx}-p_t(x)\right|
\le\frac{q_t^{2M}}{a(1-q_t)}=q_t^{2M}.
\]

Quadrature is exact for p_t. Integrate the error against μ and the quadrature measure, each of mass m₀, to get 2m₀q_t^(2M). Maximizing over t≤T proves (1).

The quadrature–Padé correspondence is classical; an original reference is Allen, Chui, Madych, Narcowich and Smith, [“Padé approximation and gaussian quadrature”](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/133CD9E0E6960B585002005424549ADA/S0004972700043641a.pdf/pade-approximation-and-gaussian-quadrature.pdf), Bulletin of the Australian Mathematical Society 11 (1974), 63–69. The elementary rate (1) is derived here rather than quoted.

## 2. Zero Taylor radius is also compatible with uniform Padé convergence

Let μ instead be a finite positive measure on [0,∞), with every moment finite, and assume its Stieltjes moment problem is determinate: no other positive measure on [0,∞) has the same moments. Define F and R_M exactly as above using Gaussian quadrature. Then

\[
\sup_{0\le t\le T}|F(t)-R_M(t)|\longrightarrow0
\quad\text{for every finite }T.
\tag{2}
\]

No positive Taylor radius is assumed.

**Proof including the endpoint t=0.** Let μ_M=∑w_jδ_(x_j). Its mass is m₀, and for M≥1 its first moment is m₁. The bound μ_M([A,∞))≤m₁/A gives tightness. Every subsequence has a further weakly convergent subsequence. For each fixed integer p≥1, quadrature eventually matches both moments p and p+1, and

\[
\int_{x>A}x^p\,d\mu_M\le m_{p+1}/A.
\]

This uniform tail estimate allows the p-th moment to pass to the weak limit. Mass passes by tightness. Every such limit therefore has the moments of μ, and determinacy identifies it with μ. Thus μ_M converges weakly to μ.

For every t>0, x↦1/(1+tx) is bounded and continuous, so R_M(t)→F(t). At t=0 they agree exactly. Finally,

\[
|R_M(t)-R_M(s)|\le m_1|t-s|,
\qquad |F(t)-F(s)|\le m_1|t-s|
\]

for nonnegative s,t. A finite mesh of [0,T] and these common Lipschitz bounds upgrade pointwise convergence to uniform convergence. This proves (2).

A convenient sufficient condition for Stieltjes moment determinacy is Carleman's condition

\[
\sum_{p=1}^{\infty}m_p^{-1/(2p)}=\infty.
\tag{3}
\]

In particular, m_p≤C^(p+1)(2p)! suffices. This version and the corresponding Padé convergence statements are recorded in Borghi and Weniger, [“Convergence Analysis of the Summation of the Euler Series by Padé Approximants and the Delta Transformation”](https://arxiv.org/pdf/1405.2474), §3.1, equations (3.7)–(3.8). The uniform inclusion of t=0 in (2) was proved directly above.

**Example: the Euler series.** Take μ(dx)=e^(−x)dx. Then

\[
F(t)=\int_0^\infty\frac{e^{-x}}{1+tx}\,dx,
\qquad F(t)\sim\sum_{p=0}^{\infty}(-1)^pp!t^p.
\]

Differentiation under the integral gives F^(p)(0)=(-1)^p(p!)², as right derivatives. The formal Taylor series diverges for every t>0. Nevertheless, m_p=p! satisfies (3), and the genuine [M−1/M] Padé approximants converge uniformly on every [0,T]. Here F is smooth from the right at 0 but is not analytic there.

Its ordinary Borel transform is especially simple:

\[
\mathcal B F(\xi)=\sum_{p\ge0}(-1)^p\xi^p=\frac1{1+\xi}.
\]

Its [0/1] Padé approximant is already exact, and Borel–Laplace inversion recovers F:

\[
F(t)=\int_0^\infty e^{-u}\,\mathcal B F(tu)\,du.
\]

Thus this one example has both direct Padé recovery and Borel–Padé recovery despite zero Taylor radius.

## 3. Explicit Borel–Padé uniform recovery when the transform is Stieltjes

Suppose the formal coefficients a_p have a generalized Borel transform

\[
B(\xi)=\sum_{p\ge0}\frac{a_p}{\Gamma(1+\sigma p)}\xi^p
=\int_{[0,R]}\frac{d\mu(x)}{1+\xi x},\qquad \sigma>0,
\]

where μ is positive and finite. Assume the target function is identified with the corresponding Borel sum,

\[
F(t)=\int_0^\infty e^{-u}B(tu^\sigma)\,du.
\tag{4}
\]

This identification is a substantive assumption if F was originally defined by another problem. Conditions on jets alone cannot exclude an added function flat at zero.

Let B_M=[M−1/M]_B and define

\[
F_M(t)=\int_0^\infty e^{-u}B_M(tu^\sigma)\,du.
\]

Only a₀,…,a_(2M−1) enter B_M. Positivity gives 0≤B,B_M≤m₀ on the whole positive ray. For every U>0,

\[
\sup_{0\le t\le T}|F(t)-F_M(t)|
\le 2m_0\left[
\left(\frac{RTU^\sigma}{2+RTU^\sigma}\right)^{2M}
+e^{-U}\right].
\tag{5}
\]

Indeed, split the Laplace integral at U. On [0,U] apply (1) with argument bound TU^σ; on (U,∞) use |B−B_M|≤2m₀. Choose U large enough for the tail, then M large enough for the first term. This proves uniform recovery on every finite [0,T], with an explicit finite-order choice.

For example, for 0<ε<4m₀, choose U=log(4m₀/ε). If RT>0, it suffices to choose

\[
M\ge
\frac{\log(4m_0/\varepsilon)}
{2\log\!\left((2+RTU^\sigma)/(RTU^\sigma)\right)}.
\]

The formula includes exact integration of a rational transform. F_M is a Borel–Padé approximation; it is generally not itself rational in t and need not be a Padé approximant to the original series. If a finite rational expression in t is desired, cut the integral at U and use finite positive quadrature there. Uniform continuity of (t,u)↦e^(−u)B_M(tu^σ) on [0,T]×[0,U] gives uniform quadrature convergence. The resulting finite sum is rational in t, with no nonnegative poles, but is not in general a classical Padé approximant to the original series.

There is also a direct Padé consequence under a moderate exponent. By Tonelli, (4) is itself the Stieltjes transform of the measure obtained by sending (x,u) to xu^σ under μ(dx)e^(−u)du. Its moments are

\[
\Gamma(1+\sigma p)m_p\le m_0R^p\Gamma(1+\sigma p).
\]

If 0<σ≤2, condition (3) follows from Stirling's formula, because the Carleman terms are bounded below by a constant times p^(−σ/2). Thus direct [M−1/M] Padé approximants to the original formal series also converge uniformly on every [0,T]. For σ>2, this sufficient argument stops; (5) still proves Borel–Padé convergence under the stated transform and identification assumptions.

## 4. An explicit coefficient condition for the compact-support hypothesis

Write b_p=a_p/Γ(1+σp). For a declared R>0 put s_p=(-1)^p b_p/R^p. The condition

\[
\sum_{j=0}^k(-1)^j\binom{k}{j}s_{p+j}\ge0
\quad\text{for all integers }p,k\ge0
\tag{6}
\]

is equivalent to existence of a finite positive measure ν on [0,1] with s_p=∫x^p dν(x). This is the Hausdorff moment criterion. Scaling ν by x↦Rx gives exactly the compactly supported Stieltjes representation for B above. The mass is s₀=b₀. The zero-mass case gives the identically zero transform.

For a primary modern mathematical source, see Liu and Pego, [“On generating functions of Hausdorff moment sequences”](https://arxiv.org/abs/1401.8052), or Diaconis and Freedman, [“The Markov moment problem and de Finetti's theorem: Part I”](https://www.stat.berkeley.edu/users/freedman/631.pdf), Theorem 1. In (6), positivity follows in the forward direction by integrating x^p(1−x)^k. The reverse direction is Hausdorff's theorem.

This is an all-orders condition, not a finite collection of successful sign tests. It proves a structural sufficient condition for the transform, but it still does not by itself identify a separately specified population-GF observable with its Borel sum.
