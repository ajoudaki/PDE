# Analytic route: a proved scalar reduction and the missing approximation theorem

Status: scoped theoretical analysis, 2026-10-05. The input scope was the
assignment and `docs/notation.qmd`; no other study, archived book, experiment,
or realized dense trajectory was used. The investigate-conjectures and
solve-math-rigorously skills and their applicable contract/audit references
were read. The required canonical-notation skill was inaccessible at its
specified path (`Permission denied`), so the supervisor authorized the
explicit-notation fallback recorded here.

The results below are proved for **one training sample**, which is an
admissible special case of orthogonal training data. They do not establish the
requested construction for arbitrary fixed sample count. They isolate a
constructive approximation obligation, prove that all physical time is not
the remaining obstacle in this special case, and compute the first nonlinear
coefficient directly from the initialization law.

## 1. Exact reduction with width-independent bounds

Let the training sample be \((x_1,y)\), where
\(\|x_1\|_2=\sqrt d\). At any spherical test point \(x\),
\(\|x\|_2=\sqrt d\), the dense network is

\[
 u(x)=Ax/\sqrt d,\qquad h(x)=\tanh u(x),\qquad
 v(x)=Wh(x),\qquad g(x)=\tanh v(x),\qquad
 f_n(x)=w^Tg(x)/n.
\]

The loss is \((f_n(x_1)-y)^2\), and the block mobilities for
\((A,W,w)\) are \((n,1,n)\). Write \(u,h,v,g\) for training-point
coordinates. Initially \(w=0\), the entries of \(A\) are independent
\(\mathcal N(0,1)\), and the entries of \(W\) are independent
\(\mathcal N(0,1/n)\), with the two matrices independent.

Define a feature flow, with parameter \(s\in\mathbb R\), by

\[
 \frac{dw}{ds}=g,\qquad
 \frac{dW}{ds}=\frac{(w\odot\tanh'v)h^T}{n},\qquad
 \frac{dA}{ds}=
 [\tanh'u\odot W^T(w\odot\tanh'v)]\frac{x_1^T}{\sqrt d}.
 \tag{1}
\]

These equations are independent of the label. Put
\(F_n(s)=f_n(x_1;s)\) and \(Q_n(s,x)=f_n(x;s)\). The original
physical-time gradient flow is exactly (1) composed with

\[
 \frac{ds}{dt}=2\bigl(y-F_n(s)\bigr),\qquad s(0)=0.
 \tag{2}
\]

This follows by multiplying every equation in (1) by \(ds/dt\) and
substituting the gradient of the stated loss. It is an identity for the dense
network, not yet a compact implementation: evaluating its response functions
\(F_n,Q_n\) still uses the dense feature flow.

Hereafter assume \(\|W(0)\|_{\mathrm{op}}\le M\). Since
\(|\tanh|,|\tanh'|\le1\), integration of (1) gives

\[
 \|w(s)\|_\infty\le |s|,\qquad
 \|W(s)\|_{\mathrm{op}}\le M+s^2/2.
 \tag{3}
\]

For the first estimate, integrate \(w'=g\). For the second, the
operator norm of the rank-one derivative in (1) is at most
\(\|w\|_2\|h\|_2/n\le |s|\). Consequently, with
\(D(s)=\operatorname{diag}(\tanh'(u(s))^2)\),

\[
 \frac{du}{ds}=\tanh'u\odot W^T(w\odot\tanh'v),\qquad
 \frac{dv}{ds}=
 \left(\frac{\|h\|_2^2}{n}I+WDW^T\right)
 (w\odot\tanh'v).
 \tag{4}
\]

On \(|s|\le S\), put \(B=1+(M+S^2/2)^2\). Equations (3)--(4)
imply

\[
 \frac{\|u'(s)\|_2}{\sqrt n}\le (M+S^2/2)|s|,
 \qquad
 \frac{\|v'(s)\|_2}{\sqrt n}\le B|s|,
 \qquad
 \frac{\|g(s)-g(0)\|_2}{\sqrt n}\le Bs^2/2.
 \tag{5}
\]

The same bounds on every finite interval preclude finite-time blowup of (1):
the remaining first-weight components orthogonal to \(x_1\) are constant,
and all changing coordinates stay bounded on each finite interval. Thus its
locally unique smooth solution exists for every real \(s\).

Differentiating the training prediction and using (4) yields the exact
positive identity

\[
 F_n'(s)=\frac{\|g\|_2^2}{n}
 +\frac{(w\odot\tanh'v)^T
 [\|h\|_2^2 I/n+WDW^T]
 (w\odot\tanh'v)}{n}
 \ge \frac{\|g\|_2^2}{n}.
 \tag{6}
\]

Suppose \(\|g(0)\|_2^2/n\ge\kappa_* >0\), and choose \(S>0\)
so that \(BS^2\le\sqrt{\kappa_*}\). By (5),
\(\|g(s)\|_2/\sqrt n\ge\sqrt{\kappa_*}/2\) for \(|s|\le S\).
Hence

\[
 F_n'(s)\ge k:=\kappa_*/4\quad (|s|\le S).
 \tag{7}
\]

If \(|y|<kS\), there is one root \(s_*\in(-S,S)\) of
\(F_n(s_*)=y\). Equation (2) remains between \(0\) and \(s_*\), and

\[
 |s(t)-s_*|\le |s_*|e^{-2kt}.
 \tag{8}
\]

Indeed, \(F_n(0)=0\), and integration of (7) shows
\(F_n(S)\ge kS\), \(F_n(-S)\le-kS\). The scalar vector field in
(2) points toward its unique root. Subtracting its equilibrium equation and
using (7) gives the exponential estimate. This argument covers either sign
of \(y\).

The same construction controls the whole input sphere. Define
\(c=x_1^Tx/d\in[-1,1]\). Since the first-weight motion in (1) lies in
the training-input direction,

\[
 u(x;s)=u(x;0)+c\,[u(s)-u(0)].
 \tag{9}
\]

Combining (3), (5), and (9),
\(\|v'(x;s)\|_2/\sqrt n\le B|s|\), and therefore

\[
 |\partial_s Q_n(s,x)|
 \le \frac{\|w'\|_2\|g(x)\|_2}{n}
 +\frac{\|w\|_2\|v'(x)\|_2}{n}
 \le 1+BS^2=:L.
 \tag{10}
\]

No net over the input sphere was needed for this deterministic bound.

The initial event above has probability tending to one. A direct Gaussian
net argument gives a fixed admissible \(M\), for example \(M=8\): for
one-quarter nets of the two unit spheres, each with at most \(9^n\)
points, \(\|W\|_{\rm op}\) is at most twice the maximum bilinear form
over the nets. Each form has law \(\mathcal N(0,1/n)\), so the failure
probability is at most
\(2\exp[-(8-2\log9)n]\). Also
\(n^{-1}\|h(0)\|_2^2\) concentrates around
\(q=\mathbb E\tanh^2G>0\), where \(G\sim\mathcal N(0,1)\).
Conditionally on \(h(0)\), the coordinates of \(v(0)\) are independent
\(\mathcal N(0,\|h(0)\|_2^2/n)\). Bounded-variable concentration
then bounds \(\|g(0)\|_2^2/n\) away from zero. For example,
\(\kappa_*=(1/2)\mathbb E\tanh^2(\sqrt qG)\) is valid with
probability tending to one exponentially in \(n\).

## 2. An all-time approximation transfer, with the missing premise visible

Suppose one has **actually constructed**, without dense arrays or response
oracles, two finite descriptions \(P(s)\) and \(R(s,x)\) such that

\[
 \sup_{|s|\le S}|P(s)-F_n(s)|\le\varepsilon,
 \qquad
 \sup_{|s|\le S,\ \|x\|_2=\sqrt d}
 |R(s,x)-Q_n(s,x)|\le\varepsilon.
 \tag{11}
\]

Require the training decoder to agree exactly with the feedback function,
\(R(s,x_1)=P(s)\). Assume \(P\) is continuously differentiable with
\(P'\ge k/2\), and \(|y|+\varepsilon<kS\). Define the one-state
autonomous surrogate

\[
 \dot\sigma=2(y-P(\sigma)),\qquad \sigma(0)=0,\qquad
 f_{\rm small}(t,x)=R(\sigma(t),x).
 \tag{12}
\]

Because \(R(\sigma,x_1)=P(\sigma)\), its internal residual is exactly
its actual training prediction minus \(y\). It is also gradient flow of
\((P(\sigma)-y)^2\) with scalar mobility \(1/P'(\sigma)\), which is
positive and bounded above by \(2/k\). Thus the conditional construction
has an explicit training rule as well as an autonomous prediction rule.

The boundary signs implied by (11) keep \(\sigma\) inside \([-S,S]\).
For \(e=s-\sigma\), subtract (12) from (2) and use (7), obtaining the
upper right derivative estimate

\[
 D^+|e|\le -2k|e|+2\varepsilon.
\]

Multiplying by \(e^{2kt}\) and integrating gives
\(|e(t)|\le\varepsilon/k\). By (10)--(11),

\[
 \sup_{t\ge0,\ \|x\|_2=\sqrt d}
 |f_n(t,x)-f_{\rm small}(t,x)|
 \le (1+L/k)\varepsilon.
 \tag{13}
\]

Both scalar states converge to their unique equilibria, so (13) also holds
at the physical-time endpoint. Thus in the one-sample case, a uniform
response approximation on a fixed short feature interval would supply the
entire all-time claim, with no factor depending on the physical horizon.

Equation (11) is a **missing premise**, not a proved compact construction.
Taking \(P=F_n\) or defining \(P,R\) by a precomputed trajectory would
violate the assignment. This transfer result only separates error
production from error propagation.

## 3. First nonlinear coefficient, computed directly from the law

All quantities in this section are at \(s=0\). Put

\[
 q_n=\frac{\|h\|_2^2}{n},\quad
 D=\operatorname{diag}(\tanh'(u)^2),\quad
 b=g\odot\tanh'v,\quad
 \kappa_n=\frac{\|g\|_2^2}{n}.
\]

At initialization, \(w'=g\), whereas \(u'=W'=v'=0\). Equation (4)
therefore gives

\[
 v''=(q_nI+WDW^T)b,\qquad
 g''=\tanh'v\odot(q_nI+WDW^T)b.
\]

Uniqueness in (1) also gives the parity relations: \(w\) is odd in
\(s\), and \(A,W,h,v,g\) are even. Taylor expansion at fixed width yields

\[
 F_n(s)=\kappa_ns+c_ns^3+O_n(s^5),\qquad
 c_n=\frac{2}{3n}b^T(q_nI+WDW^T)b.
 \tag{14}
\]

The subscript on the remainder is essential: a width-uniform fifth-order
bound has **not** been proved here. The factor \(2/3\) is the sum of
\(1/2\) from \(w'(0)^Tg''(0)\) and \(1/6\) from
\(w'''(0)^Tg(0)\).

The limiting coefficient is computable from one-dimensional Gaussian
integrals. Define

\[
 \begin{aligned}
 G&\sim\mathcal N(0,1),\qquad q=\mathbb E\tanh^2G,\qquad
 Z\sim\mathcal N(0,q),\\
 a&=\mathbb E\tanh'(G)^2,
 &q_D&=\mathbb E[\tanh^2G\,\tanh'(G)^2],\\
 b(z)&=\tanh z\,\tanh'z,
 &\beta&=\mathbb E b(Z)^2,\qquad
 \zeta=\mathbb E b'(Z).
 \end{aligned}
\]

Then

\[
 \kappa_n\longrightarrow\kappa:=\mathbb E\tanh^2Z,
 \qquad
 c_n\longrightarrow c_3:=\frac23[(q+a)\beta+q_D\zeta^2]>0.
 \tag{15}
\]

More precisely, for every fixed \(\delta>0\), both errors are bounded by
\(C_\delta/\sqrt n\) with probability at least \(1-\delta\), for a
constant independent of \(n\).

Here is a direct proof of the less immediate matrix contraction in (15).
Condition on \(h\), write \(v=Wh\), and condition next on \(v\).
Gaussian regression of each row gives

\[
 W=\frac{vh^T}{\|h\|_2^2}+\Xi,
\]

where the rows of \(\Xi\) are independent centered Gaussians with
covariance \(n^{-1}(I-hh^T/\|h\|_2^2)\), independent of \(v\)
conditionally on \(h\). Consequently

\[
 W^Tb=\frac{h(v^Tb)}{\|h\|_2^2}+\Xi^Tb.
 \tag{16}
\]

Given \(h,v\), the second term is Gaussian with covariance

\[
 \Sigma=\frac{\|b\|_2^2}{n}
 \left(I-\frac{hh^T}{\|h\|_2^2}\right).
\]

The conditional expectation of its contribution to
\(n^{-1}(W^Tb)^TD(W^Tb)\) is
\(n^{-1}\operatorname{tr}(D\Sigma)\). It converges to
\(a\beta\). The correction from the rank-one projection is at most
\(\|b\|_2^2/n^2\), hence \(O(1/n)\). The conditional variance of
the centered Gaussian quadratic form is

\[
 \frac{2}{n^2}\operatorname{tr}(D\Sigma D\Sigma)=O(1/n),
\]

because \(0\le D\le I\) and \(\|\Sigma\|_{\rm op}\) is bounded.
The cross term in (16) has variance \(O(1/n)\) on
\(q_n\ge q/2\): the squared norm of its deterministic vector is
\(O(n)\), whereas its normalization is \(n^{-2}\). Its mean is zero.
The remaining deterministic contribution equals

\[
 \frac{(v^Tb/n)^2}{q_n^2}\frac{h^TDh}{n}.
\]

Bounded-variable laws of large numbers, conditionally for the coordinates
of \(v\), give the limit
\(q_D(\mathbb E[Zb(Z)]/q)^2=q_D\zeta^2\). The last equality follows
by integrating the Gaussian density by parts; the boundary term vanishes
because \(b,b'\) are bounded. All empirical averages used here have
variance \(O(1/n)\), including \(v_ib(v_i)\), which is bounded.
Their conditional means are Lipschitz in \(q_n\) on
\([q/2,3q/2]\): represent \(v_i=\sqrt{q_n}G_i\) and differentiate
under the expectation, using the bounded derivatives and
\(\mathbb E|G_i|<\infty\). Chebyshev's inequality, the exponentially
small complement of this interval, and a finite union bound give the stated
\(C_\delta/\sqrt n\) rate. This proves (15) without assuming a
population dynamical theorem.

The constants \(q,a,q_D,\kappa,\beta,\zeta\) are law-derived. For
example, each can be computed to absolute error \(\epsilon\) by
truncating a standard Gaussian integral at
\(R=O(\sqrt{\log(1/\epsilon)})\), then applying a midpoint rule to
the smooth bounded integrand. A mesh of size
\(O(\epsilon/R)\) suffices after a uniform derivative bound, requiring
\(O(\epsilon^{-1}\log(1/\epsilon))\) streamed evaluations and a
fixed number of scalar accumulators. Evaluating \(b(\sqrt qG)\) uses
the previously computed \(q\); on \(q\ge q/2>0\), its quadrature
error propagates with a finite Lipschitz constant. Thus these coefficients
are actual finite computations from the law, not latent dense-state or
response-oracle coefficients. This cost bound is deliberately elementary;
it does not assert a high-order quadrature theorem.

## 4. What the cubic coefficient does and does not prove

At fixed \(n\), expand the physical-time training prediction in its label:

\[
 f_n(t;y)=y(1-e^{-2\kappa_nt})+y^3 B_n(t)+O_{n,t}(y^5).
\]

Substituting (14) in (2), solving the first- and third-order scalar
equations, and integrating by parts gives

\[
 B_n(t)=\frac{6c_n}{\kappa_n^2}e^{-2\kappa_nt}
 \left[t-\frac{1-e^{-2\kappa_nt}}{\kappa_n}
 +\frac{1-e^{-4\kappa_nt}}{4\kappa_n}\right].
 \tag{17}
\]

One way to verify every sign in (17) is to put
\(s_1(t)=(1-e^{-2\kappa_nt})/\kappa_n\). The cubic coefficient of
\(s\) solves
\(s_3'=-2\kappa_ns_3-2c_ns_1^3\), and the cubic prediction is
\(\kappa_ns_3+c_ns_1^3
=6c_ne^{-2\kappa_nt}\int_0^t s_1(u)^2\,du\).
It is strictly positive for \(t>0\) whenever \(c_n>0\).

There is also an exact statement at **fixed** label, needing no label
remainder. Applying the chain rule to (2) at \(t=0\) gives

\[
 \partial_t^3 f_n(0;y)=8\kappa_n^3y+48c_ny^3
 \longrightarrow 8\kappa^3y+48c_3y^3.
 \tag{17a}
\]

Indeed, \(s'(0)=2y\), \(s''(0)=-4\kappa_ny\),
\(s'''(0)=8\kappa_n^2y\), and \(F_n'''(0)=6c_n\).
This exhibits a surviving nonlinear initial-time derivative at every fixed
nonzero label. Uniform convergence of predictions alone does not imply
convergence of their third derivatives, so (17a) must not be turned into an
unproved uniform-error lower bound.

Thus the dense initialization law has a nonzero trained-feature correction
already at cubic label order. A proposal that simply freezes the initial
kernel omits a nonzero coefficient. However, the finite-width Taylor
remainder in (14) or (17) is not known here to be uniform in width. Therefore
these coefficient calculations alone do **not** prove a fixed-label
population discrepancy, nor a contradiction to a hypothetical
\(n^{-1/2}\) approximation theorem. They identify the coefficient that
such a theorem must retain or control.

The law-derived cubic scalar model
\(P(s)=\kappa s+c_3s^3\) and
\(\dot\sigma=2[y-P(\sigma)]\) is a concrete autonomous feedback
system with one state and two stored coefficients. It is not a proved
\(n^{-1/2}\) surrogate: cubic agreement gives no estimate of the
omitted terms at a fixed nonzero label, and no sphere decoder was
constructed. Its role is to demonstrate a computable, nontrivial feedback
term, with the approximation claim explicitly withheld.

## 5. Exact bottlenecks for extending the construction

To promote this analytic route, one needs law-computable functions
\(P_K,R_K\) satisfying, for fixed sufficiently small labels,

\[
 \sup_{|s|\le S,\ \|x\|_2=\sqrt d}
 \bigl(|F_n(s)-P_K(s)|+|Q_n(s,x)-R_K(s,x)|\bigr)
 \le C_\delta n^{-1/2}+C\rho^K,
 \quad 0<\rho<1,
 \tag{18}
\]

with the exact compatibility \(R_K(s,x_1)=P_K(s)\),
polynomial-in-\(K\) storage, a derivative bound sufficient to keep the
surrogate monotone, and explicitly finite coefficient-computation and
decoder costs. Choosing \(K=O(\log n)\) would then complete the
one-sample case through (13). A stretched exponential tail would also
suffice if its storage exponent remained fixed.

None of the following is enough to establish (18): existence of every
fixed-order Gaussian coefficient; smoothness of every finite-width flow;
width-independent bounds on the real trajectory; or the all-time stability
estimate (13). In particular, (5) controls RMS increments, not the maximum
coordinate increment. It does not give a width-uniform complex
neighborhood avoiding the poles of \(\tanh\), so applying a Taylor
remainder theorem with a width-independent analytic radius would be
unjustified. Averaging over Gaussian initialization might improve
regularity, but that is a separate theorem, not a consequence of (5).

For several samples, even the exact scalar reduction has an additional
obstacle. Let \(V_a\) be the preconditioned negative-gradient direction
with residual factor removed for sample \(a\). Then

\[
 \dot\theta=\frac2m\sum_a(y_a-f_{n,a})V_a(\theta).
\]

At zero readout, the \(W\) block of the commutator
\([V_a,V_b]:=DV_bV_a-DV_aV_b\) is

\[
 [V_a,V_b]_W
 =\frac1n\left[
 (g_a\odot\tanh'v_b)h_b^T
 -(g_b\odot\tanh'v_a)h_a^T
 \right].
 \tag{19}
\]

Orthogonality of \(x_a,x_b\) does not set this matrix to zero. For
example, already at width one with \(W>0\) and distinct positive
\(h_a,h_b\), its scalar value is generically nonzero. More explicitly,
take \(W=1\) and \(0<h_a<h_b<1\); dividing by the positive
\(h_ah_b\tanh'(h_a)\tanh'(h_b)\) leaves
\(\sinh(2h_a)/(2h_a)-\sinh(2h_b)/(2h_b)<0\), since the latter
function is strictly increasing on the positive line by its power series.
Such hidden values are compatible with orthogonal inputs through suitable
first-layer projections.

Consequently, a general full-parameter feature solution cannot be a
path-independent function merely of the accumulated residual coordinates
\(\int_0^t2(y_a-f_{n,a})/m\,dt\). One must control additional response
or commutator information, or prove a valid alternative closure. This is a
failure of that particular reduction, not a no-go theorem for compact
observable dynamics or a proof that the population limit retains the same
noncommutativity.

The sharp conclusion is therefore partial: (1)--(17) supply an exact
single-sample all-time reduction, a width-independent stability mechanism,
and a nonzero nonlinear coefficient computable from the Gaussian law. The
requested direct compact construction still needs the uniform constructive
approximation in (18), and for general sample count a finite closure that
addresses (19). No experiment, population theorem, or oracle assumption
has been substituted for those missing steps.

## 6. Author check (internal, not independent review)

The source reviewed is this complete artifact; its frozen SHA-256 is
reported to the supervisor after the final edit rather than embedded in its
own hashed content. The following checks were performed on the final text.

- **Normalization:** the loss has no factor one-half, and the mobilities
  \((n,1,n)\) yield exactly the factor \(2\) in (2), the factor
  \(1/n\) in the hidden-matrix derivative, and no extra \(1/n\) in
  the first-matrix feature derivative. With
  \(\|x_1\|_2^2=d\), multiplying the first-matrix derivative by
  \(x_1/\sqrt d\) gives precisely (4).
- **Cubic coefficient:** direct product expansion gives
  \(1/2+1/6=2/3\) in (14). Gaussian regression (16) preserves the
  dependence between \(W\) and \(Wh\); replacing that dependence by
  independence would incorrectly omit \(q_D\zeta^2\).
- **Physical time:** the linear flow is
  \(y(1-e^{-2\kappa_nt})\). Equations (17) and (17a) agree at small
  time: the cubic label correction starts as \(8c_ny^3t^3\), whose
  third derivative is \(48c_ny^3\).
- **Decoder consistency:** section 2 now explicitly requires
  \(R(s,x_1)=P(s)\). This makes the scalar feedback its own training
  residual and supplies the stated positive gradient-flow mobility.
- **All-time propagation:** the contraction constant \(k\), sphere
  Lipschitz constant \(L\), and allowed label interval are independent
  of width on the stated initialization event. The convergence of both
  scalar states supplies the endpoint assertion.
- **Approximation scope:** (11) and (18) remain unproved premises. Neither
  smooth finite-width trajectories nor convergent low-order coefficients
  supply their uniform remainders. The nonlinear derivative result does
  not imply a uniform prediction-error lower bound.
- **General sample count:** (19) only blocks a path-independent
  full-parameter parametrization by residual integrals. It does not rule
  out a compact observable closure or establish a population obstruction.
- **Provenance and cost:** the computed coefficients use fixed-dimensional
  Gaussian integrals. No initialized dense array, realized trajectory,
  target-response oracle, experiment, or external result is needed for
  the proved identities. Polylogarithmic storage for an accurate
  high-order hierarchy is not asserted.
