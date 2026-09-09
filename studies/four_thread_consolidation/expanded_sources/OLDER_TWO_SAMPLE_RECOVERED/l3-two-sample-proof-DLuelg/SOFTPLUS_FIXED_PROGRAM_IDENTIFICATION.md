# Fixed-program identification for shifted softplus with three fixed caps

This is a finite-program lemma, not a time-continuum result. The number
of instructions, all step sizes, and all three caps are fixed before
width tends to infinity. There is no assertion uniform in the number
of queries, in a time mesh, or in the caps; no cap removal, local-flow
construction, or global convergence is proved here. No experiments were
performed.

## 1. Scope and precise reference program

Mathematical source inspection was restricted to:

* `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`,
  SHA-256 `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`.
  Text inspected: lines 1--680 (Sections 1--4 and the opening of
  Section 5); a heading/cross-reference index was inspected across the
  file. The mathematical dependencies used below are the Gaussian
  operator-norm estimate in Section 2, the conditioning formulas and
  response convention in Section 3, and the finite rank-update
  expansion in Section 4. No subsequent flow theorem is used.
* `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_LOCAL_BOOTSTRAP_PLAN.md`,
  all 135 lines, SHA-256
  `4848c8a8dd38b4b5bd856e7cad30418c9c538d83a6bb906b9d86c233ed3aba01`.
* `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md`,
  the additional dependency expressly authorized during this task,
  all 473 lines, SHA-256
  `0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b`.
  Its equations (2)--(3) fix the sample weights and bottom update
  convention. Its response theorem is not used or proved here.

No additional mathematical source files were inspected. The
solve-math-rigorously skill supplied proof-writing instructions, not
an external mathematical result. Every probabilistic estimate needed
for this extension is proved below.

Put
\[
 e=0.1,\qquad \phi(z)=1+e\log(1+\exp z),\qquad
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\quad -1\le\rho\le1.
 \tag{1}
\]
Sample indices are \(a,b\in\{1,2\}\). At each first-layer neuron the
initial pair \((G_1,G_2)\) is centered Gaussian with covariance \(C\);
these pairs are iid over neurons. The two initial matrices
\(W^{(2)}_0,W^{(3)}_0\) have mutually independent iid \(N(0,1/n)\)
entries and are independent of the first-layer pairs. The initial
readout is exactly the zero vector.

For \(j\in\{w,1,2\}\), fix a smooth odd cap \(\tau_j\) such that
\[
 |\tau_j(x)|\le\min(|x|,2R_j),\qquad
 0\le\tau'_j\le1,\qquad \tau_j(x)=x\quad (|x|\le R_j),
 \tag{2}
\]
The usual integral of a smooth compactly supported cutoff has these
properties. Only boundedness and continuity of the first cap derivative
are needed below; higher cap derivatives need not be bounded. The
numbers \(R_j\) are positive and fixed.

Following equations (2)--(3) of the newly authorized scalar-law file,
fix labels \(y_b\in\{-1,1\}\) and a step size \(\Delta>0\), and set
\(\gamma_{kb}=(\Delta/2)y_b\). This notation keeps the update and
response formulas readable. The proof also works for any fixed finite
deterministic array of update weights. No small-horizon assumption is
needed for this fixed-program result.

Here is the precise raw-preactivation Euler reference to which the
lemma applies. For \(0\le k\le M\), compute
\[
 h^{(\ell)}_{ka}=\phi(z^{(\ell)}_{ka}),\qquad
 z^{(2)}_{ka}=W^{(2)}_k h^{(1)}_{ka},\qquad
 z^{(3)}_{ka}=W^{(3)}_k h^{(2)}_{ka},
\]
\[
 \delta^{(3)}_{ka}=\tau_w(w_k)\phi'(z^{(3)}_{ka}),\qquad
 q^{(2)}_{ka}=(W^{(3)}_k)^T\delta^{(3)}_{ka},\qquad
 \delta^{(2)}_{ka}=\phi'(z^{(2)}_{ka})\tau_2(q^{(2)}_{ka}),
\]
\[
 q^{(1)}_{ka}=(W^{(2)}_k)^T\delta^{(2)}_{ka},\qquad
 \delta^{(1)}_{ka}=\phi'(z^{(1)}_{ka})\tau_1(q^{(1)}_{ka}).
 \tag{3}
\]
For \(k<M\), update
\[
 z^{(1)}_{k+1,a}=z^{(1)}_{ka}
                +\sum_b\gamma_{kb}C_{ab}\delta^{(1)}_{kb},
\]
\[
 W^{(\ell)}_{k+1}=W^{(\ell)}_k+
       \frac1n\sum_b\gamma_{kb}\delta^{(\ell)}_{kb}
                              (h^{(\ell-1)}_{kb})^T,
 \quad \ell=2,3,
\]
\[
 w_{k+1}=w_k+\sum_b\gamma_{kb}h^{(3)}_{kb},\qquad
 f_{n,ka}=\frac1n w_k^T h^{(3)}_{ka}.
 \tag{4}
\]
The \(C_{ab}\) in the first update is the input Gram factor for a
shared first-layer weight matrix evaluated on two normalized inputs.
It agrees with the convention in the supplied scalar law.

In particular, the readout update and prediction are uncapped. Only
the occurrence of the readout in \(\delta^{(3)}\) is capped. Both
reverse answers are capped where they enter the next delta. This is
an auxiliary reference program; no gradient-energy identity is assumed.

## 2. Statement and exact scalar law

**Lemma.** Fix \(M<\infty\), the caps, the weights, and \(\rho\).
For each layer, every finite joint list of the fields in (3)--(4)
converges empirically in probability against every continuous test
of polynomial growth to the scalar law below: for each such tuple
\(\mathcal X_n\) and test \(T\),
\[
 \frac1n\sum_{i=1}^nT(\mathcal X_{n,i})
       \ \xrightarrow{\mathbb P}\ \mathbb E T(\mathcal X).
\]
This holds jointly for every finite collection of tests and populations.
In particular all mixed polynomial moments converge, and the empirical
measures converge in every Wasserstein order \(1\le p<\infty\).
Products and contractions
are taken within their proper neuron population; no pairing of neuron
indices from different populations is asserted.

The same conclusion holds after adjoining any fixed finite collection
of instructions using deterministic linear combinations, smooth
globally Lipschitz coordinate maps with bounded first derivatives,
and either orientation of either initial matrix, together with the
quadratic contraction feedback in the rank-update expansions. Tests may be
unbounded polynomials; allowing them as tests does not authorize
arbitrary unbounded polynomial coordinate maps as new query instructions.

There are four mutually independent centered jointly Gaussian groups,
also independent of the initial pair:
\[
 (\xi^{(2)}_{ka}),\quad (\xi^{(3)}_{ka}),\quad
 (\zeta^{(2)}_{ka}),\quad (\zeta^{(1)}_{ka}).
 \tag{5}
\]
Different slots within one group can be correlated or identical.
Layer 1 fields use \((G_1,G_2,\zeta^{(1)})\); layer 2 fields use
\((\xi^{(2)},\zeta^{(2)})\); layer 3 fields use \(\xi^{(3)}\).
These descriptions specify separate population laws. They may be
realized on an independent product space without attributing a
cross-layer empirical pairing to that realization.

With expectations always taken in the population containing the
integrand, the exact recursion is
\[
 Z^{(1)}_{ka}=G_a+\sum_{r<k,b}\gamma_{rb}C_{ab}
        \phi'(Z^{(1)}_{rb})\tau_1(q^{(1)}_{rb}),
 \qquad H^{(1)}_{ka}=\phi(Z^{(1)}_{ka}),
 \tag{6}
\]
\[
 Z^{(\ell)}_{ka}=\xi^{(\ell)}_{ka}
       +\sum_{r<k,b} A^{(\ell)}_{ka,rb}\delta^{(\ell)}_{rb},
 \qquad H^{(\ell)}_{ka}=\phi(Z^{(\ell)}_{ka}),\quad \ell=2,3,
 \tag{7}
\]
\[
 \mathsf W_k=\sum_{r<k,b}\gamma_{rb}H^{(3)}_{rb},\qquad
 \delta^{(3)}_{ka}=\tau_w(\mathsf W_k)\phi'(Z^{(3)}_{ka}),
 \tag{8}
\]
\[
 q^{(2)}_{ka}=\zeta^{(2)}_{ka}
       +\sum_{r\le k,b}B^{(3)}_{ka,rb}H^{(2)}_{rb},\qquad
 \delta^{(2)}_{ka}=\phi'(Z^{(2)}_{ka})\tau_2(q^{(2)}_{ka}),
 \tag{9}
\]
\[
 q^{(1)}_{ka}=\zeta^{(1)}_{ka}
       +\sum_{r\le k,b}B^{(2)}_{ka,rb}H^{(1)}_{rb},\qquad
 f_{ka}=\mathbb E[\mathsf W_kH^{(3)}_{ka}].
 \tag{10}
\]
The covariances are the **uncentered** input second moments:
\[
 \mathbb E[\xi^{(\ell)}_{ka}\xi^{(\ell)}_{vb}]
     =\mathbb E[H^{(\ell-1)}_{ka}H^{(\ell-1)}_{vb}],\qquad
 \mathbb E[\zeta^{(\ell-1)}_{ka}\zeta^{(\ell-1)}_{vb}]
     =\mathbb E[\delta^{(\ell)}_{ka}\delta^{(\ell)}_{vb}].
 \tag{11}
\]
The deterministic response coefficients are
\[
 A^{(\ell)}_{ka,rb}
  =\mathbb E\!\left[\frac{\partial H^{(\ell-1)}_{ka}}
                      {\partial\zeta^{(\ell-1)}_{rb}}\right]
       +\gamma_{rb}\mathbb E[H^{(\ell-1)}_{ka}H^{(\ell-1)}_{rb}],
       \qquad r<k,
 \tag{12}
\]
\[
 B^{(\ell)}_{ka,rb}
  =\mathbb E\!\left[\frac{\partial\delta^{(\ell)}_{ka}}
                      {\partial\xi^{(\ell)}_{rb}}\right]
       +\mathbf1_{r<k}\gamma_{rb}
                    \mathbb E[\delta^{(\ell)}_{ka}\delta^{(\ell)}_{rb}],
       \qquad r\le k.
 \tag{13}
\]
Each derivative differentiates the complete explicit coordinate
expression, holding all deterministic coefficients, selected scalar
feedback values, and covariance parameters fixed. It does not
differentiate the operation that selected those coefficients. Formally
distinct Gaussian slots are retained even when their covariance is
singular. Derivatives with respect to unavailable future slots are zero.

The causal order is both forward matrix-2 calls, both forward matrix-3
calls, both reverse matrix-3 calls, and both reverse matrix-2 calls,
then the update. This gives a uniquely determined finite recursion of
covariances, coefficients, and laws. In particular the sums in (12)
are strictly past-step; (13) includes the current step.

The rest of this document proves the lemma, including the moment
extension and the singular cases. The argument first obtains uniform
coordinate moments directly at finite width, then performs conditional
Gaussian induction at nonsingular Grams, and finally removes auxiliary
query noise and restores empirical scalar feedback.

## 3. Uniform moments of the actual finite programs

All moment orders below satisfy \(1\le p<\infty\). For a vector write
\(\|x\|_{n,p}=(n^{-1}\sum_i|x_i|^p)^{1/p}\). Joint tuples use
the Euclidean coordinate norm in this definition.

### 3.1 The available maps really are globally Lipschitz

Let \(s(z)=(1+\exp(-z))^{-1}\). Then
\[
 1\le\phi(z)\le 1+e\log2+e|z|,\qquad
 \phi'(z)=es(z),\quad \phi''(z)=es(z)(1-s(z)).
 \tag{14}
\]
All positive-order derivatives of \(\phi\) are bounded: differentiating
a polynomial in \(s\) replaces it by \(s(1-s)\) times its polynomial
derivative, and \(0\le s\le1\). The maps
\[
 (z,v)\longmapsto \phi'(z)\tau_j(v),\qquad j=w,1,2,
 \tag{15}
\]
are bounded and smooth, with bounded first derivatives. Their first
partial derivatives are
\(\phi''(z)\tau_j(v)\) and \(\phi'(z)\tau'_j(v)\).
Thus every coordinate map in (3)--(4), after scalar coefficients are
treated as scalar nodes, is globally Lipschitz. The feature and readout
values need not be bounded. No truncation of those values has been made.

### 3.2 A dimension-independent Gaussian moment estimate

Here is the elementary estimate used instead of an unproved
localization transfer. If \(g\) is a standard Gaussian vector in any
finite dimension, \(F\) is continuously differentiable, and its value
and gradient have the indicated finite moments, then for \(p\ge1\)
\[
 \mathbb E|F(g)-\mathbb EF(g)|^p
 \le (\pi/2)^p m_p\,\mathbb E\|\nabla F(g)\|_2^p,
 \qquad m_p=\mathbb E|N(0,1)|^p.
 \tag{16}
\]
To prove this, take an independent standard Gaussian \(g'\), and put
\(g_\theta=g\cos\theta+g'\sin\theta\) and
\(v_\theta=-g\sin\theta+g'\cos\theta\). For each \(\theta\),
these two vectors are independent standard Gaussians. The fundamental
theorem of calculus and the integral form of Hölder's inequality give
\[
 |F(g')-F(g)|^p\le (\pi/2)^{p-1}
   \int_0^{\pi/2}|\nabla F(g_\theta)\cdot v_\theta|^p\,d\theta.
\]
Conditional Gaussian integration of \(v_\theta\) proves the bound
for \(F(g')-F(g)\); conditional Jensen proves (16). All uses below
have polynomial growth in a finite Gaussian vector, which justifies
the integrals and the fundamental-theorem calculation directly.

### 3.3 Polynomial control of parameter derivatives

Unroll every trained matrix into its initial action and its finitely
many rank-one updates. The resulting graph has four kinds of nodes:
globally Lipschitz smooth coordinate maps; initial matrix actions in
either orientation; scalar contractions \(\langle x,y\rangle_n\);
and scalar arithmetic and scalar-times-vector operations. Deterministic
constants and the scalar additions and multiplications in the unrolled
graph are allowed. Every scalar contraction has normalization \(1/n\).

We also allow, for the proof, an independent standard Gaussian vector
added with coefficient \(\epsilon\in[0,1]\) immediately before each
initial matrix query. Only finitely many such roots are needed. They
are independent of the original matrices and roots.

Represent all randomness by a single standard Gaussian vector
\(g_n\), including the unscaled matrix entries. For example
\(G_1=g,\ G_2=\rho g+\sqrt{1-\rho^2}\,g'\); this representation
also works at both endpoints. Set
\[
 K_n=1+\|W^{(2)}_0\|_{\rm op}+\|W^{(3)}_0\|_{\rm op}
                 +\sum_{\text{root vectors }v}\|v\|_{n,2}.
 \tag{17}
\]
Every finite moment of \(K_n\) is bounded independently of width and
\(\epsilon\in[0,1]\). For root vectors this follows from Jensen:
for \(p\ge2\), \(\mathbb E\|v\|_{n,2}^p\le
n^{-1}\sum_i\mathbb E|v_i|^p\). For the matrices, a \(1/4\)-net
of the unit sphere has at most \(9^n\) points by the disjoint-ball
volume bound. Approximating each of the two arguments in a bilinear
form bounds the operator norm by twice the maximum on that net.
Each fixed bilinear form has variance \(1/n\). Hence
\[
 \mathbb P(\|W_0\|_{\rm op}>t)
     \le 2\exp(2n\log9-nt^2/8)
     \le 2\exp(-nt^2/16),\qquad t\ge10.
 \tag{18}
\]
Integrating this tail proves the asserted moment bounds.

Finite induction gives a polynomial \(P\), with nonnegative
coefficients depending on the fixed graph but not on width or
\(\epsilon\), such that every vector node \(x\) and scalar node
\(c\) satisfy, for every parameter direction \(v\),
\[
 \|x\|_{n,2}\le P(K_n),\quad
 \|D x(g_n)[v]\|_2\le P(K_n)\|v\|_2,
\]
\[
 |c|\le P(K_n),\quad
 |Dc(g_n)[v]|\le n^{-1/2}P(K_n)\|v\|_2.
 \tag{19}
\]
Constants have derivative zero. Here and below a larger polynomial
can replace earlier ones to cover the finitely many nodes. The
induction has the following explicit estimates:

* A root vector has a linear parameter map of bounded operator norm.
  A coordinate map of Lipschitz constant \(L\) bounds its RMS by its
  value at zero plus \(L\) times the sum of the input RMS norms, and
  bounds its differential by \(L\) times the input differentials.
* For an initial forward action,
  \[
  \|D(W_0x)[v]\|_2\le
    \|W_0\|_{\rm op}\|Dx[v]\|_2+
    n^{-1/2}\|v\|_2\|x\|_2.
  \]
  The identical estimate holds for its transpose, since
  \(\|D W_0[v]\|_{\rm op}\le\|v\|_2/\sqrt n\).
* For \(c=\langle x,y\rangle_n\), Cauchy--Schwarz gives
  \[
  |Dc[v]|\le n^{-1/2}
       (\|y\|_{n,2}\|Dx[v]\|_2+
        \|x\|_{n,2}\|Dy[v]\|_2).
  \]
  Polynomial scalar arithmetic preserves the scalar estimates.
* For a scalar-times-vector node,
  \[
  \|D(cx)[v]\|_2\le |c|\|Dx[v]\|_2+|Dc[v]|\|x\|_2.
  \]
  The \(n^{-1/2}\) from the scalar differential cancels the
  \(\sqrt n\) from the vector norm.

These estimates prove (19) without any inverse Gram matrix. For each
fixed width they also bound the values and derivatives by polynomials
in \(\|g_n\|_2\), verifying the integrability required in (16).

The programs are equivariant under independent permutations of the
three neuron populations, with both sample coordinates permuted
together. Their Gaussian initialization has this invariance. Thus
\(\mathbb E x_i^2=\mathbb E\|x\|_{n,2}^2\le c_0\) for a
finite scalar constant \(c_0\). In particular
\(|\mathbb E x_i|\le\sqrt{c_0}\). Also
\(\|\nabla x_i(g_n)\|_2\le P(K_n)\) by (19).
Apply (16) and the moment bounds for \(K_n\). For every fixed
\(p<\infty\), every vector node, and every coordinate,
\[
 \sup_{n\ge1,\,0\le\epsilon\le1}\mathbb E|x_i|^p<\infty,
 \qquad
 \sup_{n,\epsilon}\mathbb E\|x\|_{n,p}^p<\infty.
 \tag{20}
\]
The conclusion holds for finite joint tuples as well. It applies to
the actual empirical-feedback program, its deterministic-coefficient
oracle, and their query-noise perturbations. It is a moment estimate
for these fixed random programs, not a bounded \(L^p\) operator norm
for an arbitrarily queried Gaussian matrix.

## 4. Exact conditioning and polynomial empirical induction

First consider a program with deterministic scalar coefficients and
positive definite limiting query Grams. For one initial matrix write
the old observations as \(WV=Y\) and \(W^TU=Q\). Given the preceding
transcript \(\mathcal F\), the exact conditional law is
\[
 W\mid\mathcal F\ \overset d=
 Y(V^TV)^{-1}V^T+
 U(U^TU)^{-1}Q^TP_{V^\perp}
       +P_{U^\perp}\widetilde W P_{V^\perp},
 \tag{21}
\]
where \(\widetilde W\) is independent with the original entry law.
Empty observation families contribute zero terms. To verify (21),
vectorize the Gaussian entries: orthogonal projection onto the
linear constraint space is the conditional mean, and the orthogonal
Gaussian component is independent. The displayed mean satisfies both
constraints because \(U^TY=Q^TV\); the displayed residual is precisely
the component annihilated by both constraint families.

Adaptivity does not add constraints. At a new query the input is
measurable with respect to the old transcript. Conditional on that
transcript, observing its answer adds a linear constraint only on the
queried matrix. Induction therefore preserves independence of the two
conditional residual matrices. Revealing an independent auxiliary root
or applying a coordinate instruction does not change this reasoning.

For a new forward input \(h\), let
\[
 \alpha_n=(V^TV)^{-1}V^Th,\quad h_\perp=h-V\alpha_n,\quad
 \beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n),\quad
 \sigma_n=\|h_\perp\|_{n,2}.
\]
Then
\[
 Wh\mid\mathcal F\ \overset d=
        Y\alpha_n+U\beta_n+\sigma_n P_{U^\perp}g,
 \tag{22}
\]
with a fresh iid standard Gaussian vector \(g\). The reverse rule is
obtained by interchanging input and output populations, \(V,Y\) with
\(U,Q\), and \(W\) with \(W^T\).

### 4.1 The discarded projection is small in every finite moment

Let \(P\) be any \(\mathcal F\)-measurable orthogonal projection
of rank at most the fixed number \(J\) of past calls. Its diagonal
satisfies \(0\le P_{ii}\le1\) and \(\sum_iP_{ii}\le J\). Thus,
for every \(p\ge2\),
\[
 \mathbb E[\|\sigma_n Pg\|_{n,p}^p\mid\mathcal F]
   =\frac{m_p\sigma_n^p}{n}\sum_iP_{ii}^{p/2}
   \le \frac{m_pJ\sigma_n^p}{n}.
 \tag{23}
\]
Since \(\sigma_n\le\|h\|_{n,2}\), (20) bounds the expectation of
the right side by \(C_p/n\). For \(p<2\), use
\(\|x\|_{n,p}\le\|x\|_{n,2}\). This estimate requires no
bound on the leverage of individual coordinates and no inverse-Gram
limit. It supplies exactly the higher-moment projection control that
a second-moment argument alone would not supply.

### 4.2 Conditional averaging for unbounded tests

After dropping the projection in (22), the new coordinate has the
form \(m_i+\sigma_ng_i\), where \(m_i\) is a linear combination of
old coordinates. Convergent Gram entries and positive definiteness
give convergence in probability of the coefficients and \(\sigma_n\)
to deterministic values. They are consequently bounded with probability
arbitrarily close to one.

Let \(T\) be a continuous test of the old tuple and the new answer,
with \(|T(x)|\le c_T(1+|x|^d)\); enlarge \(d\) to an integer if
necessary. On a bounded-coefficient event, independence of the \(g_i\)
conditional on the transcript bounds the conditional variance of its
empirical average by
\[
 \frac{c_{T,L}}n\left(1+\frac1n\sum_i|\text{old tuple}_i|^{2d}\right),
 \tag{24}
\]
where \(L\) bounds the coefficients. The parenthesis is bounded in
probability by (20), so conditional
Chebyshev gives concentration about the conditional expectation. That
expectation is the old empirical average of the Gaussian-integrated
test. This integrated test is continuous in the old tuple and the
coefficients, and has polynomial growth uniformly on compact coefficient
sets. On a fixed ball, continuity is uniform. Outside the ball the
error is bounded using, for any \(q>d\),
\[
 \frac1n\sum_i |x_i|^d\mathbf1_{|x_i|>L}
       \le L^{d-q}\frac1n\sum_i|x_i|^q.
 \tag{25}
\]
Gaussian moments provide the identical bound for the integrated
variable. Consequently induction for the old tuple implies convergence
of this conditional expectation to the claimed Gaussian expectation.

Restoring the projection does not change the result. For polynomial
tests this also follows directly from
\[
 |P(x)-P(y)|\le C_P|x-y|(1+|x|^{d-1}+|y|^{d-1})
 \tag{26}
\]
and Hölder, using (23). For a general continuous polynomial-growth
test, restrict both tuples to a ball, use uniform continuity and the
small empirical difference, then use (25) for the tails. The tuple
with the projection dropped has bounded empirical moments in
probability, since its coefficients are tight and its old coordinates
and fresh Gaussians have such moments. The original tuple has (20).

The root step is the iid law of large numbers; it follows here directly
from the variance bound for a test with finite second moment. Revealing
an auxiliary Gaussian root is the same conditional averaging argument.
Coordinate instructions preserve the induction because composing a
polynomial-growth test with a globally Lipschitz map again has
polynomial growth. This proves joint empirical convergence for every
fixed nonsingular program, including all scalar contractions.

## 5. Derivation of the source/response rule, including both orientations

For one matrix let the old forward inputs be \(v_r\), with forward
sources \(\xi_r\), and the old reverse inputs be \(u_s\), with
reverse sources \(\zeta_s\). The claimed generic rule for a new
forward answer is
\[
 W h\ \leadsto\ \xi_h+
                 \sum_s u_s\,\mathbb E[\partial_{\zeta_s}h],
 \qquad \mathbb E[\xi_h\xi_{v_r}]=\mathbb E[h v_r],
 \quad \mathbb E\xi_h^2=\mathbb E h^2.
 \tag{27}
\]
The reverse answer is
\[
 W^T u\ \leadsto\ \zeta_u+
                 \sum_r v_r\,\mathbb E[\partial_{\xi_r}u],
 \qquad \mathbb E[\zeta_u\zeta_{u_s}]=\mathbb E[u u_s],
 \quad \mathbb E\zeta_u^2=\mathbb E u^2.
 \tag{28}
\]
Only available opposite-orientation inputs occur in either formula.

For completeness, suppose the old forward decompositions are
\(y_r=\xi_r+\sum_sD_{rs}u_s\), where
\(D_{rs}=\mathbb E\partial_{\zeta_s}v_r\), with unavailable
derivatives set to zero. Let \(h_\perp=h-\sum_r\alpha_rv_r\) be
the limiting least-squares residual. Old reverse answers have the
form \(q_s=\zeta_s+\) a linear combination of old forward inputs.
Orthogonality of \(h_\perp\) to those inputs gives
\[
 \mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]
For a centered Gaussian vector \(\zeta\) of covariance \(\Gamma_U\),
\[
 \mathbb E[\zeta f]=\Gamma_U\mathbb E[\nabla f].
 \tag{29}
\]
This identity follows by one-dimensional integration by parts in
independent standard Gaussian coordinates: write \(\zeta=Ag\),
integrate \(g_j f(Ag)\), and apply the chain rule. It is valid for
singular \(\Gamma_U=AA^T\) too. In the present deterministic
program, coordinate expressions have linear growth in the finite
root/source tuple and their first derivatives are bounded on compact
sets of deterministic coefficients. Gaussian integrability makes the
boundary terms vanish. Conditioning on the other independent source
groups and roots is therefore legitimate.

In the nonsingular case \(\Gamma_U\) is invertible. Equations
(22) and (29) give
\[
 \beta=\mathbb E\nabla_\zeta h
          -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]
Substituting the old decompositions into the limiting conditional
mean cancels the second term, giving (27), with
\(\xi_h=\sum_r\alpha_r\xi_r+\|h_\perp\|_{L^2}g_{\rm new}\).
The new scalar Gaussian is independent of all old roots and sources.
Projection orthogonality gives precisely the two covariance identities
in (27). Applying the same computation to \(W^T\) proves (28).
Induction maintains mutual independence of the four Gaussian groups:
each new source is a deterministic linear combination of earlier
sources in its own group and a Gaussian independent of all old groups.

This argument differentiates through complete earlier expressions,
including earlier uses of the other matrix. It neither replaces a
transpose by independent noise nor subtracts the squared response
from the source variance. The innovation at an individual conditional
step has residual variance \(\mathbb E h_\perp^2\); the full source
in (27) has variance \(\mathbb E h^2\).

## 6. Singular Grams and polynomial moments: an actual transfer proof

Add \(\epsilon g^{\rm in}\) to the input of each initial matrix
call, with a fresh independent root revealed just before that call.
Use the original matrices in both perturbed and unperturbed programs.
This changes the query only; it does not insert noise into the
explicit learned rank-one factors. At \(\epsilon>0\), the new
limiting query is \(h+\epsilon g^{\rm in}\), with this root
independent of the old same-orientation query span and of \(h\).
Its squared distance from that span is the original squared distance
plus \(\epsilon^2\). Thus every successive limiting Gram Schur
complement is positive. Sections 4--5 apply. At finite width greater
than the number of old inputs, the fresh Gaussian also makes the
corresponding finite Gram nonsingular almost surely.

### 6.1 Comparing the finite-width programs

Couple the two graphs with the same matrices and roots, including
unused auxiliary roots in the unperturbed graph. Bounds (19) and the
global Lipschitz coordinate inequalities give, by finite induction,
\[
 \|x_n^\epsilon-x_n^0\|_{n,2}\le\epsilon P(K_n)
 \tag{30}
\]
for every vector node. This induction is also valid with empirical
quadratic feedback: a contraction difference satisfies
\[
 |\langle x,y\rangle_n-\langle\widetilde x,\widetilde y\rangle_n|
 \le\|x-\widetilde x\|_{n,2}\|y\|_{n,2}
     +\|\widetilde x\|_{n,2}\|y-\widetilde y\|_{n,2},
 \tag{31}
\]
and scalar-times-vector differences then use the RMS bounds (19).
Polynomial scalar maps have polynomial Lipschitz bounds on the
bounded scalar ranges supplied by (19). In particular (30) has
uniformly bounded moments after division by \(\epsilon\).

For \(p>2\), choose \(q>p\) and \(0<\theta<1\) with
\(1/p=\theta/2+(1-\theta)/q\). The finite-measure Hölder
interpolation inequality gives
\[
 \|x_n^\epsilon-x_n^0\|_{n,p}
 \le \|x_n^\epsilon-x_n^0\|_{n,2}^{\theta}
       \|x_n^\epsilon-x_n^0\|_{n,q}^{1-\theta}.
 \tag{32}
\]
The second factor is bounded in probability uniformly in width and
\(\epsilon\), by (20) and Markov's inequality. The first tends to
zero uniformly in probability as \(\epsilon\downarrow0\), by
(30). For \(p\le2\), (30) suffices. Consequently for every \(p\)
and \(\eta>0\),
\[
 \lim_{\epsilon\downarrow0}\sup_n
  \mathbb P(\|x_n^\epsilon-x_n^0\|_{n,p}>\eta)=0.
 \tag{33}
\]
Equations (25)--(26) transfer the same assertion to empirical averages
of any fixed continuous polynomial-growth test. Thus the transfer
uses both finite-width all-order moments and an actual projection
estimate, not only an RMS localization comparison.

### 6.2 Passing the scalar law through a rank drop

Use (27)--(28), which do not involve an inverse covariance, to pass
\(\epsilon\downarrow0\) in the scalar recursion. Here are the
details ensuring that this is not an inverse-limit assumption.

Inductively the finitely many already chosen coefficients converge
and hence lie in a compact set. Coordinate expressions in the
already available roots and source slots then have uniformly bounded
first derivatives, linear growth, and continuous dependence on those
coefficients. Their formal first derivatives are finite sums of
products of the continuous bounded first partial derivatives of
the coordinate maps in (14)--(15), with deterministic coefficients.
They are therefore continuous in the arguments and coefficients,
and bounded uniformly on compact coefficient sets.
The extra input-root term \(\epsilon g^{\rm in}\) has these same
properties and has zero formal derivative with respect to the old
opposite-orientation sources.

The next source covariance entries are second moments of these input
expressions. Suppose the already constructed covariance matrices
converge, say \(\Gamma_j\to\Gamma\). Their positive semidefinite
square roots converge too. Indeed their operator norms are bounded
by \(\sqrt{\sup_j\|\Gamma_j\|_{\rm op}}\), so every subsequence
has a convergent further subsequence in this fixed finite-dimensional
matrix space. Its limit \(B\) is positive semidefinite and satisfies
\(B^2=\Gamma\). Such a root is unique: \(B\) commutes with
\(\Gamma\), and on each \(\lambda\)-eigenspace of \(\Gamma\)
its nonnegative eigenvalues must all equal \(\sqrt\lambda\).
Thus every subsequential limit is \(\Gamma^{1/2}\), which proves
convergence. Couple the finite source vectors by these square
roots applied to the same standard Gaussian vector, keeping the root
vectors independent. The coordinate expressions converge in every
finite \(L^p\), by their uniform linear-growth bounds and Gaussian
moments. Their formal first derivatives converge by dominated
convergence, since their bounds are uniform on the compact coefficient
set. Thus the next input covariances and expected derivatives converge.

Appending a source preserves positive semidefiniteness, because its
entire same-orientation covariance is the Gram matrix of the query
inputs. This completes the induction: the next full source covariance
has a square-root coupling of the stated kind, and the next response
coefficient has a finite limit. Such couplings can be chosen anew for
each finite induction step; a consistent extension of the old
particular coupling is unnecessary for convergence of its law.

At \(\epsilon=0\) the auxiliary roots disappear from all expressions.
Combining this scalar \(L^p\) convergence, the positive-noise
empirical theorem, and (33) proves the unperturbed theorem. For a
fixed test, this is just the triangle inequality between its empirical
averages at zero and positive noise and its expectations under the
two scalar laws; first take the width limit and then decrease the
noise. No growing sequence of regularized queries is involved.

Finally, singularity does not permit deletion of formal slots. If
\(\Gamma=\mathbb E[uu^T]\) and \(v\in\ker\Gamma\), then
\(\mathbb E(u^Tv)^2=0\), so \(u^Tv=0\) almost surely. A change
of derivative coefficient by such a null vector cannot change the
contracted response in (27) or (28). Formula (29) likewise identifies
the response independent of an off-support smooth extension, up to
this null space. The displayed explicit-expression derivative remains
the convention for computing the individual coefficients. This covers
zero queries, redundant queries, and \(\rho=\pm1\), with no
nondegeneracy hypothesis.

## 7. Learned rank terms and empirical scalar feedback

The exact finite-width unrolling is
\[
 W^{(\ell)}_kh^{(\ell-1)}_{ka}
  =W^{(\ell)}_0h^{(\ell-1)}_{ka}
   +\sum_{r<k,b}\gamma_{rb}\delta^{(\ell)}_{rb}
          \langle h^{(\ell-1)}_{rb},h^{(\ell-1)}_{ka}\rangle_n,
 \tag{34}
\]
\[
 (W^{(\ell)}_k)^T\delta^{(\ell)}_{ka}
  =(W^{(\ell)}_0)^T\delta^{(\ell)}_{ka}
   +\sum_{r<k,b}\gamma_{rb}h^{(\ell-1)}_{rb}
          \langle\delta^{(\ell)}_{rb},\delta^{(\ell)}_{ka}\rangle_n.
 \tag{35}
\]
First replace each scalar contraction, in causal instruction order,
by the expectation under the scalar law already constructed. This
defines a deterministic-coefficient oracle. A contraction feeding a
new query uses only existing inputs; a contraction needed after a
matrix answer is selected after that answer's law has been constructed.
Thus the oracle is not defined by an implicit equation. Sections 4--6
give its empirical law and convergence of all its contractions.

Couple the actual and oracle programs using the original matrices
and roots. On \(K_n\le L\), all vector RMS norms and scalar values
of the actual graph are bounded by (19); the finitely many fixed
oracle coefficients and oracle RMS norms are bounded as well. At a
contraction use (31), plus the error between the oracle empirical
contraction and its limiting expectation. At a scalar-times-vector
node use the product difference inequality; at the other nodes use
the Lipschitz and operator bounds. Since the graph is finite and
causal, induction bounds every RMS discrepancy by a finite constant
depending on \(L\) times the sum of the finitely many oracle
contraction errors. Those errors tend to zero in probability.
Finally increase \(L\); (17)--(18) show its complement has arbitrarily
small probability. All RMS discrepancies therefore vanish.

The all-order moment bounds (20) apply separately to both programs.
Interpolation (32), followed by (25)--(26), upgrades this comparison
to every finite empirical moment and every continuous polynomial-growth
test. This proves the actual-feedback conclusion, not merely an
oracle conclusion.

The predictions \(\langle w_k,h^{(3)}_{ka}\rangle_n\) and all
fixed polynomial functions of the convergent contractions converge
as observables. The contraction coefficients occurring in (34)--(35)
are replaced by their deterministic expectations in the scalar law.
The response derivatives hold those selected values fixed; no
derivative of the selection of an empirical contraction is inserted
into (12)--(13).

Applying (27) to the initial-matrix part of (34), and (28) to the
initial-transpose part of (35), gives exactly (7), (9), and (10),
with coefficients (12)--(13). Equations (6) and (8) are the direct
coordinate updates. Their input second moments give (11). This
establishes the announced scalar law for both transposes.

For clarity, convergence against continuous polynomial-growth tests
also implies the Wasserstein assertion in the lemma without an
extra moment assumption. For order \(p\), (25) with \(q>p\) gives
uniformly small empirical \(p\)-tails in probability. On a large
ball partition into finitely many cells of small diameter whose
boundaries have zero limiting mass. Convergence for bounded continuous
tests gives convergence of cell masses. Match common mass in the
same cell, couple the unmatched bounded mass arbitrarily, and couple
tail mass through the origin. The resulting transport cost is bounded
by the cell-diameter cost, the vanishing unmatched bounded cost, and
a constant times the two \(p\)-tails. Taking these limits in that
order proves convergence in Wasserstein order \(p\).

## 8. The cap derivative, the current return, and zero initial slots

The full top derivative, for every available formal source slot, is
\[
 \frac{\partial\delta^{(3)}_{ka}}{\partial\xi^{(3)}_{vb}}
 =\tau'_w(\mathsf W_k)\phi'(Z^{(3)}_{ka})
                  \frac{\partial\mathsf W_k}{\partial\xi^{(3)}_{vb}}
  +\tau_w(\mathsf W_k)\phi''(Z^{(3)}_{ka})
                  \frac{\partial Z^{(3)}_{ka}}{\partial\xi^{(3)}_{vb}}.
 \tag{36}
\]
In particular one must retain the readout derivative term, including
\(\tau'_w\). For past slots
\[
 \frac{\partial\mathsf W_k}{\partial\xi^{(3)}_{vb}}
   =\sum_{r<k,c}\gamma_{rc}\phi'(Z^{(3)}_{rc})
                        \frac{\partial Z^{(3)}_{rc}}
                             {\partial\xi^{(3)}_{vb}}.
 \tag{37}
\]
For the current slots this derivative is zero, while
\(\partial Z^{(3)}_{ka}/\partial\xi^{(3)}_{kb}=\mathbf1_{a=b}\).
Hence
\[
 B^{(3)}_{ka,kb}=\mathbf1_{a=b}
               \mathbb E[\tau_w(\mathsf W_k)\phi''(Z^{(3)}_{ka})].
 \tag{38}
\]
At the middle layer the chain rule through the complete expression is
\[
 \partial\delta^{(2)}_{ka}
   =\phi''(Z^{(2)}_{ka})\tau_2(q^{(2)}_{ka})\,\partial Z^{(2)}_{ka}
    +\phi'(Z^{(2)}_{ka})\tau'_2(q^{(2)}_{ka})\,\partial q^{(2)}_{ka}.
 \tag{39}
\]
For a current forward source,
\(\partial_{\xi^{(2)}_{kb}}Z^{(2)}_{ka}=\mathbf1_{a=b}\) and
\[
 \partial_{\xi^{(2)}_{kb}}q^{(2)}_{ka}
      =B^{(3)}_{ka,kb}\phi'(Z^{(2)}_{kb}).
\]
Thus the second transpose has the current coefficient
\[
 B^{(2)}_{ka,kb}
   =\mathbf1_{a=b}\mathbb E[\phi''(Z^{(2)}_{ka})\tau_2(q^{(2)}_{ka})]
    +B^{(3)}_{ka,kb}\mathbb E[\phi'(Z^{(2)}_{ka})
                \tau'_2(q^{(2)}_{ka})\phi'(Z^{(2)}_{kb})].
 \tag{40}
\]
The last term is the current return through the top matrix. By (38)
it is diagonal in the *formal* current sample slots, even when their
Gaussian covariance is singular. Sample correlations enter the
expectations and source covariances; they do not replace a formal
partial derivative by a covariance-weighted derivative.

The bottom update likewise has, for any formal derivative,
\[
 \partial\delta^{(1)}_{ka}
  =\phi''(Z^{(1)}_{ka})\tau_1(q^{(1)}_{ka})\partial Z^{(1)}_{ka}
   +\phi'(Z^{(1)}_{ka})\tau'_1(q^{(1)}_{ka})\partial q^{(1)}_{ka}.
 \tag{41}
\]
Together with (6), this specifies the bottom contributions to (12);
no uncapped backward factor has been substituted into them.

At step zero, \(\mathsf W_0=0\) and \(\tau_w(0)=0\), so
\(\delta^{(3)}_0=q^{(2)}_0=\delta^{(2)}_0=q^{(1)}_0=0\).
Both reverse source covariance blocks at that step are exactly zero.
Nevertheless the slots \(\zeta^{(2)}_{0a},\zeta^{(1)}_{0a}\) remain
in the displayed coordinate expressions, and later formal derivatives
through them need not be zero. Equations (27)--(33) justify these
slots without a positive-variance assumption. Multipliers belonging
to covariance null spaces cancel in the contracted answers as proved
in Section 6. Neither zero initialization nor \(\rho=\pm1\)
requires dropping a source slot or changing the derivative convention.

This proves the fixed-program identification and polynomial-moment
extension requested in step 2 of the supplied bootstrap plan. With
\(\gamma_{rb}=(\Delta/2)y_b\), equations (6)--(13) are exactly
equations (2)--(3) and their source covariances in the supplied local
Gaussian-response file. In particular this proves that its finite law
is well defined and its displayed formal derivative expectations
exist, at each fixed choice of mesh and finite caps. Its separate
primal hypotheses (4)--(5) have not been established here. All
mesh-uniform response estimates, time-continuum passages, population
flow construction, and removal of the three caps remain outside this
lemma.
