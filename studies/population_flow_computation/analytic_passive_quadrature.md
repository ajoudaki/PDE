# Passive Gaussian quadrature at a saved finite source state

Date: 2026-09-12. Author: scoped agent `/root/passive_quadrature_bound`.
Scientific input scope: the supervisor's self-contained assignment only. No
repository scientific sources, saved arrays, trajectories, or experimental results
were read or generated. Shared instructions and the required proof/research skills
were read. Numerical clues subsequently supplied by the supervisor are not inputs
to any statement or proof below.

Claim type: exact deterministic inequalities under the stated assumptions.
Check status: complete derivation with an author audit; awaiting the supervisor's
check against the established source definitions. This is study material, not an
independent review or a promoted result.

The result bounds only replacement of a one-dimensional Gaussian expectation by
exact Gauss--Hermite quadrature at one saved source state. It is uniform in all the
saved means. A residual norm estimate then extends a variance grid to the whole
input circle. There is no assertion about the accuracy of that source state as an
approximation to any other dynamics or population object.

## Statement and finite certificate

Let \(P,q\geq1\) be integers, \(G\sim N(0,1)\), and let

\[
 Q_q f=\sum_{j=1}^q\lambda_j f(x_j),\qquad
 \lambda_j>0,\qquad \sum_j\lambda_j=1,
\]

be a quadrature rule with \(q\) distinct real nodes that is exact on every
polynomial of degree at most \(2q-1\) for the law of \(G\). This fixes the
**standard-normal normalization**; nodes for the weight \(e^{-x^2}\) must first
be multiplied by \(\sqrt2\) and their weights divided by \(\sqrt\pi\).

Let \(c_i\in\mathbb R\), let \(m_i(u)\in\mathbb R\) be arbitrary for
\(u\in S^1=\{u\in\mathbb R^2:|u|=1\}\), and let \(\sigma(u)\geq0\). Define

\[
 F(u)=\frac1P\sum_{i=1}^P c_i\,\mathbb E\tanh(m_i(u)+\sigma(u)G),
\]
\[
 F_q(u)=\frac1P\sum_{i=1}^P c_i\sum_{j=1}^q
 \lambda_j\tanh(m_i(u)+\sigma(u)x_j),\qquad
 C=\frac1P\sum_{i=1}^P|c_i|.
\]

For every \(0<r<\pi/2\), put \(A(r)=\max\{1,\tan r\}\). Then

\[
 |F(u)-F_q(u)|
 \leq C\min\left\{2,\ q!A(r)
           \left(\frac{\sigma(u)}r\right)^{2q}\right\}.
 \tag{1}
\]

The two explicit choices requested by the assignment are

\[
 |F(u)-F_q(u)|\leq Cq!
       \left(\frac{4\sigma(u)}\pi\right)^{2q},
 \qquad r=\pi/4,
 \tag{2}
\]
\[
 |F(u)-F_q(u)|\leq Cq!\tan(3/2)
       \left(\frac{2\sigma(u)}3\right)^{2q},
 \qquad r=3/2<\pi/2.
 \tag{3}
\]

For a whole-circle certificate, suppose the saved state supplies fixed vectors
\(w_i\in\mathbb R^2\) and a fixed orthogonal projection \(\Pi\) in the
real source Hilbert space, with

\[
 h_u(i)=\tanh(w_i\cdot u),\qquad
 \|h\|^2=\frac1P\sum_{i=1}^P h(i)^2,\qquad
 \sigma(u)=\|(I-\Pi)h_u\|,
\]
\[
 W=\left(\frac1P\sum_{i=1}^P|w_i|^2\right)^{1/2}.
\]

Let \(M\geq1\), let \(u_k=(\cos(2\pi k/M),\sin(2\pi k/M))\) for
\(0\leq k<M\), and set

\[
 \overline\sigma
 =\min\left\{1,\ \max_{0\leq k<M}\sigma(u_k)
                 +2W\sin\frac{\pi}{2M}\right\}.
 \tag{4}
\]

Here \(\sigma\) is the residual **standard deviation**. If the saved grid
contains variances \(v_k=\sigma(u_k)^2\), its contribution to (4) is
\(\max_k\sqrt{v_k}\), with \(v_k\geq0\) in exact arithmetic.

Then \(\sigma(u)\leq\overline\sigma\) for every \(u\in S^1\). For any
nonempty finite set \(\mathcal R\subset(0,\pi/2)\), an explicitly finite
scalar certificate is

\[
 \sup_{u\in S^1}|F(u)-F_q(u)|
 \leq C\min\left\{2,
       q!\min_{r\in\mathcal R}
       \left[A(r)\left(\frac{\overline\sigma}{r}\right)^{2q}\right]
       \right\}.
 \tag{5}
\]

For example, \(\mathcal R=\{\pi/4,3/2\}\) retains both (2) and (3).
No optimization, new source evolution, or evaluation of the means is required.
All factors depend only on the integer \(q\), saved coefficient magnitudes,
saved source weights, the finite residual grid, and the specified strip radii.

The proof first establishes the Gaussian polynomial norm, then proves a
pointwise interpolation remainder and integrates it. A strip estimate supplies
the derivative constant; projection geometry supplies (4).

## Gaussian quadrature remainder, including the unbounded domain

Write \(\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). Define

\[
 H_n(x)=(-1)^n\varphi(x)^{-1}\varphi^{(n)}(x),\qquad n\geq0.
\]

From \(\varphi'=-x\varphi\), differentiation gives

\[
 H_0=1,\qquad H_{n+1}=xH_n-H_n'.
\]

Induction shows that \(H_n\) is a real monic polynomial of degree \(n\), and
every derivative of \(\varphi\) is a polynomial times \(\varphi\).
Every polynomial is integrable against \(\varphi(x)\,dx\): for each finite
degree \(d\), \(|x|^d e^{-x^2/4}\) is bounded, so a degree-\(d\) polynomial
times \(e^{-x^2/2}\) is bounded in magnitude by a constant times
\(e^{-x^2/4}\). The same observation shows that polynomial multiples of
derivatives of \(\varphi\) vanish at both infinities.

For any real polynomial \(p\), integration by parts \(n\) times therefore gives
the identity

\[
 \mathbb E[H_n(G)p(G)]=\mathbb E[p^{(n)}(G)].
 \tag{6}
\]

All boundary terms vanish by the preceding Gaussian decay. Consequently
\(H_n\) is orthogonal to every polynomial of degree below \(n\), and, because
the \(n\)-th derivative of a monic degree-\(n\) polynomial is \(n!\),

\[
 \mathbb E H_n(G)^2=n!.
 \tag{7}
\]

Now let \(R_q(x)=\prod_{j=1}^q(x-x_j)\). If \(\deg p\leq q-1\), moment
exactness and the zero values of \(R_q\) at the nodes give

\[
 \mathbb E[R_q(G)p(G)]=Q_q(R_qp)=0.
\]

Both \(R_q\) and \(H_q\) are monic of degree \(q\). Their difference \(d\)
has degree at most \(q-1\), so

\[
 \mathbb E d(G)^2
 =\mathbb E[R_q(G)d(G)]-\mathbb E[H_q(G)d(G)]=0.
\]

A nonzero real polynomial is nonzero on some open real interval, which has
positive Gaussian measure. Thus the last identity implies \(d=0\). This proves
directly from the supplied moment conditions that

\[
 R_q=H_q,\qquad \mathbb E R_q(G)^2=q!.
 \tag{8}
\]

Let \(f\in C^{2q}(\mathbb R)\) have bounded \(2q\)-th derivative and be
Gaussian integrable. There is a unique polynomial \(I_f\) of degree at most
\(2q-1\) satisfying

\[
 I_f(x_j)=f(x_j),\qquad I_f'(x_j)=f'(x_j),\qquad 1\leq j\leq q.
\]

Indeed, the linear map from that \(2q\)-dimensional polynomial space to these
\(2q\) values has trivial kernel: a polynomial in its kernel has a double zero
at every \(x_j\), hence is divisible by the degree-\(2q\) polynomial \(R_q^2\)
and must vanish. A linear injective map between equal finite dimensions is
surjective as well.

Fix a real \(x\notin\{x_1,\ldots,x_q\}\) and put

\[
 a=\frac{f(x)-I_f(x)}{R_q(x)^2},\qquad
 g(t)=f(t)-I_f(t)-aR_q(t)^2.
\]

On the compact interval spanning \(x,x_1,\ldots,x_q\), the function \(g\)
has double zeros at the \(q\) nodes and a further zero at \(x\). Repeated
Rolle arguments imply that \(g^{(2q)}(\xi)=0\) somewhere in that interval.
For completeness, if a differentiable function has distinct zeros with total
multiplicity \(N\), its derivative retains one less multiplicity at each
multiple zero and has one additional zero between each two consecutive
distinct zeros by Rolle's theorem. The derivative therefore has at least
\(N-1\) zeros counted with these multiplicities. Iterating this argument from
\(N=2q+1\) proves the asserted \(2q\)-th derivative zero. Only derivatives
through order \(2q\) are required.

Since \(I_f^{(2q)}=0\) and \((R_q^2)^{(2q)}=(2q)!\), we have

\[
 a=\frac{f^{(2q)}(\xi)}{(2q)!},\qquad
 |f(x)-I_f(x)|
 \leq\frac{\|f^{(2q)}\|_\infty}{(2q)!}R_q(x)^2.
 \tag{9}
\]

At a node the same inequality holds because both sides vanish. It consequently
holds for every real \(x\), with no bounded-domain or Gaussian-tail assumption.
The polynomial \(I_f\) is Gaussian integrable, and the majorant in (9) is
integrable by (8). Since \(I_f\) agrees with \(f\) at every node and has degree
at most \(2q-1\),

\[
 Q_qf=Q_qI_f=\mathbb E I_f(G).
\]

Taking the Gaussian integral of (9) now proves the needed remainder bound:

\[
 \left|\mathbb Ef(G)-Q_qf\right|
 \leq\frac{q!}{(2q)!}\|f^{(2q)}\|_\infty.
 \tag{10}
\]

This argument never chooses a common unknown intermediate point outside a
finite interval, and never interchanges an unbounded-domain limit with a
quadrature remainder.

## Uniform derivative bound for the shifted and scaled hyperbolic tangent

The zeros of \(\cosh z\) are \(z=i(\pi/2+\pi k)\), \(k\in\mathbb Z\):
the equation is equivalent to \(e^{2z}=-1\). Therefore \(\tanh z\) is
holomorphic throughout \(|\operatorname{Im}z|<\pi/2\).
For real \(x,y\) in this strip,

\[
 |\tanh(x+iy)|^2
 =\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}.
 \tag{11}
\]

If \(|y|\leq\pi/4\), the ratio is at most \(1\). If
\(\pi/4<|y|<\pi/2\), writing \(t=\sinh^2x\geq0\) shows that
\((t+\sin^2y)/(t+\cos^2y)\) decreases with \(t\), and its largest value
is \(\tan^2y\) at \(t=0\). Since \(\tan\) increases on \([0,\pi/2)\),

\[
 \sup_{x\in\mathbb R,\ |y|\leq r}|\tanh(x+iy)|\leq A(r),
 \qquad 0<r<\pi/2.
 \tag{12}
\]

The elementary Cauchy derivative formula used here says that if \(g\) is
holomorphic on a neighborhood of the closed disk \(|z-x|\leq r\), then

\[
 g^{(n)}(x)=\frac{n!}{2\pi i}
       \int_{|z-x|=r}\frac{g(z)}{(z-x)^{n+1}}\,dz.
\]

For every real center \(x\), the closed radius-\(r\) disk is inside the
pole-free strip, with positive distance to its boundary, so this formula
applies to \(g=\tanh\). Taking absolute values and using the circumference
\(2\pi r\) and (12) gives

\[
 \sup_{x\in\mathbb R}|\tanh^{(n)}x|
 \leq n!A(r)r^{-n}.
 \tag{13}
\]

For fixed \(m\in\mathbb R\) and \(\sigma\geq0\), the function
\(f(x)=\tanh(m+\sigma x)\) is bounded and smooth. The chain rule and (13)
give

\[
 \|f^{(2q)}\|_\infty
 \leq\sigma^{2q}(2q)!A(r)r^{-2q}.
\]

Substitution into (10) proves, uniformly in the real shift \(m\),

\[
 \left|\mathbb E\tanh(m+\sigma G)
     -\sum_j\lambda_j\tanh(m+\sigma x_j)\right|
 \leq q!A(r)(\sigma/r)^{2q}.
 \tag{14}
\]

At \(\sigma=0\), both averages equal \(\tanh m\) because the weights sum
to one; thus (14) includes this case exactly. Positivity and normalization of
the weights also keep both averages in \([-1,1]\), giving the bound \(2\).
Multiplying each instance of (14) by \(|c_i|/P\), summing, and using the
triangle inequality proves (1), including arbitrary signs of the \(c_i\).
The independence of the bound from \(m_i(u)\) means that no regularity or
grid control of those means is needed.

For fixed \(q,r\), the new bound is \(O(\sigma^{2q})\) as
\(\sigma\downarrow0\). To compare its order with a generic Lipschitz
transport bound, let \(Z\) have masses \(\lambda_j\) at \(x_j\), and let
\(d_q\) be the infimum of \(\mathbb E|G-Z|\) over all couplings of these
two laws. The real derivative bound \(|\tanh'|\leq1\) gives

\[
 |\mathbb Ef(G)-\mathbb Ef(Z)|\leq\sigma\,d_q.
\]

This follows for each coupling by the pointwise Lipschitz inequality and then
by taking the infimum. The constant \(d_q\) is finite using the independent
coupling, and it is strictly positive because
\(|G-Z|\geq\min_j|G-x_j|\), whose Gaussian expectation is positive for a
finite node set. Hence (14) is strictly smaller than this generic bound for
all sufficiently small positive \(\sigma\), for every fixed \(q\geq1\).
No transport theorem is needed for this comparison.

## Extending the variance grid to the circle

An orthogonal projection satisfies

\[
 \|(I-\Pi)v\|^2=\|v\|^2-\|\Pi v\|^2\leq\|v\|^2.
\]

The reverse triangle inequality and this contraction property imply

\[
 |\sigma(u)-\sigma(v)|
 \leq\|(I-\Pi)(h_u-h_v)\|\leq\|h_u-h_v\|.
\]

The real derivative \(\tanh' x=\operatorname{sech}^2x\) lies in \([0,1]\).
The mean value theorem and the Euclidean Cauchy--Schwarz inequality therefore
give

\[
 \|h_u-h_v\|^2
 \leq\frac1P\sum_i|w_i\cdot(u-v)|^2
 \leq W^2|u-v|^2.
 \tag{15}
\]

Every point on the circle has a grid node whose shortest angular separation
is at most \(\pi/M\). Points separated by an angle \(\theta\in[0,\pi]\)
have Euclidean distance \(\sqrt{2-2\cos\theta}=2\sin(\theta/2)\).
Consequently

\[
 \sigma(u)\leq\max_k\sigma(u_k)
                  +2W\sin\frac{\pi}{2M}.
\]

Also \(\sigma(u)\leq\|h_u\|\leq1\), since each \(|h_u(i)|\leq1\).
This proves (4), including \(M=1\) and \(W=0\). For every chosen \(r\),
the right side of (14) is nondecreasing in \(\sigma\geq0\). Substitute
\(\overline\sigma\), take the finite minimum over radii, and then use the
coefficient triangle inequality to obtain (5).

## Optional strip choice and arithmetic implementation

The factor \(A(r)/r^{2q}\) decreases on \((0,\pi/4]\). On
\((\pi/4,\pi/2)\), its logarithmic derivative is

\[
 \frac1{\sin r\cos r}-\frac{2q}r,
\]

whose sign is the sign of \(r-q\sin(2r)\). The latter expression is
strictly increasing there because its derivative is
\(1-2q\cos(2r)>0\). At \(r=\pi/4\) it equals \(\pi/4-q<0\), and
as \(r\uparrow\pi/2\) it tends to \(\pi/2>0\). Thus the unique optimal
radius lies in \((\pi/4,\pi/2)\) and solves

\[
 r_q=q\sin(2r_q).
\]

This optimization is optional: every explicitly chosen admissible radius
already yields a valid bound, and a finite minimum avoids any assumption about
root-finding accuracy. The choice \(r=3/2\) is one such fixed radius.

If \(C=0\) or \(\overline\sigma=0\), the certificate is exactly zero.
Otherwise each positive candidate can be evaluated without forming a large
factorial using

\[
 \log\big[Cq!A(r)(\overline\sigma/r)^{2q}\big]
 =\log C+\sum_{k=1}^q\log k+\log A(r)
       +2q(\log\overline\sigma-\log r).
\]

The \(2C\) cap can likewise be applied in logarithmic form. This is an
evaluation prescription, not a floating-point error bound.

If exact residuals are replaced by certified intervals
\(|\widehat\sigma_k-\sigma(u_k)|\leq\delta_k\) and \(W\leq\overline W\),
the same proof permits

\[
 \overline\sigma
 =\min\left\{1,\ \max_k(\widehat\sigma_k+\delta_k)
                 +2\overline W\sin\frac{\pi}{2M}\right\}.
\]

Without such validated enclosures, substitution of floating-point grid values
produces an evaluation of the analytic formula, not a machine-verified numerical
upper bound. The same distinction applies to coefficient magnitudes, the strip
constants, nodes, weights, residual projection, and summation.

## Scope and retained limitations

- The reference \(F\) is the Gaussian expectation defined at the **same fixed
  saved source state** as \(F_q\). The result does not bound source discretization,
  population approximation, time stepping, model identification, or accumulated
  dynamical error. No trajectory was computed or certified.
- The whole-circle bound requires the stated residual identity and a single fixed
  orthogonal projection. If the projection changes with the input, (15) alone
  no longer proves the asserted Lipschitz bound for the residual norm.
- The quadrature proof assumes exact real nodes and positive weights with exact
  polynomial moments. Rounded numerical rules require separate numerical error
  control. The standard-normal normalization is essential for the factor \(q!\).
- This is a small-residual, fixed-\(q\) certificate. For a fixed positive
  \(\sigma\), the factorial bound need not improve as \(q\) increases and does
  not itself prove convergence as \(q\to\infty\). For a fixed radius its ratio
  at successive orders is \((q+1)(\sigma/r)^2\), which eventually exceeds one.
- The coefficient factor \(C\), source scale \(W\), and residual grid are retained
  finite-state information. The proof does not claim a dimension bound independent
  of the saved source population \(P\), an autonomous closure, or a certificate
  independent of unavailable source information.

Author checks performed on this derivation: Gaussian normalization and the
identity \(\mathbb EH_q^2=q!\); all Hermite interpolation degrees and zero
multiplicities; integrability on the full real line; the strip constant on both
sides of \(r=\pi/4\); arbitrary real shifts and signed coefficients; the cases
\(\sigma=0\), \(C=0\), \(q=1\), \(M=1\), and \(W=0\); chord-distance constants;
and the separation between exact arithmetic and numerical evaluation. For
\(q=1\), \(H_1(x)=x\) and (10) reduces to
\(|\mathbb Ef(G)-f(0)|\leq\|f''\|_\infty/2\), confirming the normalization.
No experiment or numerical source evaluation forms part of these checks.
