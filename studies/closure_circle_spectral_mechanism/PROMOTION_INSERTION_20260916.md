**Order, angular symmetry, and the closure's own tangent kernel.**
In this remark write \(p=N\ge1\) for closure order, \(P_1,P_2\) for
the numbers of quadrature particles, \(n\) for neural width, and \(d=2\)
for input dimension. This local \(p\) denotes order; the numerical theorem
below retains its separate precision symbol \(p\). Order limits, particle
refinement, precision and time discretization are different operations.
The statements below concern the exact finite closure equations and one
explicitly conditional symmetric population version. They add no neural
limit or longer-horizon approximation assertion. The underlying neural
model remains bias-free two-hidden-layer tanh, with stored Gaussian
variances \((1,1/n,1/n^2)\), mobilities \((n,1,n)\), unhalved
probability-weighted squared loss and physical time. Its finite random
readout is not set to zero; the closure's prescribed initial readout is zero.

Here is a self-contained finite-node form of the closure. Fix bounded mark
columns \(b_i\in\mathbb R^{r_1}\), \(\beta_j\in\mathbb R^{r_2}\),
and strictly positive weights \(\pi_i,\rho_j\), each population's weights
summing to one. Zero-weight nodes may be omitted. Write \(E_1,E_2\)
for these two weighted sums. The moving coordinates are
\(w_i\in\mathbb R^2\), \(c_j\in\mathbb R\), and
\(M\in\mathbb R^{r_2\times r_1}\). For \(u=x/\sqrt2\in S^1\), set
\[
\begin{aligned}
 h_i(u)&=\tanh(w_i\cdot u),& a(u)&=E_1[b h(u)],\\
 H_j(u)&=\tanh(\beta_j^TMa(u)),&f(u)&=E_2[cH(u)],\\
 s_i(u)&=1-h_i(u)^2,&
 \mathbf d(u)&=E_2[\beta c(1-H(u)^2)],\\
 q_i(u)&=b_i^TM^T\mathbf d(u).
\end{aligned}                                                    \tag{H3.CS1}
\]
Thus \(\mathbf d\) is the backward coefficient vector called \(d(u)\)
in (H3.N2), not input dimension. For any fixed probability law
\(\mu\) on \(S^1\times[-Y,Y]\), \(Y<\infty\), write
\(r(u,y)=f(u)-y\). The exact equations are
\[
\dot w_i=-2\int r s_iq_i u\,d\mu,\qquad
\dot c_j=-2\int r H_j\,d\mu,\qquad
\dot M=-2\int r\mathbf d a^T\,d\mu.                    \tag{H3.CS2}
\]
They are gradient flow of \(\mathcal L=\int r^2d\mu\) for the
constant state metric
\[
 \|\delta(w,c,M)\|^2
 =\sum_i\pi_i|\delta w_i|^2+
   \sum_j\rho_j|\delta c_j|^2+\|\delta M\|_F^2.          \tag{H3.CS3}
\]
In stored Euclidean node coordinates the inverse metric therefore has
mobilities \(1/\pi_i\), \(1/\rho_j\), and one, respectively. No extra
particle factor or change of physical time is implicit.

**Fixed order is not an angular cutoff.** The order-\(p\) dictionary of
part B restricts the fixed initialized-mark features used in \(M\).
The moving node values \(w,c\) remain unrestricted; they are not
degree-\(p\) polynomials in those marks. At any finite represented state,
oddness of tanh gives successively
\[
 h_i(-u)=-h_i(u),\quad a(-u)=-a(u),\quad
 H_j(-u)=-H_j(u),\quad f(-u)=-f(u).
\]
This uses no symmetry of the marks, weights, data law or trajectory. With
\(u(\theta)=(\cos\theta,\sin\theta)\) and the convention
\(\widehat f_k=(2\pi)^{-1}\int_0^{2\pi}f(u(\theta))e^{-ik\theta}d\theta\),
splitting the integral into two half-circles yields
\[
 \widehat f_k=\frac{1-(-1)^k}{2\pi}
       \int_0^\pi f(u(\theta))e^{-ik\theta}d\theta.
                                                               \tag{H3.CS4}
\]
Every even coefficient vanishes, including the mean.

There is nevertheless no finite odd-frequency cutoff imposed by \(p\).
To see this for any fixed finite dictionary here, its first raw feature is
the constant one. If \(LL^T=G+\eta I\), \(\eta>0\), and
\(b=L^{-1}\psi\), the first normalized feature is the constant
\((1+\eta)^{-1/2}\); the same holds in the upper population. Hence
\(v_0=E_1[b]\ne0\) and every \(\beta_j\ne0\). Choose one upper node
\(j_0\), put \(w_i=R(1,0)\) for every \(i\), and set
\[
 M=\frac{A\beta_{j_0}v_0^T}{|\beta_{j_0}|^2|v_0|^2},\qquad
 c_{j_0}=\rho_{j_0}^{-1},\quad c_j=0\ (j\ne j_0),\qquad R,A>0.
\]
Then (H3.CS1) represents exactly
\[
 F_{R,A}(\theta)=\tanh\!\big(A\tanh(R\cos\theta)\big).    \tag{H3.CS5}
\]
For finite positive \(R,A\), this is not a trigonometric polynomial.
Indeed it is even in \(\theta\), so any finite trigonometric
representation would be a finite cosine sum and hence a polynomial
\(P(\cos\theta)\), by the recurrence
\(\cos((k+1)\theta)=2\cos\theta\cos(k\theta)-\cos((k-1)\theta)\).
We would have \(P(x)=\tanh(A\tanh(Rx))\) on \([-1,1]\).
Both sides are real analytic on \(\mathbb R\); equality on an interval
extends across this connected line. Explicitly, at a finite endpoint of
an interval of equality all derivatives of the difference vanish by
continuity, and its convergent Taylor series extends that interval.
The right side is bounded on \(\mathbb R\) and has derivative \(AR>0\)
at zero. A bounded real polynomial is constant, a contradiction.

More specifically, fix any positive odd integer \(k\). As \(R\to\infty\),
\(F_{R,A}\to\tanh(A)\operatorname{sign}(\cos\theta)\) except at the two
zeros of cosine, and \(|F_{R,A}|\le1\). Dominated convergence in the
Fourier integral gives the nonzero limiting cosine coefficient
\[
 \lim_{R\to\infty}\frac1\pi\int_0^{2\pi}
           F_{R,A}(\theta)\cos(k\theta)d\theta
 =\frac{4\tanh A}{\pi k}\sin(k\pi/2)\ne0.                \tag{H3.CS6}
\]
Here the integral over the positive half-circle is
\(2\sin(k\pi/2)/k\), and the integral over the negative half-circle is
its negative. Thus that coefficient is nonzero at some finite \(R\),
while \(p\) is unchanged. These are statements about represented states.
They do not say that prescribed-initialization training reaches these
states or selects any specified odd coefficients.

**Conditional parity equivalence of orders one and two.** The exact
symmetry relevant to this comparison is reversal of initialization marks,
which is distinct from reversal of the input. For completeness the core
marks are
\[
 X=(\tanh g_1,\tanh g_2,\tanh(\zeta_1+\alpha\tanh g_1),
          \tanh(\zeta_2+\alpha\tanh g_2)),\qquad
 Z=(\tanh\xi_1,\tanh\xi_2),
\]
where \(g_1,g_2\) are independent standard Gaussians,
\(\zeta\sim N(0,\tau I_2)\) is independent of \(g\), and the separate
upper population has \(\xi\sim N(0,v I_2)\). With a standard scalar
Gaussian \(G\), the constants are
\[
 v=E\tanh^2G,\qquad \tau=E\tanh^2(\sqrt vG),\qquad
 \alpha=E[1-\tanh^2(\sqrt vG)].
\]
All are finite and positive. Sign reversal \(S_1(g,\zeta)=(-g,-\zeta)\)
or \(S_2\xi=-\xi\) preserves its population law and reverses every
component of \(X\) or \(Z\).

At \(p=1,2\), the raw lists \(\psi_1,\psi_2\) consist of all
total-degree-at-most-\(p\) Chebyshev products in \(X,Z\), respectively,
in total degree and then descending lexicographic order. The constant
is first; there are no added nonconstant word features at these two orders.
Use the *same* positive ridge \(\eta\) at both orders and the same
coefficient integration rule. Define \(b=L_1^{-1}\psi_1\),
\(\beta=L_2^{-1}\psi_2\), with
\(L_\ell L_\ell^T=E[\psi_\ell\psi_\ell^T]+\eta I\).
The initialized core contraction and middle matrix are
\[
 \begin{split}
 C={}&E_2[\nabla_\xi\psi_2]\,
                E_1[\psi_1(\tanh g)^T]^T
       +E_2[\psi_2(\tanh\xi)^T]\,
                E_1[\nabla_\zeta\psi_1]^T,\\
 D={}&L_2^{-1}CL_1^{-T}.
 \end{split}                                                   \tag{H3.CS7}
\]
Gradients here are feature-by-two matrices. This is the explicit core
initialization (H3.1); for the symmetry argument (H3.CS7) itself specifies
the contraction, so no Gaussian-action or neural-limit theorem is needed.

Assume both coefficient integration and population evolution preserve the
two sign reversals exactly. This holds for the exact Gaussian expectations,
or for finite rules whose nodes occur with their reversed nodes at equal
weights. In the latter case all core constants, nodes and weights are
identical across the two orders; coefficient and evolution rules may be
different from each other, but each must have the stated symmetry.
Start with \(w(0)=g,c(0)=0,M(0)=D\). For the continuum version assume
existence and uniqueness on the interval in question in a characteristic
class with bounded \(w-g,c,M\), fixed bounded features, and the displayed
expectations. No uniqueness of a more general formal population solution
is asserted. The finite-rule conclusion holds on every common interval of
existence of its smooth ordinary differential equations.

Here is the invariant-subsystem proof. Chebyshev recurrence implies
\(T_j(-x)=(-1)^jT_j(x)\); a product of total degree \(j\) therefore
has parity \((-1)^j\). An integral of an odd function of the full marks
is zero, by substituting \(S_\ell\). Opposite-parity raw Gram entries
vanish, as do the cross-parity entries of its Cholesky factor: in the
recurrence for \(L_{ij}\), a potentially nonzero product \(L_{ik}L_{jk}\)
requires both \(i,k\) and \(j,k\) to have equal parity, and therefore
requires \(i,j\) to have equal parity. Induction on columns proves the
claim; positive ridge makes every diagonal pivot positive. Its inverse
also preserves parity.

For an even lower feature, its product with \(\tanh g\) is odd and
its \(\zeta\)-derivatives are odd. Both corresponding rows in (H3.CS7)
therefore vanish. The same reasoning applies to even upper features,
using \(\xi\)-derivatives and \(\tanh\xi\). Thus \(D\) has only an
odd-to-odd block. Consider states with \(w\circ S_1=-w\),
\(c\circ S_2=-c\), and \(M\) supported in that block. Then \(h\) is
odd in lower marks, \(a\) has only odd coordinates, \(H\) is odd in
upper marks, and its gate \(1-H^2\) is even. Consequently \(\mathbf d\)
has only odd coordinates and \(q\) is odd in lower marks. Formula
(H3.CS2) makes \(\dot w\) odd, \(\dot c\) odd, and \(\dot M\)
odd-to-odd. The restricted equations thus solve the full equations;
uniqueness gives preservation from the prescribed initialization.
For finite rules, local uniqueness follows by the integral-map contraction
on a small time interval: the finite vector field is smooth and hence
Lipschitz on each closed bounded neighborhood. In the stated continuum
characteristic class the same contraction works in the supremum norm of
\((w-g,c)\) and the matrix norm: bounded features and the Lipschitz
functions tanh and \(1-\tanh^2\) bound every product and integral on
bounded sets. Starting Picard iteration in the displayed linear parity
subspace keeps every iterate there; its closedness keeps the local
solution there. Repeat on successive intervals of existence.

Order two adds only degree-two even features. Its active odd lists and
their ordering equal those at order one. The common ridge and integration
rule give identical active Cholesky factors, identical active \(D\), and
identical active initial node values. In (H3.CS2), inactive coordinates
remain zero and the surviving equations coincide. Uniqueness therefore
gives identical predictions at the two orders under precisely these
matched assumptions. The maintained schedule instead gives
\(\eta_1=1/4096\) and \(\eta_2=1/9216\); its ordinary Halton-prefix
rules do not impose sign pairs. This conditional equality is consequently
not an equality or a small-error claim for default numerical runs.

**The evolving kernel and its frozen comparator.** At a finite state,
ordinary partial derivatives in stored coordinates are
\[
 \partial_{c_j}f(u)=\rho_jH_j(u),\qquad
 \partial_M f(u)=\mathbf d(u)a(u)^T,\qquad
 \partial_{w_i}f(u)=\pi_iq_i(u)s_i(u)u.
\]
Contract these derivatives using the inverse metric (H3.CS3), or substitute
(H3.CS2) in the chain rule. For any query \(u\),
\[
 \dot f(u)=-2\int K_t(u,v)r(v,y)\,d\mu(v,y),\qquad
 K_t=K_c+K_M+K_w,                                      \tag{H3.CS8}
\]
where
\[
 \begin{split}
 K_c(u,v)&=E_2[H(u)H(v)],\\
 K_M(u,v)&=[\mathbf d(u)^T\mathbf d(v)][a(u)^Ta(v)],\\
 K_w(u,v)&=(u\cdot v)E_1[q(u)q(v)s(u)s(v)].
 \end{split}                                                   \tag{H3.CS9}
\]
These are Gram kernels with features, respectively,
\((\sqrt{\rho_j}H_j(u))_j\), the entries of
\(\mathbf d(u)a(u)^T\), and the concatenated vectors
\((\sqrt{\pi_i}q_i(u)s_i(u)u)_i\). Every finite Gram matrix is
positive semidefinite, since its quadratic form is the squared Euclidean
norm of the corresponding linear combination of features.
Differentiation under the data integral is valid locally: finite states,
bounded input and labels, and the bounded tanh gates bound all its
integrands on a time neighborhood. Thus
\[
 \dot{\mathcal L}=-4\iint r(u,y)K_t(u,v)r(v,z)
                   \,d\mu(u,y)d\mu(v,z)\le0.             \tag{H3.CS10}
\]
The sign also follows directly by writing the double integral as the
squared norm of the integral of the residual times each displayed feature.
It concerns exact gradient flow, not an arbitrary discrete Heun step.

At the closure initialization \(c=0\), \(\mathbf d=q=0\), so
\(K_M=K_w=0\) and \(K_0(u,v)=E_2[H_0(u)H_0(v)]\).
Freezing \(w,M\) at their own initial values and training only \(c\)
therefore gives exactly the linear prediction flow with this fixed
kernel and initial prediction zero. This comparator exists separately
at each \(p\); the maintained positive-order hierarchy has no order-zero
member. The projected finite closure kernel need not equal the full
Gaussian population kernel or be stationary on the input circle.
The identities give no universal improvement with order, learned
bandwidth law, nonlinear endpoint characterization, or new convergence
scope.
