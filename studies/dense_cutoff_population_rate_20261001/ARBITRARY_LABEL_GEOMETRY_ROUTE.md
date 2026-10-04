# Arbitrary fixed labels: one-sample geometry and exact deep-linear passive fluctuations

2026-10-03. Scoped theoretical route; no experiments. These are complete
deterministic and probabilistic arguments for the subclasses stated below,
not a counterexample or a general arbitrary-label population-rate theorem.
They have been checked by their author, not independently reviewed or promoted.

The conclusions are:

1. At every finite depth, one-sample fitting with zero initial readout does
   not require bounded activation values, small labels, or even globally
   bounded activation derivatives. Smooth local well-posedness and positive
   initial last-feature energy suffice. A finite target is reached on the
   controlled curve before any possible controlled blowup.
2. For canonical deep linear networks with one sphere input and any fixed
   label, the entire passive prediction process minus the training prediction
   times the input correlation has strict root-width fluctuations. The fitted
   endpoint has an exact conditional Gaussian law around a deterministic
   predictor, with sharp root-width scale on nonparallel test inputs.
3. Neither statement proves the nonlinear multi-sample population rate.
   The second leaves the scalar training transient as the only possible
   source of a slower rate in its linear one-sample subclass.

## Scope, inputs, and provenance

Allowed scientific inputs were the current manuscript and its included proofs,
the book index and notation, and this study's LARGE_LABEL_ASSESSMENT.md,
LARGE_LABEL_ASSESSMENT_CHECK.md, and GENERAL_SELF_AVERAGING.md. The three study
notes and both book entry files were read completely. The manuscript setting
in `paper/main.tex`, lines 173--212, and the all-time statements in
`paper/results.tex` were read to fix the architecture and mobility conventions;
no manuscript theorem outside its stated hypotheses is used. No other study
was read. Required canonical-notation, rigorous-math, and conjecture-audit
instructions were applied.

The author independently derived the two-hidden-layer linear balancedness
equation in Section 4. The supervisor subsequently sent the same equation,
explicitly permitting comparison. The scalar stopping extension was likewise
derived independently by both before comparison. Sections 2--3 below were
derived by this author. Before this file was frozen, the supervisor announced
a separate Wick-moment proof of the remaining two-layer scalar rate; that
unread proposed proof is not an input to any conclusion here. Thus this file
is a scoped research derivation, not a blind review of the supervisor's route.

Source SHA-256 hashes:

```text
paper/main.tex: 60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95
paper/results.tex: 6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1
docs/index.qmd: f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de
docs/notation.qmd: 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023
LARGE_LABEL_ASSESSMENT.md: 736ad09b8081657373ba98687cc32f52bfdc2db33d46c72c69e5ad85ce977208
LARGE_LABEL_ASSESSMENT_CHECK.md: c3692e1ec1cceb30a49be266769433542572506b97099d0a20c956054f23564a
GENERAL_SELF_AVERAGING.md: bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5
```

The shared HEAD was `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e` and the shared
index was empty before this file was written. Other working changes were
preserved. Only this assigned file is written by this route.

## 1. The scalar stopping argument does not require bounded activations

Fix one training input \(x_0\), width \(n\), and finite depth \(L\).
The forward equations and output are
\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f(\theta,x)=w^\top h^{(L)}(x)/n.
\]
Here \(\theta\) collects all parameters, and the positive mobility matrix
\(M\) is \(n\) on first weights and readout and \(1\) on hidden matrices.
Assume the finite vector field is locally Lipschitz, as holds for \(C^2\)
activations. The loss is \((f(\theta,x_0)-y)^2\), and \(w(0)=0\).
Write
\[
 Q_0=\|h^{(L)}(0,x_0)\|_2^2/n>0.
\]

For positive labels, first follow the controlled gradient-ascent curve
\[
 \theta'(u)=M\nabla_\theta f(\theta(u),x_0),\qquad
 P(u)=f(\theta(u),x_0),\qquad
 R(u)=\|w(u)\|_2/\sqrt n.                         \tag{1}
\]
Primes in this section denote controlled time \(u\), not physical time.
The squared mobility norm is
\[
 \|\dot\theta\|_{M^{-1}}^2
 =\|\dot W^{(1)}\|_F^2/n
  +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F^2
  +\|\dot w\|_2^2/n.
\]
The readout equation is \(w'=h^{(L)}(x_0)\), hence
\[
 P'=\|\theta'\|_{M^{-1}}^2
       \ge\|h^{(L)}(x_0)\|_2^2/n,
 \qquad R'=P/R\quad(R>0).                         \tag{2}
\]
All lower-layer velocities vanish at zero readout. In particular
\(P'(0)=Q_0\) and \(R'(0+)=\sqrt{Q_0}\).
For \(u>0\) in the maximal controlled existence interval,
\[
 P'\ge P^2/R^2=(R')^2,\qquad
 R''=\frac{P'-(R')^2}{R}\ge0.                     \tag{3}
\]
Initially \(R>0\); convexity gives \(R'\ge\sqrt{Q_0}\) and
\(R\ge u\sqrt{Q_0}\), so it never returns to zero. Consequently
\[
 P'(u)\ge Q_0,\qquad P(u)\ge Q_0u.               \tag{4}
\]

**Finite-target continuation.** For every fixed \(Y>0\), the controlled
curve reaches \(P=Y\) at a unique finite \(u_Y\le Y/Q_0\), and the
parameter state there is finite. To prove this, suppose the curve does not
reach \(Y\). Equation (4) forces its maximal interval to end at a finite
\(U\le Y/Q_0\). On that interval \(P<Y\), and (2) gives
\[
 \int_0^U\|\theta'(u)\|_{M^{-1}}^2du\le Y.
\]
For \(0\le s<t<U\), Cauchy--Schwarz bounds its displacement by
\(\sqrt{Y(t-s)}\). The parameters therefore have a finite limit at
\(U\). Local well-posedness continues the solution there, contradicting
maximality. This proves the assertion even when the unrestricted controlled
curve blows up later.

In particular,
\[
 \int_0^{u_Y}\|\theta'\|_{M^{-1}}du
 \le\sqrt{u_YY}\le Y/\sqrt{Q_0},                 \tag{5}
\]
and the normalized parameter distance of the manuscript is bounded by
\(\sqrt{L+1}\,Y/\sqrt{Q_0}\) from initialization, along the entire fitted
curve. No bounded-activation assumption occurs in this estimate.

The physical scalar clock solves
\[
 \dot u=2[Y-P(u)],\qquad u(0)=0.
\]
It remains in \([0,u_Y]\), exists globally, and converges to \(u_Y\).
Its residual and integrated activity satisfy
\[
 |f_n(t,x_0)-Y|\le Ye^{-2Q_0t},\qquad
 2\int_0^\infty|f_n(t,x_0)-Y|dt=u_Y\le Y/Q_0.    \tag{6}
\]
The actual parameters converge to the finite fitted state. For negative
labels replace \((y,w)\) by \((-y,-w)\): the hidden physical dynamics
are unchanged and the output changes sign. For \(y=0\), the initialized
network is stationary. This proves the same claims for every fixed real
label with \(Y=|y|\).

When activation slopes are bounded, (5) and bounded initial hidden operator
norms give width-independent bounds for every hidden operator norm, training
feature RMS, and readout RMS. With the first-weight Frobenius norm divided by
\(\sqrt n\) initially bounded, the same holds for query feature RMS divided
by \(1+\|x\|/\sqrt d\). Thus the extension includes the linear-growth
activation class in the assignment. It gives no fluctuation or population
bias estimate by itself.

## 2. Deep linear training leaves a conditionally independent Gaussian query component

Now let every activation be \(\phi_\ell(z)=z\), with any fixed \(L\ge2\).
This is a literal subclass of the assigned canonical model: all first and
hidden matrices train with the stated mobilities, hidden entries are
independent \(N(0,1/n)\), first entries are independent \(N(0,1)\), and
the readout starts exactly at zero. No layer is frozen by intervention.
Take one sphere input and write
\[
 v_0=x_0/\sqrt d,\quad\|v_0\|_2=1,\qquad
 a_0=W^{(1)}(0)v_0\in\mathbb R^n.
\]
Let \(\mathcal F_0\) be generated by \(a_0\) and all initialized hidden
matrices. The complete training trajectory is measurable with respect to
\(\mathcal F_0\). Every first-layer update is an outer product with
\(v_0^\top\), so, with \(a(u)=W^{(1)}(u)v_0\),
\[
 W^{(1)}(u)=a(u)v_0^\top+B,
 \qquad B=W^{(1)}(0)(I-v_0v_0^\top).               \tag{7}
\]
In an orthonormal basis of \(v_0^\perp\), the columns of \(B\) are
independent standard Gaussian vectors, independent of \(\mathcal F_0\).
This follows by orthogonal transformation of each isotropic Gaussian row of
\(W^{(1)}(0)\); no trained matrix is declared Gaussian.

Define the residual-free first-layer backward vector
\[
 k(u)=W^{(2)}(u)^\top\cdots W^{(L)}(u)^\top w(u).
\]
For a fixed query, decompose its normalized input as
\[
 v=x/\sqrt d=c v_0+v_\perp,\qquad
 c=v_0^\top v=x_0^\top x/d,\qquad v_\perp\perp v_0.
\]
The exact prediction decomposition is
\[
 f_n(t,x)=c f_n(t,x_0)
           +\frac{k(u(t))^\top Bv_\perp}{n}.      \tag{8}
\]
Conditional on \(\mathcal F_0\), the second term is a centered Gaussian
process with conditional covariance
\[
 \operatorname{Cov}\bigl(f_n(t,x)-cf_n(t,x_0),
     f_n(s,x')-c'f_n(s,x_0)\mid\mathcal F_0\bigr)
 =\frac{k(u(t))^\top k(u(s))}{n^2}
      v_\perp^\top v'_\perp.                     \tag{9}
\]
The negative-label convention multiplies \(k\) by \(-1\), without
affecting the covariance.

### A good event involving only the training roots

Fix constants \(q>0\) and \(K<\infty\) so that the events
\[
 G_n=\left\{Q_0\ge q,\quad
       \|a_0\|_2/\sqrt n\le K,\quad
       \max_{2\le\ell\le L}\|W^{(\ell)}(0)\|_{\rm op}\le K\right\}
                                                               \tag{10}
\]
satisfy \(\Pr(G_n)\to1\). This can be verified without a dynamical
population theorem. The initial first-feature energy is \(\chi_n^2/n\).
Conditional on the preceding layer's features, each hidden-layer energy is
the preceding energy times another \(\chi_n^2/n\) ratio. These ratios have
mean 1 and variance \(2/n\), so the final energy tends to 1 for fixed depth.
For the operator norms, a \(1/4\)-net of the unit sphere has at most
\(9^n\) points. Applying the Gaussian tail to every two-net bilinear
pairing bounds \(\Pr(\|W\|_{\rm op}>K)\) by
\(2\exp(2n\log9-nK^2/8)\); a sufficiently large fixed \(K\) works.
Here the net inequality is \(\|W\|_{\rm op}\le2\max_{u,v}|u^\top Wv|\).
Taking a union bound over fixed depth proves the claim. The event \(G_n\)
belongs to \(\mathcal F_0\), preserving the conditional Gaussian law.

On \(G_n\), (5) bounds all trained hidden operator norms and
\(\|a(u)\|_2/\sqrt n,\|w(u)\|_2/\sqrt n\) by a constant depending
only on \(K,q,L,Y\), up to the fitted control time \(u_Y\).
Linear forward and backward recursions therefore give
\[
 \sup_{u\le u_Y}\frac{\|k(u)\|_2+\|k'(u)\|_2}{\sqrt n}
 \le C_{K,q,L,Y}.                                \tag{11}
\]
For completeness, the controlled updates are
\[
 a'=k,\quad w'=h^{(L)}(x_0),\quad
 (W^{(\ell)})'=\delta^{(\ell)}
                      h^{(\ell-1)}(x_0)^\top/n.
\]
Every feature and backward vector has bounded RMS on this tube, so each
hidden derivative has bounded operator norm. Differentiating the finite
product defining \(k\) gives \(L-1\) terms with one matrix derivative
and one term with \(w'\), each bounded in RMS. This proves (11).

## 3. Strict root-width bounds, including the fitted endpoint

Let \(\mu\) be a fixed probability law with
\(\int\|x\|_2^2d\mu(x)<\infty\). Define the whole-time passive error
\[
 \mathcal R_{n,\mu}
 =\left(\int\sup_{t\ge0}
       |f_n(t,x)-c(x)f_n(t,x_0)|^2d\mu(x)\right)^{1/2}.           \tag{12}
\]
Then
\[
 \mathbb E[\mathbf1_{G_n}\mathcal R_{n,\mu}^2]
 \le\frac{C_{K,q,L,Y}}{n}
               \int\|v_\perp(x)\|_2^2d\mu(x).                 \tag{13}
\]

To prove (13), set \(S=Y/q\) and extend the controlled vector after fitting
by \(\bar k(u)=k(\min\{u,u_Y\})\), \(0\le u\le S\).
It is absolutely continuous, starts at zero, and obeys (11) almost
everywhere. This is only a device for bounding the already trained path.
For each fixed query,
\[
 \sup_{0\le u\le S}|\bar k(u)^\top Bv_\perp/n|^2
 \le\frac S{n^2}\int_0^S
                   |\bar k'(u)^\top Bv_\perp|^2du.
\]
Condition on \(\mathcal F_0\). Gaussian independence makes the expected
integrand \(\|\bar k'(u)\|_2^2\|v_\perp\|_2^2\). Equation (11)
therefore bounds the conditional expectation by
\(C S^2\|v_\perp\|_2^2/n\). Tonelli and (8) give (13). The case
\(Y=0\) is identically zero and needs no division by \(S\).

Thus for every fixed confidence, sufficiently large widths obey
\(\mathcal R_{n,\mu}\le C_{\delta,\mu,L,Y}/\sqrt n\) with probability
at least \(1-\delta\). Markov's inequality is applied to (13), and
\(\Pr(G_n^c)\to0\) is added separately. No unconditional moment estimate
on the exceptional event is asserted.

At the fitted endpoint, write \(k_*=k(u_Y)\). Equation (8) becomes
\[
 f_n(\infty,x)=y\,x_0^\top x/d+\frac{k_*^\top Bv_\perp}{n},    \tag{14}
\]
with the exact conditional law
\[
 f_n(\infty,x)-y\,x_0^\top x/d
  \mid\mathcal F_0
 \sim N\left(0,\frac{\|k_*\|_2^2}{n^2}\|v_\perp\|_2^2\right).
                                                               \tag{15}
\]
In particular the deterministic endpoint limit is the linear predictor
\(x\mapsto yx_0^\top x/d\), with strict root-width convergence in the
query \(L^2(\mu)\) norm. This assertion about limits of fitted endpoints
does not silently interchange the width and infinite-time limits of a
nonlinear population construction.

The endpoint rate is also sharp for a fixed \(y\ne0\) and a nonparallel
query. From \(y=k_*^\top a(u_Y)/n\) and the tube bound
\(\|a(u_Y)\|_2/\sqrt n\le M_{K,q,L,Y}\),
\[
 \frac{Y}{M_{K,q,L,Y}}\le\frac{\|k_*\|_2}{\sqrt n}
           \le C_{K,q,L,Y}\qquad\text{on }G_n.                 \tag{16}
\]
If \(v_\perp\ne0\), the conditional Gaussian standard deviation is
bounded above and below by positive constants times \(n^{-1/2}\).
For example, with \(c_*=Y\|v_\perp\|_2/M_{K,q,L,Y}\),
\[
 \Pr\{|f_n(\infty,x)-yx_0^\top x/d|\ge c_*/\sqrt n\}
 \ge\Pr(G_n)\Pr\{|Z|\ge1\},\qquad Z\sim N(0,1).             \tag{17}
\]
This is a canonical Gaussian width lower bound at the ordinary root rate,
not a slower-rate counterexample.

## 4. Two hidden linear layers: exact balance and the remaining transient

For \(L=2\), introduce normalized training vectors
\(A=a/\sqrt n\), \(b=w/\sqrt n\), and write \(W=W^{(2)}\).
Here \(A,b\in\mathbb R^n\), and \(A_0=A(0)\). In controlled time,
\[
 A'=W^\top b,\qquad W'=bA^\top,\qquad b'=WA,
 \qquad P=b^\top WA.                              \tag{18}
\]
Direct differentiation gives the exact conserved quantities
\[
 WW^\top-bb^\top=W_0W_0^\top,\qquad
 \|A\|_2^2-\|b\|_2^2=\|A_0\|_2^2.              \tag{19}
\]
Indeed the two terms in each matrix derivative cancel pairwise; the two
norm derivatives are both \(2b^\top WA\). Therefore
\[
 b''=W'A+WA'
 =\left[W_0W_0^\top+
       \bigl(\|A_0\|_2^2+2\|b\|_2^2\bigr)I\right]b,
 \quad b(0)=0,\quad b'(0)=W_0A_0,\quad P=b^\top b'.            \tag{20}
\]
This is a canonical reduction, with the original random Gaussian matrix
still present. It is not obtained by prescribing a special singular-vector
initialization or deleting the random matrix environment.

A spectral representation of (20) makes clear where a quantitative scalar
population rate would enter. If \(\nu_n\) is the spectral measure of
\(W_0W_0^\top\) weighted by \(W_0A_0\), then for the scalar propagator
\[
 \psi''(u,\lambda)
 =\bigl[\lambda+\|A_0\|_2^2+2\|b(u)\|_2^2\bigr]\psi(u,\lambda),
 \qquad\psi(0,\lambda)=0,\quad\partial_u\psi(0,\lambda)=1,
\]
one has exactly
\[
 \|b(u)\|_2^2=\int\psi(u,\lambda)^2d\nu_n(\lambda),\qquad
 P(u)=\int\psi(u,\lambda)\partial_u\psi(u,\lambda)d\nu_n(\lambda).
                                                               \tag{21}
\]
Here \(\nu_n(A)=(W_0A_0)^\top\mathbf1_A(W_0W_0^\top)(W_0A_0)\),
so its coefficients are explicitly determined by canonical initialization.
The scalar potential still depends on the evolving norm; (21) is an exact
nonlinear self-consistency relation, not a frozen-feature approximation.

The finite-output stopping theorem bounds \(\|b\|\), all trained
operators, and the fitted activity interval independently of width on
\(G_n\). In particular the scalar coefficient in the propagator equation
is bounded on \(0\le u\le u_Y\), uniformly for
\(0\le\lambda\le K^2\). The first-order system for
\((\psi,\partial_u\psi)\) and the bound \(u_Y\le Y/q\) give
\(\sup(|\psi|+|\partial_u\psi|)\le C_{K,q,Y}\) by Gronwall.
Every initial spectral component of \(b'(0)\) is multiplied by this
bounded factor. Thus a blowup at a finite target, or width-diverging
amplification of one initialized spectral component before a fixed target,
is ruled out in this subclass. Proving a quantitative rate for its scalar transient further
requires quantitative convergence of (21) and its feedback, rather than
only fitting or Gaussian concentration around a width-dependent center.
No such estimate is claimed in this file. The supervisor's separately
announced moment route is to be checked on its own persisted proof.

## 5. What this excludes, and what remains open

For one sample, arbitrary fixed labels cannot cause a reachable finite-target
singularity or a loss of the scalar tangent lower bound. This statement
extends the existing bounded-activation fitting result to the assigned
linear-growth activation class and beyond. It does not control population
bias in a general nonlinear deep network.

For canonical deep linear one-sample networks, the generalization component
orthogonal to the training input has root-width fluctuations throughout the
entire physical trajectory and a sharp root-width fitted error. A slower
all-time rate in this subclass would have to survive on the training input
itself. A proof based only on a poorly conditioned initialized hidden matrix
or a claimed large transverse query response cannot supply such a witness.

For multiple samples the shared readout update is a sum of feature vectors
with competing residual signs. There is no single controlled prediction
whose derivative supplies (3)--(4). Smooth degree-one homogeneous scalar
activations do not provide a distinct nonlinear escape from the linear
calculation: if \(\phi(cz)=c\phi(z)\) for \(c>0\) and \(\phi\) is
differentiable at zero, then \(\phi(0)=0\) and
\(\phi(z)=\phi'(0)z\), by taking the derivative along either ray at zero.
Nonlinear multi-sample dynamics with arbitrary fixed labels remain outside
the theorems proved here. No admissible slower-than-near-root counterexample
has been constructed by this route.
