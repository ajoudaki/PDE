# Direct compact learning without a realized dense network

## Outcome

The requested strict root-width theorem is **not proved**.  In particular,
this study does not establish a directly initialized model with
polylogarithmic retained storage and the following guarantee.  Here
\(C_{\rm data,\delta}\) may depend on the fixed dataset, architecture, and
confidence, but not on width or time:

\[
 \Pr\!\left\{
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_C(t,x)-f_n(t,x)|\le \frac{C_{\rm data,\delta}}{\sqrt n}
 \right\}\ge 1-\delta .                                  \tag{1}
\]

It does establish three positive results in the orthogonal-data setting.  The
all-time statements use the small-label condition stated in Section 1.

1. There is an explicit family of finite, directly initialized, autonomous
   models with trainable hidden blocks that converges to the deterministic
   nonlinear population learning flow.  The convergence is uniform over
   physical time, the whole input sphere, and the fitted endpoint.  Combining
   this with the maintained fixed-horizon finite-width limit and the
   finite-width fitting and endpoint-tail estimate gives a direct all-time
   comparison with a fresh dense network at every **fixed** error tolerance.
   The construction never forms a width-\(n\) network.
2. There is a fully explicit \(m\)-scalar direct model whose all-time,
   whole-sphere population error is at most \(C_{\rm data}Y^3\), where
   \(Y=\|y\|_2/\sqrt m\).  This second model freezes the hidden features, so
   it is a controlled small-label baseline rather than a solution of (1).
   Against a fresh dense run its proved error is
   \(C_{\rm data,\delta}(Y/\sqrt n+Y^3)\).
3. At initialization, every training-to-query tangent-kernel row has,
   uniformly over the query sphere, finite-width fluctuation \(O(n^{-1/2})\)
   and bias \(O(n^{-1})\).
   Residual damping reduces the full all-time dense-to-population theorem to
   one composite residual-weighted tangent-kernel source estimate, with
   fluctuation and bias controlled separately and no extra \(\log n\) loss.

The first result has no proved tolerance-to-order bound.  Therefore it gives
neither a certified order choice from \(n\), nor a polylogarithmic storage
bound, nor a construction-time bound as a function of \(n\).  Two independent
quantitative bridges remain open: effective discretization of the population
flow and a strict root-width dense-to-population theorem, including finite-width
bias.

## 1. Common setup

Put \(v=x/\sqrt d\), and write the dataset as
\(\{(v_a,y_a)\}_{a=1}^m\), where \(v_a=x_a/\sqrt d\).  The training
directions are orthonormal.  The dense reference is

\[
 h_n(v)=\tanh(A_nv),\qquad
 g_n(v)=\tanh(W_nh_n(v)),\qquad
 f_n(v)=\frac{w_n^Tg_n(v)}n,                              \tag{2}
\]

where initially the entries of \(A_n\) are independent \(N(0,1)\), the
entries of \(W_n\) are independent \(N(0,1/n)\), the two matrices are
independent, and \(w_n=0\).  It follows gradient flow of
\(m^{-1}\sum_a(f_n(v_a)-y_a)^2\) with block mobilities \((n,1,n)\).
The comparison norm used below is

\[
 \|f-g\|_*
 :=\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}|f(t,v)-g(t,v)|, \tag{3}
\]

where \(t=\infty\) is the fitted endpoint.  All comparisons retain the same
physical time.

Let \(f_\infty\) be the unique deterministic population action flow from the
maintained orthogonal-data theorem.  If \(G\) is standard Gaussian, define

\[
 \gamma
 =\mathbb E\tanh^2\!\left(
     \sqrt{\mathbb E\tanh^2(G)}\,G\right)>0 .             \tag{4}
\]

For the present orthogonal tanh data, \(\gamma I_m\) is the initialized
population top-feature Gram.  The all-time results use

\[
                       Y\le c\,\gamma/m,                  \tag{5}
\]

for a sufficiently small fixed constant \(c\).  Arbitrary label signs are
allowed.  Constants denoted by \(C_{\rm data}\) have the same convention
without confidence dependence.  Whenever \(Y\) is displayed explicitly,
the coefficient is uniform over all label magnitudes and signs satisfying
(5); its remaining dependence is on the fixed inputs and architecture.

The full-time direct-construction results below remain in this orthogonal
setting.  Orthogonality is used essentially by the clock argument, so no
broader data theorem is claimed.

## 2. A direct nonlinear autonomous hierarchy

### 2.1 Initialization from the law

Choose finite dictionaries of lengths \(r_1,r_2\) on the two population
spaces.  Their entries are bounded cylinder functions generated from the
first-row Gaussian coordinates and finite forward and reverse words of the
single initialized Gaussian middle action.  Reverse words use the actual
adjoint of the same action; they are not independently resampled.

Write the two dictionary vectors as \(\psi_1,\psi_2\).  Gaussian integration
computes

\[
 b_\ell=\bigl(\mathbb E[\psi_\ell\psi_\ell^T]+\eta I\bigr)^{-1/2}\psi_\ell,
 \qquad
 M_0=\mathbb E\!\left[b_2(\mathcal A_0b_1)^T\right],     \tag{6}
\]

where \(\eta>0\) is a ridge and \(\mathcal A_0\) is the initialized
population action.  Every entry in (6) is a finite Gaussian source/response
program determined by the dataset and initialization law.

These programs are evaluated without a population-response oracle.  At a
fixed dictionary, the source/response recursion produces a finite joint
Gaussian integral for each requested entry.  One truncates its Gaussian
coordinates with an explicit tail allowance, applies an ordinary finite
deterministic rule on the resulting box, and then performs the finite matrix
diagonalizations in (6).  The same compiled joint program is used for forward
and reverse calls, so Gaussian reuse is preserved.

Next apply positive deterministic quadrature to the laws of \((b_1,G_d)\)
and \(b_2\), where \(G_d\sim N(0,I_d)\).  Denote the lower nodes and weights
by \((b_i,g_i,\pi_i)\), \(1\le i\le p_1\), and the upper ones by
\((\beta_j,\rho_j)\), \(1\le j\le p_2\).  Both sets of weights are positive
and sum to one.  This is the entire preprocessing input to the trained model.
It contains no realized width-\(n\) row, matrix, feature, derivative, path, or
endpoint.

For fixed orders, (6) requires

\[
 \frac{r_1(r_1+1)}2+\frac{r_2(r_2+1)}2+r_1r_2             \tag{7}
\]

scalar Gaussian integrals, two matrix inverse square roots, and construction
of the two positive rules.  The present proof supplies no bound on the number
of scalar quadrature evaluations or required bits as a function of \(n\) or a
requested tolerance.  Thus (7) is an operation inventory, not an efficient
preprocessing theorem.  At fixed numerical rules, its arithmetic cost is the
total number of quadrature-node evaluations times the finite program lengths,
plus \(O(r_1^3+r_2^3)\) linear algebra and the cost of constructing the two
positive rules.  No width-\(n\) array occurs even temporarily.

### 2.2 State, prediction, and evolution

The moving variables are lower rows \(u_i\in\mathbb R^d\), upper readouts
\(c_j\in\mathbb R\), and one matrix \(M\in\mathbb R^{r_2\times r_1}\).
Initialize

\[
                     u_i=g_i,\qquad c_j=0,\qquad M=M_0.   \tag{8}
\]

For a unit query \(v\), define locally

\[
\begin{aligned}
 h_i(v)&=\tanh(u_i^Tv),
 &a(v)&=\sum_i\pi_i b_i h_i(v),\\
 H_j(v)&=\tanh(\beta_j^TMa(v)),
 &f_C(v)&=\sum_j\rho_jc_jH_j(v),\\
 e(v)&=\sum_j\rho_j\beta_jc_j[1-H_j(v)^2].
\end{aligned}                                             \tag{9}
\]

With current training residuals \(R_a=f_C(v_a)-y_a\), evolve

\[
\begin{aligned}
 \dot u_i
 &=-\frac2m\sum_aR_a[1-h_i(v_a)^2]
       \bigl[b_i^TM^Te(v_a)\bigr]v_a,\\
 \dot c_j
 &=-\frac2m\sum_aR_aH_j(v_a),\\
 \dot M
 &=-\frac2m\sum_aR_a e(v_a)a(v_a)^T .
\end{aligned}                                             \tag{10}
\]

Equations (9)--(10) are autonomous and restartable from the retained state.
Both hidden layers are trained: the lower rows and middle matrix are governed
by (10).  The reused
forward/adjoint structure is represented by \(M\) and \(M^T\).  The exact
energy identity is

\[
 \frac d{dt}\frac1m\sum_aR_a^2
 =-\sum_i\pi_i\|\dot u_i\|_2^2
  -\sum_j\rho_j|\dot c_j|^2-\|\dot M\|_F^2\le0 .          \tag{11}
\]

There is no stored clock history, playback table, dense seed, or response
oracle.

### 2.3 Moving state, fixed storage, and runtime work

For the chosen four orders, the moving state has

\[
                         p_1d+p_2+r_1r_2                  \tag{12}
\]

real coordinates.  The fixed retained marks, weights, and dataset have

\[
              p_1(r_1+1)+p_2(r_2+1)+m(d+1)              \tag{13}
\]

real coordinates.  Adding (12) and (13) is the complete retained-storage
count.  One evaluation of (10), streaming over the training set, costs

\[
 O\!\left(m\{p_1(d+r_1)+p_2r_2+r_1r_2\}\right)          \tag{14}
\]

scalar operations.  The count is independent of elapsed training time.
No claim is made here about numerical ODE integration error.

For a clean external interface, let \(q=\max\{r_1,r_2\}\) be the dictionary
rank and let \(p=\max\{p_1,p_2\}\) be the number of quadrature nodes per
population.  Then moving state, fixed storage, total retained storage, and
one right-side evaluation are respectively bounded by

\[
 pd+p+q^2,\qquad
 2p(q+1)+m(d+1),\qquad
 O\!\left(p(q+d)+q^2+m(d+1)\right),\qquad
 O\!\left(m\{p(q+d)+q^2\}\right).                       \tag{15}
\]

The rank \(q\), node count \(p\), ridge \(\eta\), quadrature refinement, and
arithmetic precision are all genuine resolution choices.  The current theorem
does not provide a sufficient joint schedule from \(n\) or from a requested
error.

### 2.4 What is proved

There is a nested refinement of the dictionaries, ridge, and positive rules
for which

\[
                          \|f_C-f_\infty\|_*\longrightarrow0 . \tag{16}
\]

This includes the entire sphere, all finite physical times, both fitted
endpoints, and the tails approaching them.  The proof first couples each
finite quadrature to its mark law, then lets the dictionary projections tend
strongly to the identity on the compact set of forward, adjoint, and learned
rank-source fields.  The key stability step uses orthogonality and the tanh
clock

\[
 \Psi(z)=\frac z2+\frac{\sinh(2z)}4,
 \qquad X_a=\Psi(z_a)-\Psi(z_a(0)),
\]

where \(z_a\) is one lower preactivation on training input \(v_a\).  Because
\(\Psi'=1/\tanh'\), the equation for \(X_a\) contains the reverse
field without multiplying it by a changing lower gate.  This removes the
otherwise invalid attempt to beat a Gronwall factor using only an \(L^2\)
tail.  Energy dissipation, the initialized Gram margin, and (5) then give
order-uniform fitting and endpoint tails.

Combining (16) with the maintained finite-width limit and the finite-width
fitting estimate gives the following complete, but non-effective, comparison:
for every fixed \(\varepsilon>0\) and \(0<\delta<1\), sufficiently refined
orders in (6)--(10) and a finite threshold
\(N_{\rm data}(\varepsilon,\delta)\) exist such that, for every
\(n\ge N_{\rm data}(\varepsilon,\delta)\), an independent fresh dense run
satisfies

\[
                 \Pr\{\|f_C-f_n\|_*\le\varepsilon\}\ge1-\delta . \tag{17}
\]

To obtain (17), choose a fixed time after which both systems are uniformly
close to their own endpoints; on the preceding compact interval use (16) and
the maintained convergence in probability.  A finite input net and the
uniform input-Lipschitz bounds upgrade the maintained finite-query statement
to the fixed-dimensional sphere.  Comparing both endpoints through their
values at that fixed time gives the remaining all-time interval.

The threshold in (17), the sufficient refinement orders, and their bit cost
are unquantified.  In particular, (17) does **not** give a certified algorithm
which receives \(\varepsilon\) and returns the orders.  It is a consistency
theorem for an explicit law-only hierarchy, not the requested efficiency
theorem.

## 3. A complete \(m\)-state baseline

The orthogonal-data symmetry yields a smaller result with an explicit order
choice.  If \((G,G')\) are standard Gaussians of correlation \(s\), set

\[
 k_1(s)=\mathbb E[\tanh(G)\tanh(G')].                    \tag{18}
\]

If \((U,U')\) are centered Gaussian with both variances \(k_1(1)\) and
covariance \(s\), set \(k_2(s)=\mathbb E[\tanh(U)\tanh(U')]\).  Then
\(\gamma=k_2(k_1(1))\).  The direct residual state and prediction are

\[
 \dot{\bar R}_a=-\frac{2\gamma}{m}\bar R_a,
 \qquad \bar R_a(0)=-y_a,                                \tag{19}
\]

\[
 \bar f(\bar R,v)
 =\frac1\gamma\sum_{a=1}^m
       k_2(k_1(v^Tv_a))(y_a+\bar R_a)
 =\frac{1-e^{-2\gamma t/m}}{\gamma}
       \sum_{a=1}^m k_2(k_1(v^Tv_a))y_a .                 \tag{20}
\]

The second expression in (20) is the closed form along (19); below,
\(\bar f(t,v)\) means \(\bar f(\bar R(t),v)\).
This model uses only the data and low-dimensional Gaussian integrals, stores
\(m\) moving scalars in addition to the dataset, and is autonomous and
restartable without retaining elapsed time.  An
independent audit verified

\[
                         \|\bar f-f_\infty\|_*
                         \le C_{\rm data}Y^3 .            \tag{21}
\]

Its training right-hand side costs \(O(m)\) operations, and a query costs
\(O(md)\) arithmetic plus \(m\) evaluations of the two fixed scalar kernels.
The theorem treats these scalar Gaussian integrals in exact-real arithmetic.
A numerical implementation can use ordinary low-dimensional quadrature; this
does not change the moving-state dimension, but its work and precision must
be chosen for the requested output tolerance and are not bounded here.

There is also a direct comparison with the fresh finite network.  Freeze that
network's two initialized hidden layers and train only its readout.  Its
entire trajectory is a smooth function of the initialized top-feature kernel.
The whole-sphere onset theorem in Section 4 controls that kernel at strict
root width, while the small-label stability argument bounds the difference
between the actual nonlinear dense flow and its own frozen-feature flow by
\(C_{\rm data,\delta}Y^3\).  Hence, for every fixed confidence and all
sufficiently large widths,

\[
 \Pr\!\left\{
   \|\bar f-f_n\|_*
   \le C_{\rm data,\delta}
        \left(\frac{Y}{\sqrt n}+Y^3\right)
 \right\}\ge1-\delta .
\]

This is a complete direct-to-dense theorem, including the endpoint, but on a
mixed width/label scale.  Equation (21) is only an upper bound; it does not
prove a nonzero cubic term.  For fixed nonzero labels the displayed estimate
does not tend to zero, and the small model omits hidden feature learning.  If
one instead imposes the narrower, width-dependent regime
\(Y=O(n^{-1/6})\), it gives the strict root-width target.  That shrinking-label
corollary is not the fixed-label theorem requested in (1).

## 4. What is already sharp at finite width

At initialization, zero readout makes the tangent kernel equal to the
top-feature Gram.  For a fixed training direction \(u\), write this kernel as
\(K_n^0(u,v)\) and its population value as \(K_\infty^0(u,v)\).  A direct
two-layer empirical-process calculation proves

\[
 \sup_{v\in S^{d-1}}
 |\mathbb E K_n^0(u,v)-K_\infty^0(u,v)|
 \le \frac{C_{\rm data}}n,
\]

and, for every fixed confidence,

\[
 \Pr\!\left\{
  \sup_{v\in S^{d-1}}
  |K_n^0(u,v)-\mathbb E K_n^0(u,v)|
  >\frac{C_{\rm data,\delta}}{\sqrt n}
 \right\}\le\delta .
\]

Thus both the whole-sphere root-width fluctuation and the smaller
finite-width bias are proved at the onset of training.  The initial
probability scale is not the obstruction.

There is also an exact dynamical reduction.  Residual damping shows that an
integrated, residual-weighted finite-versus-population tangent-kernel estimate
of order \(n^{-1/2}\), only up to time
\((m/\gamma)\log n\), implies the full all-time, whole-sphere and endpoint
bound with no additional logarithmic loss.  What remains unproved is that
dynamic kernel estimate.  The first missing fluctuation estimate is a
uniform fourth-moment bound for transported forward/adjoint responses; a
separate finite-size expansion is still needed for the dynamic bias.

## 5. The two missing quantitative bridges

The desired theorem would follow if both statements below were proved.

1. **Effective direct discretization.**  The initialization in Section 2,
   or another law-only construction, must select orders from \(n\) with all
   retained storage bounded by a fixed power of \(\log(en)\), and it must
   satisfy \(\|f_C-f_\infty\|_*\le C_{\rm data}/\sqrt n\).
2. **Fresh dense run versus population.**  Independently of the compact
   construction, the width-\(n\) dense flow must satisfy
   \(\|f_n-f_\infty\|_*\le C_{\rm data,\delta}/\sqrt n\) with probability
   at least \(1-\delta\), for all sufficiently large \(n\).

For the construction above, matching the existing compact model's order
would mean

\[
 q\le C_{\rm data}[\log(en)]^{3d/2+1},
 \qquad p\le C_{\rm data}q,
 \qquad
 \text{retained storage}\le
 C_{\rm data}[\log(en)]^{3d+2}.                           \tag{22}
\]

No such sufficient choices have been proved for the law-built model.
Conditional on an effective rank-\(q\) dynamic source certificate, generic
positive cubature for its fixed finite moment list supplies
\(p=O(q^2)\). Even if the existing source-rank estimate transferred to
population, that generic rule would give the larger conditional count
\(O([\log(en)]^{9d/2+3})\).  Recovering the existing
\(O([\log(en)]^{3d+2})\) storage additionally requires a law-built,
source-compatible linear-size sparsification.

There is a concrete reason the realized-network source proof cannot simply be
passed to population.  If \((G,H)\) is a nondegenerate Gaussian pair, then

\[
                         \mathbb E|\tanh(G+isH)|^2=\infty
                         \qquad(s\ne0).
\]

Indeed, the joint density is positive near a preimage of the pole
\(i\pi/2\), where the squared integrand is proportional to the inverse
squared distance; its two-dimensional integral diverges logarithmically.
A finite network avoids the poles on a high-probability bounded-coordinate
event, but the Gaussian population has no nonzero complex \(L^2\) strip.
This blocks the direct complex-analytic transfer used by the current source
count.  It does not rule out a real Gevrey, truncation, or other direct proof.

For the second statement one may work up to a fitting time proportional to
\((m/\gamma)\log(en)\) and use endpoint tails afterward.  The constant must
remain independent of this growing horizon.  More importantly, one must
control both terms in

\[
 f_n-f_\infty=(f_n-\mathbb Ef_n)+(\mathbb Ef_n-f_\infty). \tag{23}
\]

The first is fluctuation; the second is finite-width bias.  Independent
dense-versus-dense agreement cancels the second term and cannot prove it.
The maintained population theorem gives only qualitative convergence on
each separately fixed horizon.

If the two bridges hold, the triangle inequality, followed by the fitted
tails, proves (1) at the same physical time and at the endpoint.  The
sufficient width would have the form
\(n\ge N_{\rm data,\delta}\).  No bound for this threshold is currently
proved.

## 6. What has been ruled out, and what has not

A plain independent-particle replacement cannot give the desired storage.
The initialized diagonal top-kernel coefficient is the expectation of a
bounded nonconstant random variable.  Its empirical average over \(P\)
ordinary particles has fluctuations of order \(P^{-1/2}\).  Consequently,
if \(P=o(n)\), the probability that this coefficient is accurate to
\(C/\sqrt n\) tends to zero.  This excludes naive iid random features and
the analogous positive iid weighted rules with effective sample size
\(o(n)\).

It does not exclude deterministic high-order cubature, correlated designs,
control variates, or prediction-based response representations.  Likewise,
the recent source-space lower bound concerns fixed linear approximation of
entire hidden-feature vectors followed by the current quadratic metric.  It
is not an impossibility theorem for the nonlinear hierarchy above or for an
arbitrary autonomous predictor.

## 7. Answer to the central question

No realized large network is conceptually necessary to obtain a convergent
nonlinear learning procedure: Sections 2 and 2.4 give a direct law-built
hierarchy and a complete fixed-accuracy consistency statement.  What is not
known is whether a member of that hierarchy can be selected and initialized
with the same polylogarithmic retained size as the current realization-based
compact model while achieving the large model's natural \(n^{-1/2}\) scale.

Thus the answer is presently:

> **Direct construction is proved qualitatively and at every fixed accuracy,
> but the same-size, strict root-width theorem remains open.**

The unresolved issue is quantitative, not a source-space impossibility: an
effective law-built population discretization and an independent
dense-to-population bias/rate theorem are both still required.
