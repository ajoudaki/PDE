# Initialization-kernel endpoint: a positive fluctuation coefficient and its limits

This is a bounded theoretical route, authored by the scoped
`endpoint_linear_response` agent on 2026-10-10. It proves statements about
frozen initialization features and their interpolation endpoint. It does not
prove a lower bound for the endpoint of the trained nonlinear dense network.
The supervisor clarified that the intended observable is a supremum over
test inputs separated from the training directions and that training
directions are pairwise neither parallel nor antiparallel. A fixed admissible
query supplies a witness for that supremum.

The scientific inputs were `paper/compact.tex` in full and
`docs/notation.qmd` in full, plus the supervisor's assignment and clarification.
No other study or included paper dependency was read. Required proof,
research-audit, and canonical-notation instructions were read. The input
SHA-256 hashes were, respectively,
`460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` and
`78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.
The recorded Git HEAD was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`.
This is a complete candidate argument with an author audit, not an independent
review or promotion. No experiment was run.

## 1. Setup and exact claims

Let \(v_a=x_a/\sqrt d\in\mathbb R^d\) be the unit training directions,
\(a=1,\ldots,m\), where \(m\ge2\). Fix a unit query \(v_*\) with
\(v_*\ne\pm v_a\) for every \(a\). Initially assume also
\(v_a\ne\pm v_b\) for distinct training indices; Section 3 gives a version
that uses only the final training gap instead. There are \(L\ge2\) hidden
layers. Every activation \(\phi_\ell\) is real on the real axis, holomorphic
on a strip about it, nonaffine, and has bounded first derivative on that
strip. In particular it is smooth, nonconstant, and globally Lipschitz on
\(\mathbb R\), and is not a polynomial: a polynomial with bounded real
derivative has degree at most one.

Use the index set \(I=\{1,\ldots,m,*\}\). Define the augmented, uncentered
population feature Grams by

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}
 =\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],\qquad
 Z\sim\mathcal N(0,Q^{(\ell-1)}),\quad a,b\in I.
\]

An expectation here belongs to a fresh Gaussian vector at the specified
layer; it is not an assertion that population neurons of different layers
share one Gaussian space. All expectations exist because
\(|\phi_\ell(z)|\le |\phi_\ell(0)|+C_\ell|z|\).

At the final layer abbreviate the training block, query column, and label
vector by

\[
 Q=Q^{(L)}_{\mathrm{train},\mathrm{train}},\qquad
 q=Q^{(L)}_{\mathrm{train},*},\qquad
 y\in\mathbb R^m\setminus\{0\},\qquad
 \gamma=\lambda_{\min}(Q)>0.
\]

The population frozen-feature interpolation value is \(q^\top Q^{-1}y\).
The results below are:

1. Every augmented \(Q^{(\ell)}\), \(\ell\ge1\), is positive definite.
2. The empirical iid top-feature interpolation value has a nondegenerate
   \(n^{-1/2}\) Gaussian fluctuation, with the explicit positive coefficient
   in Section 4.
3. Actual finite-depth Gaussian initialization also has a frozen-kernel
   endpoint anti-concentration bound at this scale. The last-layer
   conditional fluctuation is enough; a full depth-wise central limit
   theorem is unnecessary.
4. A coefficient uniform over activations cannot depend only on the final
   training gap, a common upper regularity envelope, and query separation.

The paper's small-label restriction is not needed for these frozen-feature
statements. The counterexample in Section 7 can satisfy it with one fixed
positive label scale.

## 2. Positive definiteness of the augmented feature Gram

First consider unit directions \(u_1,\ldots,u_M\) with
\(u_j\ne\pm u_k\) whenever \(j\ne k\), and a smooth nonpolynomial function
\(\phi\) of at most linear growth. We show that the functions
\(w\mapsto\phi(w^\top u_j)\) are linearly independent in Gaussian
\(L^2(\mathbb R^d)\).

Suppose \(\sum_j c_j\phi(w^\top u_j)=0\) for almost every standard Gaussian
\(w\). The sum is continuous, and Gaussian measure is positive on every
nonempty open set, so it vanishes for every \(w\in\mathbb R^d\). Fix an
index \(k\) with \(c_k\ne0\). For each \(j\ne k\), put

\[
 b_j=u_k-(u_k^\top u_j)u_j.
\]

Then \(b_j^\top u_j=0\), whereas
\(b_j^\top u_k=1-(u_k^\top u_j)^2>0\). Apply the commuting directional
derivatives \(\prod_{j\ne k}D_{b_j}\) to the identity. The term indexed by
\(j\ne k\) is killed by \(D_{b_j}\), leaving

\[
 c_k\prod_{j\ne k}[1-(u_k^\top u_j)^2]\,
 \phi^{(M-1)}(w^\top u_k)=0\qquad\text{for every }w.
\]

The coefficient is nonzero and \(w^\top u_k\) ranges over \(\mathbb R\).
Thus \(\phi^{(M-1)}\equiv0\), which makes \(\phi\) a polynomial, a
contradiction. For \(M=1\), independence follows because a nonpolynomial
function is not identically zero. Consequently, for nonzero \(c\),

\[
 c^\top Q^{(1)}c
 =\mathbb E\left[\sum_{a\in I}c_a\phi_1(w^\top v_a)\right]^2>0.
\]

Now suppose a covariance matrix \(S\) is positive definite, let
\(Z\sim\mathcal N(0,S)\), and let \(\phi\) be a continuous nonconstant
function with finite second Gaussian moments. If
\(\mathbb E(\sum_j c_j\phi(Z_j))^2=0\), full support of this Gaussian
and continuity give \(\sum_jc_j\phi(z_j)=0\) for every
\(z\in\mathbb R^M\). Keeping all coordinates except \(z_k\) fixed and
subtracting the identities at two distinct values gives
\(c_k[\phi(s)-\phi(t)]=0\). Choosing \(s,t\) with different activation
values proves \(c_k=0\). This holds for every coordinate. Hence applying
the next activation produces a positive-definite feature Gram.

Induction proves the first claim. In particular, although the input Gram
\(Q^{(0)}\) may be singular, \(Q^{(L-1)}\) is positive definite because
\(L\ge2\). The Gaussian entering the last layer therefore has full support
on \(\mathbb R^{m+1}\).

## 3. Optional stronger version with singular intermediate training Grams

The query innovation also survives without the pairwise training-direction
condition. This observation is relevant to the literal setup in
`paper/compact.tex`, which assumes the final training gap but does not itself
exclude all antipodal training pairs.

For the layer feature vector
\(H_a^{(\ell)}=\phi_\ell(Z_a)\), \(a\in I\), where
\(Z\sim\mathcal N(0,Q^{(\ell-1)})\), define its query innovation variance by

\[
 \min_{b\in\mathbb R^m}
 \mathbb E\left(H_*^{(\ell)}-b^\top H_{\mathrm{train}}^{(\ell)}\right)^2.
\]

The minimum exists because the span of finitely many \(L^2\) random variables
is finite dimensional and closed. At layer 1 it is positive: otherwise an
exact linear relation expressing the query feature through training features
holds everywhere in \(w\). Applying
\(\prod_{a=1}^mD_{v_*-(v_*^\top v_a)v_a}\) kills its entire training side
and forces \(\phi_1^{(m)}\equiv0\), contradicting nonpolynomiality.

Suppose this innovation is positive at one layer. A Gaussian vector with
that layer's augmented Gram as covariance admits the representation

\[
 Z_*=b^\top Z_{\mathrm{train}}+\sigma\xi,\qquad \sigma>0,
 \qquad \xi\sim\mathcal N(0,1)
\]

with \(\xi\) independent of the training vector. To verify this even when
the training covariance \(S\) is singular, take its eigendecomposition.
The cross-covariance \(q\) lies in the range of \(S\): if \(Sc=0\),
then the variance of \(c^\top Z_{\mathrm{train}}\) is zero and hence
\(c^\top q=0\). Set \(b=S^\dagger q\). The Gaussian difference
\(Z_*-b^\top Z_{\mathrm{train}}\) has zero covariance with the training
vector, so independence follows by factorization of the joint Gaussian
characteristic function. Its variance is exactly the positive innovation.

For every real \(\mu\), the variable \(\phi(\mu+\sigma\xi)\) has positive
variance if \(\phi\) is continuous and nonconstant. Indeed, variance zero
would make it constant almost surely, and the strictly positive Gaussian
density and continuity would then make \(\phi\) constant on all of
\(\mathbb R\). Therefore, for every \(c\),

\[
 \mathbb E[\phi(Z_*)-c^\top\phi(Z_{\mathrm{train}})]^2
 \ge \mathbb E\operatorname{Var}(\phi(Z_*)\mid Z_{\mathrm{train}})>0.
\]

This proves positive query innovation at the next layer, with a lower bound
independent of \(c\). It propagates to all layers. At the final layer,
\(Q\succ0\) then implies that the augmented feature Gram is positive
definite, by completing the square in its quadratic form. It also supplies
the positive conditional query variance at the top layer used below.
Thus Sections 4–6 remain valid under final \(\gamma>0\) and query separation
alone. No claim that \(\gamma>0\) forces every earlier training Gram to be
positive definite is needed.

## 4. Strict positivity of the endpoint influence variance

Let \(Z\sim\mathcal N(0,Q^{(L-1)})\), and define the population top feature
vector and query feature by

\[
 H=(\phi_L(Z_1),\ldots,\phi_L(Z_m))^\top,\qquad
 H_*=\phi_L(Z_*),\qquad b=Q^{-1}q,\qquad \alpha=Q^{-1}y.
\]

The scalar influence and its variance are

\[
 \Psi=(H_*-b^\top H)(H^\top\alpha),\qquad
 V=\mathbb E\Psi^2.
\]

This is the assignment's expression, since
\(b^\top=Q^{(L)}_{*,\mathrm{train}}Q^{-1}\). Gaussian moments and at most
linear activation growth imply \(\mathbb E|\Psi|^k<\infty\) for every fixed
positive integer \(k\). The feature projection identity gives

\[
 \mathbb E\Psi=(q-Qb)^\top\alpha=0.
\]

The preceding section, or ordinary Gaussian regression under the stronger
pairwise-separation assumption, gives
\(\operatorname{Var}(H_*\mid Z_{\mathrm{train}})>0\) almost surely. Since
\(H\) is measurable with respect to \(Z_{\mathrm{train}}\),

\[
 \begin{aligned}
 V
 &=\mathbb E\left[(H^\top\alpha)^2
       \mathbb E((H_*-b^\top H)^2\mid Z_{\mathrm{train}})\right]\\
 &\ge\mathbb E\left[(H^\top\alpha)^2
       \operatorname{Var}(H_*\mid Z_{\mathrm{train}})\right]>0.
 \end{aligned}
\]

For the strict last inequality, note explicitly that

\[
 \mathbb E(H^\top\alpha)^2=\alpha^\top Q\alpha=y^\top Q^{-1}y>0,
\]

so \(H^\top\alpha\ne0\) on a set of positive probability, and the other
factor is strictly positive everywhere except a null set. This proves
positivity for every fixed nonzero label vector, without label-sign or
centering assumptions.

## 5. Empirical iid random features and their interpolation endpoint

Take iid copies \((H_i,H_{*,i})\) of the preceding feature vector, and set

\[
 Q_n=\frac1n\sum_{i=1}^nH_iH_i^\top,\qquad
 q_n=\frac1n\sum_{i=1}^nH_iH_{*,i},\qquad
 F_n=q_n^\top Q_n^{-1}y.
\]

The predictor \(F_n\) is defined on the invertibility event. It may be
assigned any value on the complementary event when stating convergence in
distribution; that event has probability tending to zero. Indeed, the
entrywise law of large numbers gives \(Q_n\to Q\), and \(Q\succ0\) ensures
\(\lambda_{\min}(Q_n)\ge\gamma/2\) with probability tending to one.

For completeness, these are exactly frozen-feature gradient-flow endpoints
with the paper's zero readout, loss, and readout mobility. With fixed feature
columns \(h_i=H_i\), train only the readout \(w\in\mathbb R^n\) from zero:

\[
 f_{n,a}=\frac1n\sum_iw_i h_{a,i},\qquad
 \mathcal L=\frac1m\sum_a(f_{n,a}-y_a)^2,\qquad
 \dot w_i=-\frac2m\sum_a(f_{n,a}-y_a)h_{a,i}.
\]

Then \(\dot f_{n,\mathrm{train}}=-(2/m)Q_n(f_{n,\mathrm{train}}-y)\).
Thus \(f_{n,\mathrm{train}}(t)=(I-e^{-2tQ_n/m})y\), and integrating the
query equation gives \(f_n(\infty,x_*)=q_n^\top Q_n^{-1}y\).

Here is the complete first-order fluctuation calculation. Write
\(R_i=H_{*,i}-b^\top H_i\). The exact identity

\[
 F_n-q^\top Q^{-1}y
 =\left(\frac1n\sum_iR_iH_i\right)^\top Q_n^{-1}y
\]

follows from \(q_n-Q_nb=n^{-1}\sum_iR_iH_i\) and
\(b^\top y=q^\top Q^{-1}y\). Because \(\mathbb E(R_iH_i)=0\) and all
required second moments are finite, Chebyshev's inequality in finitely many
coordinates gives

\[
 Q_n-Q=O_{\mathbb P}(n^{-1/2}),\qquad
 \frac1n\sum_iR_iH_i=O_{\mathbb P}(n^{-1/2}).
\]

On the event \(\lambda_{\min}(Q_n)\ge\gamma/2\), the identity
\(Q_n^{-1}-Q^{-1}=-Q_n^{-1}(Q_n-Q)Q^{-1}\) gives
\(Q_n^{-1}y-\alpha=O_{\mathbb P}(n^{-1/2})\). Therefore

\[
 \sqrt n\,[F_n-q^\top Q^{-1}y]
 =\frac1{\sqrt n}\sum_i\Psi_i+o_{\mathbb P}(1)
 \ \Longrightarrow\ \mathcal N(0,V),\qquad V>0.
\]

The probability theorem used here is the scalar iid central limit theorem:
independent identically distributed real variables of mean zero and finite
positive variance \(V\) have normalized sums converging in distribution to
\(\mathcal N(0,V)\). These hypotheses were all checked above. One direct
verification is to expand their characteristic function at zero:
\(\mathbb E e^{it\Psi/\sqrt n}=1-t^2V/(2n)+o(n^{-1})\), with the
remainder justified by dominated convergence using \(\mathbb E\Psi^2<\infty\).
Independence takes the \(n\)-th power, giving \(e^{-t^2V/2}\); the
characteristic-function continuity theorem identifies the limiting normal
law. Adding a quantity converging to zero in probability does not alter
this weak limit, as follows by bounded uniform-continuity tests and tightness.

For an independent copy \(\widetilde F_n\), the same calculation gives

\[
 \sqrt n(F_n-\widetilde F_n)\Longrightarrow\mathcal N(0,2V).
\]

In particular, for every \(0<\delta<1\), there is a positive
problem-dependent \(c_\delta\) such that
\(\Pr\{|F_n-\widetilde F_n|\ge c_\delta/\sqrt n\}\ge1-\delta\)
at every sufficiently large individual width. Choose \(c_\delta>0\) for
which \(\Pr\{|N(0,2V)|\le c_\delta\}<\delta/2\), and then use convergence
at the two interval endpoints. This coefficient depends on \(V\), hence
on the fixed activation, data, query, and labels.
The coefficient also depends on the confidence. At one query a fixed
positive \(c\) has a strictly positive limiting small-ball failure
probability, so this argument does not give probability tending to one
with a single fixed \(c>0\).

## 6. Actual dense initialization: a frozen-kernel extension

The preceding iid model samples the final Gaussian covariance directly.
In an actual depth-\(L\) initialization, top neurons are conditionally iid
given the lower layers, with a random covariance. The following argument
handles that difference while continuing to freeze every hidden weight
during subsequent readout training.

For the original Gaussian initialization, define the finite augmented
initialization Gram at each layer by

\[
 Q_n^{(\ell)}{}_{ab}
 =\frac1n\sum_{i=1}^n h_{a,i}^{(\ell)}(0)h_{b,i}^{(\ell)}(0),
 \quad a,b\in I,
 \qquad Q_n^{(0)}=Q^{(0)}.
\]

Conditional on layers before \(\ell\), the preactivation rows at layer
\(\ell\) are independent centered Gaussian vectors with covariance
\(Q_n^{(\ell-1)}\). This is exact: each new Gaussian weight row is
independent of the preceding layers, and its covariance is their normalized
feature Gram.

For a positive-semidefinite matrix \(S\), let

\[
 K_\ell(S)_{ab}=\mathbb E[\phi_\ell((S^{1/2}g)_a)
                              \phi_\ell((S^{1/2}g)_b)],
 \qquad g\sim\mathcal N(0,I_{m+1}).
\]

This matrix map is continuous, including at singular \(S\). To see this,
\(S_j\to S\) implies \(S_j^{1/2}\to S^{1/2}\), as follows by diagonalizing
positive-semidefinite matrices and uniformly approximating the scalar square
root on a bounded spectral interval by polynomials. On the common Gaussian
space the inputs then converge in every finite \(L^p\), and Lipschitz
growth gives the same convergence for the features and their products.

On any bounded set of input covariances, the conditional fourth moments of
the features are uniformly bounded by Gaussian fourth-moment formulas and
linear activation growth. Conditional Chebyshev therefore gives

\[
 Q_n^{(\ell)}-K_\ell(Q_n^{(\ell-1)})
   \xrightarrow{\mathbb P}0
\]

whenever \(Q_n^{(\ell-1)}\) is tight. Induction, starting at the deterministic
input Gram and using continuity, proves
\(Q_n^{(\ell)}\to Q^{(\ell)}\) in probability at every fixed layer.

Put \(S_0=Q^{(L-1)}\) and \(S_n=Q_n^{(L-1)}\). For \(S\) near \(S_0\),
let \(Q(S)\) and \(q(S)\) be the training block and query column of
\(K_L(S)\), and define

\[
 F(S)=q(S)^\top Q(S)^{-1}y.
\]

The inverse exists in a neighborhood of \(S_0\), since \(Q(S_0)=Q\succ0\).
Let \(F_n^{\mathrm{init}}\) denote interpolation using the actual empirical
last-layer features at initialization. Conditional on \(S_n\), its samples
have the iid law used in Section 5 with covariance \(S_n\).

For every deterministic covariance sequence \(S_n\to S_0\), the proof in
Section 5 yields

\[
 \sqrt n[F_n^{\mathrm{init}}-F(S_n)]
       \Longrightarrow\mathcal N(0,V).
\]

Here are the extra checks for this triangular version. On a small bounded
covariance neighborhood, \(Q(S)^{-1}\) is uniformly bounded, all feature
moments through order six are uniformly bounded, and the influence means
are zero. The common-Gaussian coupling proves that the influence variances
converge to \(V\). Their absolute third moments are uniformly bounded.
The characteristic-function expansion therefore has a uniform remainder
bounded by \(|t|^3\mathbb E|\Psi(S)|^3/(6n^{3/2})\). Its \(n\)-th power
converges to \(e^{-t^2V/2}\). Uniform second-moment bounds give the same
\(O_{\mathbb P}(n^{-1})\) inverse-matrix remainder as before. These facts
verify the claimed triangular central limit theorem directly.

Since the limiting normal distribution function is continuous, weak
convergence is uniform over interval endpoints. This can be checked by
choosing finitely many normal quantiles with small probability increments,
using convergence at that finite set, and controlling the two tails.
Moreover the convergence is locally uniform in covariance as
\(n\to\infty\), \(S\to S_0\): failure would produce a deterministic
subsequence \(n_j\to\infty\), \(S_j\to S_0\) contradicting the preceding
argument. Consequently it applies to the random \(S_n\) in probability.

Now consider independent dense initializations. Conditional on both lower
layer covariances, the centered endpoint difference has distribution
converging uniformly to \(\mathcal N(0,2V)\). Its uncentered value contains
the possibly random shift
\(\sqrt n[F(S_n)-F(\widetilde S_n)]\). No control on that shift is necessary
for an upper bound on small-interval probabilities: among intervals of
length \(2c\), a centered normal law places most mass on \([-c,c]\).
Conditioning and then averaging gives, for every \(c>0\),

\[
 \limsup_{n\to\infty}
 \Pr\!\left\{\sqrt n\,
       |F_n^{\mathrm{init}}-\widetilde F_n^{\mathrm{init}}|\le c\right\}
 \le 2\Phi\!\left(\frac{c}{\sqrt{2V}}\right)-1,
\]

where \(\Phi\) is the standard normal distribution function. In passing
from conditional convergence in probability to the averaged bound, the
distribution-function errors are bounded by one, so their expectations
converge to zero. Singular empirical training Grams have probability tending
to zero by the initialization law of large numbers; they do not change the
bound. Choosing \(c\) small proves the same eventual
\(c_\delta/\sqrt n\) independent-run lower bound as in Section 5.

This is a statement about the *initialization-kernel interpolation endpoint*.
Because the paper initializes the readout at zero, hidden-weight parameter
derivatives of the output vanish at time zero, and its mobility-weighted
initial tangent kernel is exactly this last-feature Gram. The trained dense
network immediately develops nonzero readout and hidden-weight updates;
its fitted predictor is a different random variable.

If a deterministic set of separated test inputs contains the chosen query,
the supremum of the difference of these frozen-kernel endpoint predictors
is at least the fixed-query difference. Thus this route already handles
that supremum for frozen-kernel training, provided the separated set is
nonempty. No simultaneous lower bound at every query is claimed.

## 7. No coefficient from gap and separation alone across activations

The positive coefficient need not stay bounded away from zero under uniform
strip and upper derivative bounds, even when \(\gamma\), depth, data,
query separation, and nonzero labels are fixed.

Take \(d=m=2\), \(v_1=e_1\), \(v_2=e_2\), and
\(v_*=(e_1+e_2)/\sqrt2\). Its angle to each training direction is
\(\pi/4\), and its distance to the nearest signed training direction is
\(\sqrt{2-\sqrt2}\). Fix any \(L\ge2\), and use at every layer

\[
 \phi_\varepsilon(t)
 =\frac{t+\varepsilon\tanh t}{c_\varepsilon},\qquad
 c_\varepsilon^2=\mathbb E(G+\varepsilon\tanh G)^2,
 \quad G\sim\mathcal N(0,1),\quad 0<\varepsilon\le1.
\]

Each activation is odd and nonaffine, is holomorphic for
\(|\operatorname{Im}z|<\pi/2\), and has a uniformly bounded first derivative
on the common smaller strip \(|\operatorname{Im}z|<\pi/4\).
Indeed, \(c_\varepsilon\ge1\), \(c_\varepsilon\) is uniformly bounded,
and \(|\cosh(x+iy)|^2=\sinh^2x+\cos^2y\ge1/2\) on that strip, which
uniformly bounds \(\operatorname{sech}^2z\). The second derivative is also
uniformly bounded on a smaller strip. Thus the paper's activation envelope
\(\beta\) has a common finite upper bound \(B\).

At every layer, the training Gaussian coordinates are independent standard
normals: induction uses oddness to make the off-diagonal feature expectation
zero and the chosen normalization to make each diagonal expectation one.
Hence \(Q_{\mathrm{train}}^{(\ell)}=I_2\) for every layer and every
\(\varepsilon\), so \(\gamma=1\) exactly. Fix
\(y=(Y,Y)^\top\) with \(0<Y\le B^{-30L}/2\). Then its RMS is \(Y\),
and the paper's small-label condition holds uniformly in \(\varepsilon\).

As \(\varepsilon\downarrow0\), the activation converges to the identity
in every Gaussian \(L^p\), uniformly over bounded variances, and the finite
depth covariance recursion converges to the linear covariance recursion.
Using the common-Gaussian square-root coupling at the last layer, all top
features and their products converge in every fixed finite \(L^p\). At the
limiting identity activation,

\[
 H_*=(H_1+H_2)/\sqrt2,\qquad
 q=(1,1)^\top/\sqrt2,\qquad Q=I_2.
\]

Therefore \(H_*-q^\top Q^{-1}H=0\) almost surely at the limit. The bounded
moment coupling proves

\[
 V_\varepsilon
 =\mathbb E\left[(H_*-q^\top Q^{-1}H)^2
                     (H^\top Q^{-1}y)^2\right]\longrightarrow0,
 \qquad V_\varepsilon>0\text{ for every }\varepsilon>0.
\]

This disproves a positive uniform lower coefficient using only
\(\gamma\), angular separation, fixed dimensions/depth/labels, and upper
regularity bounds. A quantitative distance from affine activations is absent
from those parameters. It does **not** disprove a bound whose coefficient
may depend on the actual fixed activation through its nonaffine component.
The paper permits activation-dependent constants, so this example by itself
does not contradict such a convention. It also concerns the fixed-query
coefficient; a uniform lower bound for a supremum is a separately quantified
statement and is not refuted merely by making one query's coefficient small.

## 8. Precise missing bridge to nonlinear dense endpoints

Let \(f_n(\infty,x_*;s y)\) denote the true nonlinear dense endpoint when
the labels are multiplied by \(s\), if that endpoint exists. At any fixed
finite time, ordinary differentiability of the smooth finite-dimensional
gradient-flow ODE at \(s=0\) yields frozen-feature dynamics as its first
label derivative. Indeed, \(w=0\), residual zero, and unchanged hidden
weights form the \(s=0\) trajectory. The first derivative of each hidden
weight velocity vanishes because its two factors, residual and backward
response, both vanish there. The first derivative of the readout solves
the fixed-feature flow of Section 5 with labels \(y\).

This finite-time derivative does not justify interchanging label
differentiation with the fitted limit. Even after proving that interchange
at each finite width, the following are still missing:

1. A \(n^{-1/2}\)-scale fluctuation expansion for the true nonlinear
   endpoint at the specified fixed nonzero labels, including lower-layer
   and trajectory-dependent contributions.
2. A proof that its variance remains positive, or a conditional
   anti-concentration argument surviving the nonlinear training dependence.
3. Bounds uniform enough in width and label amplitude to connect that
   fluctuation to the initialization influence just proved.

A pathwise approximation
\(f_n(\infty,x_*;s y)=sF_n^{\mathrm{init}}+O(s^3)\), even if established
uniformly in width, would not suffice: with fixed \(s>0\), its remainder
is larger than \(n^{-1/2}\) for large widths. One would need a centered
fluctuation estimate for the remainder, or another mechanism excluding
cancellation. A nonzero derivative at zero also does not ensure a nonzero
fluctuation coefficient at every permitted nonzero amplitude.

For example, a sufficient *additional* result would be an asymptotic
final-layer endpoint influence \(\Psi_s\), conditional on lower-layer
initialization, satisfying
\(\|\Psi_s-s\Psi\|_{L^2}=o(s)\), together with a valid endpoint central
limit theorem conditional on those lower layers and using that influence.
The reverse triangle inequality would
then give positive variance for sufficiently small positive \(s\), with a
threshold depending on \(\sqrt V\); random lower-layer shifts could be
handled as in Section 6. Neither this conditional influence expansion nor
its uniform relation to the paper's particular label bound has been proved
here. The potentially very small \(V\) in Section 7 makes that dependence
substantive.

The established output of this route is therefore a nondegenerate
initialization-kernel endpoint coefficient and a complete frozen-feature
anti-concentration proof. Transfer to actual nonlinear fitted predictors
remains an open proof obligation.
