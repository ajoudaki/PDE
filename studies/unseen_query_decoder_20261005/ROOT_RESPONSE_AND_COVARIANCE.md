# Gaussian response bounds and the limit of causal covariance coupling

2026-10-06. Continuation of the unseen-input decoder study. These are
partial mathematical results, not a complete compact decoder.

Two useful root-width estimates do not require a lower bound on a history
covariance eigenvalue. The first controls scalar matrix-response errors
directly in the original Gaussian initialization coordinates. The second
couples Gaussian laws with population and empirical covariances. An explicit
two-dimensional example shows why the second estimate cannot simply be
replaced by a same-innovation, chronological Cholesky coupling. That
distinction matters for nonlinear training, where the order of information
is part of the model.

## 1. A scalar response estimate from good-set Lipschitz bounds

Let the complete initialization root be a standard Gaussian vector, and
let one of its blocks be an n by n matrix M of independent standard
Gaussians. Other independent root coordinates are allowed. On a measurable
good set E, suppose two vector fields c,h in R^n are restrictions of locally
smooth fields, and satisfy

\[
 \|c\|_2,\|h\|_2\le B\sqrt n,
 \qquad
 \|c(G)-c(\widetilde G)\|_2,
 \|h(G)-h(\widetilde G)\|_2
       \le A\|G-\widetilde G\|_2
 \quad(G,\widetilde G\in E).
 \tag{1}
\]

Here A and B may depend on n; G denotes the complete root, not just M.
For every 0<eta<1,

\[
 \mathbb P\left\{G\in E:\left|
  \frac{c^TMh}{n^{3/2}}
  -\frac1{n^{3/2}}\sum_{i,j}
                  \partial_{M_{ij}}(c_i h_j)
  \right|>
       \frac{\sqrt{B^4+4B^2A^2}}{\sqrt{n\eta}}
                 \right\}\le\eta.
 \tag{2}
\]

Derivatives in (2) are total derivatives through the actual fields. In
particular they are not derivatives with fitted coefficients artificially
held fixed. There is no inverse history Gram matrix in the assertion.

### Extension without a coordinate maximum

We first justify the vector extension used in the proof. Every A-Lipschitz
map from a subset of a finite-dimensional Euclidean space to R^n admits an
A-Lipschitz extension to the entire space. Here is the needed construction.
For a new domain point x and a finite collection of old pairs (x_i,u_i),
consider the balls with centers u_i and radii A||x-x_i||. Minimize

\[
 \max_i\{\|u-u_i\|^2-A^2\|x-x_i\|^2\}
\]

over u. The objective is continuous and coercive. At a minimizer, zero is
in the convex hull of the gradients of the active quadratics: otherwise a
strictly separating direction decreases every active quadratic and hence,
for a sufficiently short step, their maximum. Thus there are nonnegative
active weights alpha_i summing to one for which u=sum_i alpha_i u_i.
The attained maximum equals

\[
 \begin{aligned}
 &\frac12\sum_{i,j}\alpha_i\alpha_j\|u_i-u_j\|^2
              -A^2\sum_i\alpha_i\|x-x_i\|^2\\
 &\quad\le\frac{A^2}{2}\sum_{i,j}\alpha_i\alpha_j\|x_i-x_j\|^2
              -A^2\sum_i\alpha_i\|x-x_i\|^2
       =-A^2\left\|x-\sum_i\alpha_i x_i\right\|^2\le0.
 \end{aligned}
\]

The inequality uses precisely the old Lipschitz inequalities. The finite
balls therefore intersect. For an arbitrary old domain, restrict the
intersections to any one of these compact balls and use its finite
intersection property. This supplies a value at x compatible with every
old value. Add a countable dense set of new domain points successively and
extend by continuity. The cases of an empty domain and A=0 are immediate.

Apply this construction to c and h separately, then project their values
onto the Euclidean ball of radius B sqrt(n). This projection is
nonexpansive and fixes the old values, so (1) now holds globally. These are
auxiliary proof extensions, not computations required of the decoder.

A Euclidean Lipschitz map is differentiable almost everywhere, with
Jacobian operator norm bounded by its Lipschitz constant. Its Jacobian has
rank at most n. Consequently the extended fields obey

\[
 \|D_Gc\|_{\rm HS}^2,\|D_Gh\|_{\rm HS}^2\le nA^2
 \quad\hbox{almost everywhere}.
 \tag{3}
\]

The derivatives of an extension and of the original locally smooth field
agree almost everywhere on E. Indeed their difference vanishes on E;
at a density point of E where it is differentiable, a nonzero derivative
would force nonzero values in a cone of positive relative measure. Almost
every point of E is a density and differentiability point. Gaussian
absolute continuity gives the same almost-everywhere conclusion under
the initialization law.

### Gaussian divergence proof

For a vector field U indexed by the entries of M, define its Gaussian
divergence by
delta(U)=sum_ij [M_ij U_ij-partial_Mij U_ij]. Gaussian integration by parts
twice gives

\[
 \mathbb E\delta(U)=0,\qquad
 \mathbb E\delta(U)^2
   =\mathbb E\|U\|_2^2+
     \mathbb E\sum_{p,q}(\partial_qU_p)(\partial_pU_q)
   \le\mathbb E\|U\|_2^2+\mathbb E\|D_MU\|_{\rm HS}^2.
 \tag{4}
\]

For smooth fields this follows from
E[(M_pu-partial_pu)(M_qv-partial_qv)]
=1_{p=q}E[uv]+E[(partial_qu)(partial_pv)]. Summing this identity proves
(4). Smooth approximation extends it to the bounded Lipschitz fields just
constructed; their first weak derivatives are square integrable. Independent
auxiliary root coordinates can be conditioned on and then integrated out.

Use U=c tensor h divided by n^(3/2). Equations (1) and (3) give

\[
 \|U\|_2^2\le B^4/n,
 \qquad
 \|D_MU\|_{\rm HS}^2
 \le\frac{2\|h\|_2^2\|D_Mc\|_{\rm HS}^2
            +2\|c\|_2^2\|D_Mh\|_{\rm HS}^2}{n^3}
 \le4B^2A^2/n.
\]

Apply Markov's inequality to delta(U)^2 and use derivative locality on E.
This proves (2), without a quantitative bound on the probability of E^c.
An unconditional success statement adds P(E^c) to eta.

### Application to inherited dense paths and its precise scope

For the actual model use unit inputs x/sqrt(d), hidden depth L, mean squared
training loss, mobilities (n,1,...,1,n), iid Gaussian hidden initialization,
and zero readout. The original activation and small-label assumptions and
positive training feature-Gram gap are unchanged.

Section 2, equations (8)--(9), of the authorized
`GENERAL_DENSE_COMPARISON.md` give pairwise good-root parameter control
uniformly in physical time. Multiplying its normalized forward estimate
by sqrt(n) yields, for a fixed training feature vector,

\[
 \|h(G)-h(\widetilde G)\|_2
       \le C\exp\{C\sqrt{\log(en)}\}\|G-\widetilde G\|_2.
 \tag{5}
\]

The backward estimate immediately before that source's equation (8) gives
the same bound with an additional fixed power of log(en) for a training
backward vector. The RMS norms have width-independent bounds. Constants
here may depend on all fixed original problem parameters. Thus (2) gives
a near-root scalar response error for any such pair, at each specified
finite physical time. The derivative trace is the sum of both forward and reverse total
responses to the reused initialized matrix.

This is not yet a compact representation of that trace, a Gaussian law
for an entire dependent training program, or a supremum bound over all
times and queries. A polynomial-sized query net with only (2) would lose
the target rate. The analytic-patch lemmas in
`GROWING_PROGRAM_STABILITY.md` provide conditional supremum transfers;
their complex good-pair hypotheses must still be proved for the actual
query fields. No such hypothesis is silently appended to the target.

## 2. Population and empirical Gaussian covariance can be coupled at root width

Let X_1,...,X_n be independent copies of X in R^r, with ||X||<=B almost
surely. These are not required to be centered. Write

\[
 Q=\mathbb E XX^T,\qquad
 \widehat Q=\frac1n\sum_iX_iX_i^T.
\]

There is, conditional on the samples, a coupling of centered Gaussian
vectors with covariances Q and Q-hat such that its expected squared
distance, further averaged over the samples, is at most

\[
 \frac1n\left[
      \mathbb E\{\|X\|_2^2X^TQ^\dagger X\}
                     -\operatorname{tr}Q\right]
 \le \frac{B^2\operatorname{rank}Q}{n}.
 \tag{6}
\]

Here the dagger is the Moore--Penrose inverse. This statement permits
zero eigenvalues and arbitrarily small positive ones.

To prove it, work on the range of Q; X belongs to that range almost surely,
since every null vector has E|v^TX|^2=0. If Q=0 both laws are zero. Otherwise
Q is positive definite on its range. Put
R=Q^(-1/2) Q-hat Q^(-1/2) on that range. For a standard Gaussian Z
independent of the sample, use the pair

\[
 Q^{1/2}Z,\qquad Q^{1/2}R^{1/2}Z.
\]

Their covariances are Q and Q-hat. Their conditional squared coupling
cost is tr[Q(sqrt(R)-I)^2]. For every nonnegative scalar u,
(sqrt(u)-1)^2<=(u-1)^2. Diagonalizing R proves this inequality in
positive-semidefinite order, and tracing against Q preserves it even
though Q and R need not commute. Therefore the cost is at most

\[
 \operatorname{tr}[Q(R-I)^2]
   =\operatorname{tr}[(\widehat Q-Q)Q^\dagger(\widehat Q-Q)].
 \tag{7}
\]

Independence and centering of X_iX_i^T-Q cancel cross-sample terms when
taking the expectation of (7). Expansion of the remaining square gives
the first expression in (6). Finally
E[X^TQ-dagger X]=rank(Q) and ||X||^2<=B^2 prove the inequality.

The boundedness assumption can be replaced by finiteness and an explicit
bound for the mixed fourth moment appearing in (6). Merely assuming a
finite fourth moment gives that formula, not automatically a uniform
eigenvalue-free constant for a width-dependent family.

## 3. Chronological Cholesky coupling can nevertheless lose a square root

The preceding coupling need not preserve chronological innovations. The
following bounded two-dimensional example shows that this is a substantive
restriction, not a harmless choice of matrix square root.

For each n>=4, let p=1/n, let epsilon=n^(-1/4), and take

\[
 X=(\varepsilon,1)\quad\hbox{with probability }1-p,
 \qquad
 X=(1,0)\quad\hbox{with probability }p.
 \tag{8}
\]

Then ||X||<=sqrt(2), and

\[
 Q=\begin{pmatrix}
       (1-p)\varepsilon^2+p &(1-p)\varepsilon\\
       (1-p)\varepsilon&1-p
    \end{pmatrix},
 \qquad \det Q=p(1-p)>0.
\]

Let U be its upper triangular Cholesky factor, so Q=U^TU and U has
positive diagonal. Its second diagonal entry obeys

\[
 U_{22}^2=\frac{p(1-p)}{(1-p)\varepsilon^2+p}
                \ge\frac12\sqrt p.
 \tag{9}
\]

The last inequality uses p<=1/4 and epsilon^2=sqrt(p). With probability
(1-1/n)^n>=1/4, no rare sample (1,0) is observed. On that event Q-hat
has rank one, and its chronological Cholesky factor has second diagonal
zero. Consequently the factor difference has Frobenius norm at least

\[
             2^{-1/2} n^{-1/4}
 \quad\hbox{with probability at least }1/4.
 \tag{10}
\]

The squared error of a coupling using these two fixed-order triangular
factors and the same independent Gaussian innovations is exactly their
squared Frobenius difference. In contrast, (6) gives expected squared
error at most 4/n for the freely oriented coupling. Thus a root-width
Gaussian-law comparison does not, by itself, prove root-width stability
of a causal factorization.

This example is a width-dependent bounded iid source family. It is not
claimed to be a training history generated by the admissible neural
network. It refutes an unrestricted covariance-to-causal-coupling lemma,
not the compact-decoder conjecture or a network-specific stable response
construction.

## 4. Source screening and remaining implication

The primary statement of Reeves,
[Dimension-Free Bounds for Generalized First-Order Methods via Gaussian Coupling](https://arxiv.org/html/2508.10782v1),
was screened for an applicable growing-program theorem. Theorem 4 assumes
a positive-definite target history covariance and uses whitened covariance
error, together with exponential dependence on iteration count. Theorem 5
also explicitly uses that covariance's condition number. These hypotheses
and constants are not supplied by a positive training-feature Gram gap.
Therefore neither theorem is imported as the missing decoder comparison.
This is applicability screening, not a review of the paper or a claim
about the correctness of its proof.

The highest-leverage remaining step is a causal, compact evaluation of the
total response traces in (2), or a smooth-observable comparison that avoids
unstable chronological factorization. It must retain the original nonlinear
training, have controlled accumulated error at growing temporal resolution,
and answer all sphere queries through the fitted endpoint. The valid scalar
and covariance estimates above do not supply that step on their own.

## Provenance and checks

The lead derived Sections 1--3 using the authorized dense good-pair
comparison and the scalar divergence identity reconstructed in
`GROWING_PROGRAM_STABILITY.md`. The response-energy route separately
reconstructed (6)--(7), including the noncommuting trace step and singular
support reduction, before receiving the counterexample. The counterexample
and vector-extension proof have so far been checked by their author only.
No full-decoder internal PASS, external promotion, numerical experiment,
or new model assumption is claimed.

The dense-comparison source used is
`studies/integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`,
SHA-256 `ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9`.
The maintained notation and the user's minimal-symbol requirements are
retained. No other study or archived book material was used.
