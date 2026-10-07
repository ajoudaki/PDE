# Gaussian contractions and collective statistics for actual neural queries

2026-10-06. Scoped author derivation. No experiment, Git operation,
independent review, or promotion. Only this file is owned by this route.

The full efficient unseen-query model remains open. This note establishes
two finite mechanisms that do evaluate actual neural moment expressions
without an n-row Monte Carlo calculation:

1. An exact Gaussian matrix-sandwich identity evaluates the first nonlinear
   forward/transpose return. For a depth-two network it reduces the entire
   conditional mean of the third initial-time prediction derivative to
   Gaussian integrals involving at most six scalar projections, even with
   general correlated training inputs. The nonlinear return terms themselves
   involve at most four projections.
2. For a specified admissible nonlinear network, the first learned mean is
   a product of two additive statistics of independent Gaussian variables.
   A bivariate generating function evaluates a nonlinear activation of this
   mean, at arbitrary prescribed strength, with polynomial work in
   log(1/epsilon). This sums every power of that learned mean; it does not
   simulate the full later training flow.

The exact gap is preservation of a bounded number of such collective
statistics, or of an equivalent small contraction circuit, through the
actual all-layer temporal history. No preservation theorem is supplied by
Gaussian initialization, small labels, or the existing response bounds.
This note neither assumes that theorem nor presents it as a conditional
completion of the requested result.

The continuation in Section 10 identifies a nonzero actual Taylor branch
whose natural correlated-Gaussian contraction graph has width growing
with the number of participating samples. It invalidates an absolute
treewidth claim for that particular contraction representation. It is
not a decoder lower bound.

## 1. Target and scope of the new calculations

Use v=x/sqrt(d), so sphere inputs satisfy ||v||=1. The original network is

\[
 z^{(1)}(t,v)=A(t)v,\quad
 z^{(\ell)}(t,v)=W^{(\ell)}(t)h^{(\ell-1)}(t,v),\quad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\quad
 f_n(t,v)=w(t)^Th^{(L)}(t,v)/n.
\]

The first matrix has iid N(0,1) entries, hidden matrices have iid N(0,1/n)
entries, and w(0)=0. The residual is r_a=f_n(t,v_a)-y_a and the loss is
m^{-1} sum_a r_a^2. All layers train with mobilities (n,1,...,1,n).
The m>=d unit training inputs span R^d. Depth is an arbitrary fixed L>=2
in the target, the original positive feature-Gram gap and small-label
allowance are retained, and activation derivatives are analytic and bounded
on their original strips. Activation values may grow linearly.

The desired decoder reads its retained current state and a previously
unknown v. It must approximate the actual prediction simultaneously for
all v and t in [0,infinity], including the fitted endpoint, at the inherited
independent-dense upper-certificate scale

\[
 b_n=n^{-1/2+o(1)}.
\]

Its setup, retained coefficients, peak workspace, arithmetic work, and
precision are all counted; a dense oracle, replay of training, an
unspecified expectation primitive, and encoded full weights are excluded.
The preferred retained/peak count is O(log^4 n) or O(log^5 n), with
polylogarithmic query work. Results below are partial components, not a
replacement of this contract by a depth-two or initial-time problem.

The allowed RECALIBRATION_FREE_MOMENTS.md makes the concrete hard query
moment explicit. In its stable coordinates, it has the form

\[
 b_\ell=\mathbb E\left[V_\ell
   \Psi_{\phi_\ell}(U_\ell^TA_\ell b_{\ell-1},\beta_\ell)\right],
 \qquad
 \Psi_\phi(z,\beta)=\mathbb E_g\phi(z+\sqrt\beta g),
\]

with a corresponding second moment. Gaussian smoothing in g is cheap;
the retained training marks U_ell,V_ell generally have a nonlinear law.
The mechanisms below concern that law and the matrix reuse producing it.

## 2. Exact nonlinear Gaussian matrix-sandwich contraction

Let W be n by n with iid N(0,1/n) entries, let H be a deterministic n by p
matrix, and let D be a deterministic diagonal n by n matrix. Define

\[
 Z_i=(WH)_{i,:}^T,\quad Q=H^TH/n,\quad
 Q_D=H^TDH/n,\quad d_D=\operatorname{tr}(D)/n.
\]

Thus the Z_i are independent centered Gaussian p-vectors with covariance
Q; Q may be singular. For twice continuously differentiable scalar
functions a,u of polynomial growth, whose needed derivatives also have
polynomial growth, set a_i=a(Z_i), u_i=u(Z_i). If Z has covariance Q, then
exactly

\[
\begin{split}
 \mathbb E\left[\frac1n a^TWDW^Tu\right]
 ={}&d_D\mathbb E[a(Z)u(Z)]\\
 &+\left(1-\frac1n\right)
       (\mathbb E\nabla a)^TQ_D(\mathbb E\nabla u)\\
 &+\frac1n\sum_{b,c=1}^p(Q_D)_{bc}
                      \mathbb E\partial_b\partial_c(au).
 \tag{1}
\end{split}
\]

All derivatives are ordinary derivatives of the displayed functions on
R^p. No covariance inverse occurs, and no independent copy of W replaces
its transpose.

To prove (1), first consider different rows i and j. Gaussian integration
by parts in the independent entries of row i gives

\[
 \mathbb E[a(Z_i)W_{ik}]
     =\frac1n\sum_b H_{kb}\mathbb E\partial_b a(Z).
\]

The analogous formula holds for u in row j. Their product is the
expectation of the off-diagonal summand. Summing over k,i!=j, including
the outside factor 1/n, gives the second line of (1). For i=j, integrating
by parts twice gives

\[
 \mathbb E[W_{ik}^2 a(Z_i)u(Z_i)]
 =\frac1n\mathbb E[au]
  +\frac1{n^2}\sum_{b,c}H_{kb}H_{kc}
                                  \mathbb E\partial_b\partial_c(au).
\]

Summing yields the first and third lines. To justify integration by parts,
truncate the Gaussian variables to compact sets, integrate their smooth
density, and send the cutoff to infinity. Polynomial growth times the
Gaussian density makes the boundary terms vanish and supplies integrable
dominators. The derivation works in the independent entries of W, so it
also covers singular Q.

The second line of (1) is an order-one return from reusing W in opposite
directions. It generally survives n tending to infinity. A rule retaining
only d_D E[au] would miss it. Conversely, (1) replaces this complete return
by scalar Gaussian moments and a p by p matrix; it does not require an
n by n response matrix.

## 3. Where the sandwich occurs in the actual gradient flow

Specialize this calculation, not the target, to L=2. In this section every
unlabelled field is evaluated at time zero. Write

\[
 g_v=Av,\quad h_v^{(1)}=\phi_1(g_v),\quad z_v=Wh_v^{(1)},\quad
 h_v^{(2)}=\phi_2(z_v),\quad S=\sum_b y_bh_b^{(2)},\quad
 K_{av}=h_a^{(2)T}h_v^{(2)}/n,\quad
 K^{(1)}_{av}=h_a^{(1)T}h_v^{(1)}/n.
\]

In applying Section 2, its matrix H consists of the first-layer feature
columns h_1^(1),...,h_m^(1),h_v^(1).

The actual physical equations imply

\[
 \dot w(0)=\frac2mS,\qquad \dot W(0)=0,\qquad \dot A(0)=0,
 \qquad \dot\delta_a^{(2)}(0)=\frac2mS\odot\phi_2'(z_a).
 \tag{2}
\]

Differentiating the physical weight equations once more gives

\[
 \ddot W(0)=\frac4{m^2n}\sum_a y_a
        [S\odot\phi_2'(z_a)]h_a^{(1)T},
\]

\[
 \ddot A(0)=\frac4{m^2}\sum_a y_a
   \{\phi_1'(g_a)\odot W^T[S\odot\phi_2'(z_a)]\}v_a^T.
 \tag{3}
\]

Consequently the second derivative of a query preactivation is

\[
\begin{split}
 \ddot z_v(0)=\frac4{m^2}\sum_a y_a\{&
 K^{(1)}_{av}\,S\odot\phi_2'(z_a)\\
 &+(v_a^Tv)W D_{av}W^T[S\odot\phi_2'(z_a)]\},\qquad
 D_{av}=\operatorname{diag}[\phi_1'(g_a)\odot\phi_1'(g_v)].
 \tag{4}
\end{split}
\]

Both learned hidden blocks appear. In particular (4) is not the result of
freezing the first matrix. Since dot z_v(0)=0, the activation chain rule gives
\(\ddot h_v^{(2)}(0)=\phi_2'(z_v)\odot\ddot z_v(0)\).

For completeness define the scalar initial derivatives

\[
 p_v=\dot f_n(0,v)=\frac2m\sum_a y_aK_{av},\qquad
 q_v=\ddot f_n(0,v)=-\frac2m\sum_a p_aK_{av}.
\]

The full third derivative is exactly

\[
 \partial_t^3 f_n(0,v)
 =-\frac2m\sum_a q_aK_{av}
  +\frac2m\sum_a y_a\frac{\ddot h_a^{(2)}(0)^Th_v^{(2)}}{n}
  +\frac6m\frac{S^T\ddot h_v^{(2)}(0)}n.
 \tag{5}
\]

Indeed \(\dot h_v^{(2)}(0)=0\), so differentiating the prediction
three times leaves \(w'''{}^Th_v^{(2)}/n+3w'^T(h_v^{(2)})''/n\).
Twice differentiating the readout equation gives
\(w'''=-(2/m)\sum_a q_ah_a^{(2)}+(2/m)\sum_a y_a(h_a^{(2)})''\),
which proves (5).

Conditional on A, the matrix and all diagonal weights in (4) meet the
hypotheses of (1). The boundary function a(Z) needed in its two uses is
either S(Z) phi_2'(Z_v) or phi_2(Z_v) phi_2'(Z_c), and its function u(Z)
is S(Z) phi_2'(Z_a). After expanding the two sums defining S, each
same-row Gaussian expectation in (1) involves at most four coordinates
of Z. Taking the derivatives in (1) changes activation derivative orders,
not that number of coordinates. The direct term of (4) has the same bound.

The first term of (5) is a sum of products of three empirical activation
pairings. Its conditional expectation is also explicit. For iid rows Z_i
and scalar tests F_1,...,F_k,

\[
 \mathbb E\prod_{j=1}^k\left(\frac1n\sum_iF_j(Z_i)\right)
 =n^{-k}\sum_{\pi}(n)_{|\pi|}
           \prod_{B\in\pi}\mathbb E\prod_{j\in B}F_j(Z),
 \tag{6}
\]

where the sum is over partitions of {1,...,k}, and
(n)_r=n(n-1)...(n-r+1). Partition the row indices of the product by their
equality relation to prove (6). For k<=3 only finitely many partitions
occur, and each F_j contains two activation factors. Thus at most six
Gaussian scalar projections enter any integral in the exact conditional
mean of (5). No nonsingularity or orthogonality of the data is needed.

This establishes an actual neural moment reduction for a complete first
nonlinear time coefficient. It is not a bound on the full flow remainder.
In particular, holding this order fixed while n grows cannot meet a
vanishing all-time error merely because the labels are fixed and small.

## 4. Resource meaning of this finite Gaussian reduction

Each Gaussian integral in Sections 2--3 can be evaluated without Gaussian
sampling. A covariance of rank s<=6 has a square-root representation in
s independent scalar standard Gaussians. The original derivative strip
and Cauchy's integral formula give bounded higher activation derivatives
on a smaller strip. The integrands are analytic there and grow at most
as a fixed-degree polynomial on real arguments.

Here is a direct quadrature count. Multiply the integrand by its Gaussian
density. On each sufficiently narrow complex coordinate strip, its
absolute integral is at most a fixed M. Move the one-dimensional Fourier
contour within that strip; the Fourier transform decays as M exp(-c|xi|).
The infinite trapezoid rule of spacing h consequently has error at most
C M exp(-c'/h), by summing its nonzero Fourier frequencies. This identity
follows by periodizing the integrand and using the resulting absolutely
convergent Fourier series, as in the proved scalar construction in
SANE_PANEL_EXTENSION.md. Truncating each Gaussian coordinate at
R=C sqrt(log(CM/epsilon)) contributes at most epsilon after increasing
C to absorb the fixed polynomial factor. Taking

\[
 h=c/\log(CM/\epsilon)
\]

uses O(log(CM/epsilon)^{3/2}) nodes per coordinate. Tensoring over s<=6
coordinates gives O(log(CM/epsilon)^9) evaluations; the four-coordinate
nonlinear-return terms cost O(log(CM/epsilon)^6). The tensor rule can be
streamed with six indices, six coordinates, and accumulators. Its
positive Gaussian weights have total mass bounded by a fixed constant,
so assigning epsilon divided by that constant to integrand evaluation
controls numerical evaluation error. Working precision must also cover
the displayed polynomial coefficients and the requested total tolerance.

This arithmetic statement uses the same fixed activation primitives as
the dense network. A bit-time claim requires precision access to these
primitives; analyticity by itself is not an implementation of them.

There are two distinct data interfaces:

* For the exact conditional-on-A formula, acquisition of its empirical
  first-layer matrices costs at least O(n) row visits and stores the
  relevant p by p tables. A previously unknown query requires new
  first-layer empirical pairings, so this is not already an efficient
  finite-width query algorithm.
* Its deterministic large-width coefficient uses the corresponding
  first-layer Gaussian expectations. Those also involve at most four
  scalar projections, with covariance obtained directly from input inner
  products. The finite empirical quantities converge to them by the iid
  law of large numbers and Gaussian polynomial envelopes; Gaussian
  expectations depend continuously on their covariance by square-root
  coupling and the same envelopes. Thus the conditional-mean expression
  has this deterministic limit. All operations are finite, with a
  polynomial number of sample-index sums (a loose O((m+1)^8) bound
  suffices), O((m+1)^2) shared Gram storage, and the quadrature work above.

The second interface computes a limiting coefficient, not an identified
all-time population law or a finite-width decoder. No stochastic
coefficient concentration rate, growing-order limit, or prediction tail
is asserted from this calculation.

## 5. A nonlinear moment that admits a small generating function

There is a second, different positive mechanism inside an admissible
model. Set L=2 and m=d, use v_a=e_a, and choose

\[
 \phi_1(z)=\sin z,\qquad \phi_2(z)=1+\alpha\sin z,
 \qquad 0<\alpha<1.
 \tag{7}
\]

These activations and their derivatives are bounded on any fixed strip.
Let all y_a be positive and small enough for the original allowance.
Writing q=E sin^2(G)=(1-e^{-2})/2, the initial first-layer training Gram
is q I_m. The initial limiting top preactivations Z_a are therefore
independent N(0,q). The top training-feature Gram has off-diagonal one
and diagonal 1+alpha^2 E sin^2(sqrt(q)G), so its gap is positive.

For a unit query v define

\[
 \kappa_a(v)=\mathbb E[\sin(G_a)\sin(G^Tv)]
                      =e^{-1}\sinh(v_a),
 \quad b_a(v)=\kappa_a(v)/q,
 \quad \sigma_v^2=q-\sum_a\kappa_a(v)^2/q\ge0.
 \tag{8}
\]

The identity follows by writing the product of sines as the difference
of two cosines and taking their Gaussian means. Nonnegativity is the
Schur-complement inequality for the actual joint Gaussian covariance;
it also follows by minimizing the squared residual from projection.
Thus the initial query top preactivation has the joint representation

\[
 Z_v=\sum_a b_a(v)Z_a+\sigma_v G_0,
\]

with an independent standard normal G_0, including sigma_v=0.

Define two additive statistics of those independent coordinates:

\[
 S(Z)=\sum_a y_a[1+\alpha\sin Z_a],\qquad
 C_v(Z)=\sum_a y_a\kappa_a(v)\alpha\cos Z_a.
 \tag{9}
\]

The first learned top-matrix mean in (3)--(4) is exactly proportional to
S(Z) C_v(Z): the t^2 contribution from W(t)-W(0), with initial first
features inserted, is (2t^2/m^2) S C_v. This statement identifies an actual
coefficient of the original all-layer flow. Other terms of the flow,
including first-matrix motion and later readout changes, remain present
in (4)--(5).

For any specified real eta, consider the concrete nonlinear weak moment

\[
 T(\eta,v)=\mathbb E\left[S(Z)
      \phi_2(Z_v+\eta S(Z)C_v(Z))\right].
 \tag{10}
\]

Equation (10) is the exact weak gate for this learned-mean field. It
retains every power of eta S C_v. It is not a formula for the entire
trained network at time t when eta=2t^2/m^2.

Integrating G_0 exactly gives

\[
 T=\mathbb E S+\alpha e^{-\sigma_v^2/2}
       \operatorname{Im}\mathbb E
       [S e^{i\sum_a b_aZ_a}e^{i\eta S C_v}].
 \tag{11}
\]

Put s_a(z)=y_a(1+alpha sin z), c_a(z)=y_a kappa_a alpha cos z,
and introduce the bivariate generating function

\[
 F(u,w)=\prod_{a=1}^m
 \mathbb E_{Z_a}\exp\{u s_a(Z_a)+w c_a(Z_a)+i b_aZ_a\}.
 \tag{12}
\]

Independence gives F=E exp(uS+wC_v+i sum b_a Z_a). Therefore

\[
 \mathbb E[S e^{i\sum b_aZ_a}e^{i\eta S C_v}]
 =\sum_{k=0}^\infty (i\eta)^k(k+1)!
                                  [u^{k+1}w^k]F(u,w).
 \tag{13}
\]

Indeed the indicated coefficient equals
E[S^{k+1}C_v^k e^{i sum b_aZ_a}]/((k+1)! k!), and the exponential in
eta has coefficient (i eta)^k/k!. All variables in (9) are bounded,
so absolute convergence and interchange with expectation follow by
domination by ||S||_infinity exp(|eta| ||S||_infinity ||C_v||_infinity).

This is a useful contraction pattern: compute the sum using a generating
function with two formal variables, instead of retaining its high-order
moment tensors or evaluating a multivariate Gaussian integral.

## 6. Algorithm and complete resource count for (10)

Let M_S=sum_a |y_a|(1+alpha) and
M_C=sum_a |y_a kappa_a| alpha. If either is zero, (11) reduces directly
to a product of one-dimensional integrals. Otherwise put A=|eta|M_SM_C.
Truncation after k=K changes the expectation in (11) by at most

\[
 M_S\sum_{k>K}\frac{A^k}{k!}.
 \tag{14}
\]

For K+1>=2eA the tail is at most 2 M_S 2^{-(K+1)}, since
k!>=(k/e)^k and subsequent term ratios are at most 1/2. Hence
K=O(A+log((1+M_S)/epsilon)) suffices. At fixed A one may sharpen this
to O(log(1/epsilon)/log log(e/epsilon)) by the same factorial bound.

For each a compute the rectangular coefficient array

\[
 \frac{\mathbb E[s_a(Z_a)^j c_a(Z_a)^k e^{ib_aZ_a}]}{j!k!},
 \qquad 0\le j\le K+1,\quad 0\le k\le K,
 \tag{15}
\]

then multiply these arrays by truncated two-dimensional convolution.
Only coefficients inside that rectangle are needed. Compute the arrays
sequentially and retain two current product arrays and one factor array.
The convolution costs O(m(K+1)^4) arithmetic operations and
O((K+1)^2) live numbers. Formula (13) is a final diagonal extraction.

All entries of (15) are one-dimensional Gaussian integrals. One may
normalize s_a and c_a by M_S,M_C while constructing the arrays, and restore
the powers in (13). On a fixed complex strip, their powers through 2K+1
have bounds exp(C K); exp(ib_a Z_a) adds exp(C|b_a|). A common truncated
trapezoid grid with

\[
 N_1=O\bigl((mK\log(e+K+m)+K\log(1+A+M_S+M_C)
       +\log((m+1)/\epsilon)+\max_a|b_a|+1)^{3/2}\bigr)
 \tag{16}
\]

nodes, with constants displaying the fixed strip and q, suffices for
the coefficient tolerances below. On each node build all powers by
recurrence and accumulate the whole rectangle, costing O(N_1(K+1)^2)
operations per a. This avoids a separate quadrature pass for each entry.

For numerical stability it is enough to request each integral and each
arithmetic operation to absolute error exp(-B), where

\[
 B=C\{mK\log(e+K+m)+K\log(1+A+M_S+M_C)
                                  +\log((m+1)/\epsilon)+1\}.
 \tag{17}
\]

To see sufficiency, bound the norm of each finite convolution by the
sum of absolute coefficients. For normalized variables each exact factor
has such sum at most e^2. Intermediate products have norm at most e^{2m}.
An error at one operation is propagated by at most the product of the
remaining factor norms, the polynomial number of operations, and the
largest final multiplier (k+1)! times the restored powers. The logarithm
of this product is bounded by the braces in (17), after increasing C.
Induction over the finite convolution circuit then bounds total numerical
error by epsilon/2. Allocate the other half to (14). The same precision
also covers quadrature weights, Gaussian/exponential primitives, and
argument construction; its actual bit costs depend on their evaluators.

The resulting arithmetic ledger is

| Item | Count for the concrete moment (10) |
|---|---|
| Persistent model data | training labels and inputs, fixed activation parameters |
| Query input processing | O(md) work; O(m+d) live data |
| Gaussian integrations | m one-dimensional streamed grids |
| Polynomial algebra | O(m(K+1)^4+m N_1(K+1)^2) work |
| Peak real coordinates | O(md+(K+1)^2) |
| Precision | B bits plus primitive workspace from (17) |
| Dense rows, time replay, future query table | none |

For fixed admissible parameters and bounded eta this is polynomial in
log(1/epsilon). At epsilon=n^{-a}, its principal real-coordinate
workspace is O(log^2 n), with a fixed polynomial query-work exponent.
This ledger applies to (10), not to acquisition/evolution of a complete
surrogate for the original flow.

## 7. Actual neural marks already have full moment rank

The successful generating function should not be misread as a covariance
closure. The same admissible example has genuinely non-Gaussian marks and
arbitrarily large polynomial moment rank.

At initialization define the m-vector

\[
 U_a(Z)=S(Z)\phi_2'(Z_a)=\alpha S(Z)\cos Z_a.
 \tag{18}
\]

By (2), this is m/2 times the actual first time derivative of the top
backward field. At the point Z_a=pi/2 for all a, its Jacobian is

\[
 D_ZU=-\alpha(1+\alpha)\left(\sum_a y_a\right)I_m,
\]

which is invertible because all labels are positive. Continuity of the
derivative and the inverse function theorem give a neighborhood mapped
diffeomorphically onto an open neighborhood of zero. The Gaussian input
density is strictly positive there. Thus the law of U has a positive
density on some open set in R^m. It is bounded and nonconstant, hence is
not a Gaussian law.

For every integer k>=0, collect the monomials U^nu with multi-indices
nu satisfying |nu|<=k. Their Gram matrix has dimension

\[
 N_k=\binom{m+k}{k}
\]

and is positive definite. Indeed a nonzero coefficient vector defines a
nonzero polynomial P. If E P(U)^2=0, then P vanishes almost everywhere
on an open set with positive density, and by continuity on that open
set. Repeatedly viewing it as a univariate polynomial implies every
coefficient vanishes, a contradiction. This proves rank N_k.

This is a reachable neural-law statement, not an arbitrary smooth-row
counterexample. Its force is precise: exact truncations retaining all
polynomial moments through degree 2k cannot claim a uniformly bounded
matrix rank from Gaussian initialization or finite m alone. It provides
no near-root approximate-rank lower bound and no lower bound against
general circuits. In fact Sections 5--6 illustrate how a small generating
function can contract high-rank moments without storing them. Rank growth
and computational hardness must not be identified.

## 8. Why this does not yet continue through full training

The mechanisms exploit different exact structures. Equation (1) uses
independent Gaussian matrix rows and functions of their finitely many
linear projections. Equations (12)--(13) use independence of the Z_a and
only two additive collective statistics. Neither structure is an invariant
of the original flow that has been proved here.

For general correlated training inputs, Z has an arbitrary data-generated
covariance. Diagonalizing it makes its Gaussian coordinates independent,
but then each s_a,c_a depends on many coordinates; the product in (12)
does not survive that change of basis. Equation (1) still works at the
initial response and incurs no covariance inverse, but its integrands
involve increasing numbers of scalar projections at higher orders.

Even in the orthogonal example, after one nonlinear correction a typical
row contains phi_2(Z_a+eta S C_a). Its subsequent response contains
derivatives of this function and new initialized actions on changing
first-layer fields. These are no longer sums of functions of separate
initial coordinates. Replacing them by their Gaussian means or by a
fresh independent Gaussian would discard actual nonlinear and transpose
responses. The complete formula (4) already exposes one such return.

There is a concrete complexity distinction. A fixed number J of additive
statistics can be handled by a J-variable generating array of order K,
with approximately (K+1)^J entries. Replacing J=2 by the full growing
history count R(n) does not give polylogarithmic work or memory. A sparse
or low-rank representation would have to be proved for the actual array
contractions; the full-rank calculation above rules out only the easiest
exact moment-rank argument. It does not rule out such a representation.

The factorial response theorem of EFFICIENT_QUERY_DIRECT.md controls the
omitted operator expansion, but it does not show that its order-k neural
contractions can be expressed using a bounded number of collective
statistics. Its all-time curvature-action bound also does not bound
the tensor contraction complexity of those retained terms. Conversely,
the calculation here supplies genuinely evaluated terms but no summable
whole-flow error estimate.

The decisive next structural question is therefore whether the actual
training-generated cross-characteristic expressions have a bounded-size
factorization after nonlinear composition and both orientations of each
initialized matrix. An answer must construct the factors and prove their
truncation error. Merely defining E[V exp(i xi^TU)] as a stored function
would move the original query integration into a function oracle.

## 9. Claim boundary, hostile checks, and provenance

| Claim | Status and limitation |
|---|---|
| Matrix sandwich (1) | Exact; includes same-matrix transpose response and singular covariances |
| Flow identities (2)--(5) | Exact finite-width all-layer derivatives for L=2 |
| Finite Gaussian moment evaluation of conditional mean of (5) | Constructive; at most six Gaussian projections per integral |
| Two-statistic nonlinear query moment (10)--(17) | Constructive polylogarithmic-accuracy evaluator for its displayed actual leading learned field |
| Actual mark moment rank (18) | Full exact polynomial rank; no universal complexity lower bound |
| Actual higher-order branch (19)--(23) | Explicit; direct Gaussian binary-factor contraction has growing width over the general-data class |
| General-data, arbitrary-depth, all-time compact decoder | Open |

The strongest remaining objections are substantive. The full nonlinear
flow is not replaced by (10); its omitted fields are generally nonzero.
The general correlated-data factorization is absent. Higher response orders
may require growing numbers of jointly nonlinear Gaussian coordinates.
The initial-time coefficient construction supplies no long-time error
propagation or endpoint fitting theorem. Setup of a finite-width empirical
query table still costs n row accesses, explicitly charged above. These
limitations concern the proposed route, not impossibility of the target.

Complete scientific sources read for this route: EFFICIENT_QUERY_DIRECT.md,
POPULATION_DECODER.md, SANE_PANEL_EXTENSION.md, SANE_RESPONSE_MEMORY.md,
RECALIBRATION_FREE_MOMENTS.md, and docs/notation.qmd. No other route note,
other-study research, archive, external scientific source, or experiment
was used. Process sources read were Part 1 of RESEARCH_WORKFLOW.md,
investigate-conjectures with its research-contract, evidence-ledger and
adversarial-audit references, solve-math-rigorously, and the complete custom
explain-with-canonical-notation skill with its neural-response-memory
reference. The custom skill was readable for this route. The supervisor
receives this note as an author derivation, not an independently checked
result.

## 10. Continuation test: an actual Taylor branch with a dense contraction graph

The supervisor requested a further test of whether chronological response
diagrams have treewidth bounded by an absolute constant. The following
calculation tests the natural Gaussian contraction representation. It gives
an explicit higher-order branch of the actual flow, rather than an
arbitrary integrand chosen after the fact.

Continue with L=2 and the activations (7), but now allow general correlated
unit training inputs. At finite width retain the zero-time notation of
Section 3 and define

\[
 C_{v,i}^{(n)}=\sum_a y_a K^{(1)}_{av}\phi_2'(z_{a,i}).
\]

Equation (4) shows that the direct learned-top-matrix contribution to
\([t^2]z_{v,i}(t)\) is exactly \((2/m^2)S_i C_{v,i}^{(n)}\).
In the Taylor composition of the activation, choose this contribution
in each of k copies of the second-order preactivation coefficient, and
choose the first-order readout \((2/m)S\). For every k>=1 this produces
the following actual summand of \([t^{2k+1}]f_n(t,v)\):

\[
 \frac2m\frac{(2/m^2)^k}{k!}\,
 \frac1n\sum_i S_i^{k+1}(C_{v,i}^{(n)})^k
                                      \phi_2^{(k)}(z_{v,i}).
 \tag{19}
\]

This coefficient follows directly from
\([t^{2k}]\phi_2(z_0+t^2b+\cdots)\supset\phi_2^{(k)}(z_0)b^k/k!\).
All other Taylor branches are still part of the actual derivative.
Equation (19) does not assert that the indicated summand is the whole
coefficient, or that other summands cannot cancel some of its value.

For any fixed k, its Gaussian limiting row expectation has the explicit
form

\[
 \mathbb E[S(Z)^{k+1}C_v(Z)^k\phi_2^{(k)}(Z_v)],\qquad
 C_v=\sum_a y_a\kappa_a(v)\phi_2'(Z_a),
 \tag{20}
\]

where the centered Gaussian vector consisting of the training and query
top preactivations has covariance

\[
 Q_{ab}=e^{-1}\sinh(v_a^Tv_b).
 \tag{21}
\]

For the query index, use v_v=v in this formula. The reduction from (19)
to (20) uses conditional iid Gaussian rows, convergence of their bounded
empirical moments, and convergence of the first-layer bounded feature
pairings. It concerns a separately fixed order, with no substitution of
k=k(n) in this argument.

If m>=2k+1, expand S^(k+1) using k+1 distinct training indices and the
sine contribution of each phi_2, and expand C_v^k using k other distinct
training indices. A resulting term, with a nonzero explicit label and
kernel coefficient, is

\[
 \mathbb E\left[
   \prod_{j=1}^{k+1}\sin Z_{a_j}
   \prod_{j=1}^{k}\cos Z_{b_j}
   \sin(Z_v+k\pi/2)\right].
 \tag{22}
\]

There are p=2k+2 distinct Gaussian scalar projections in (22). This term
need not vanish. For example, take distinct training inputs and query
sufficiently close to the same direction, with training inputs still
spanning R^m and positive sufficiently small labels. In the collinear
limit all variables in (22) become the same nondegenerate scalar Z.
For odd k its integrand is, up to sign,
sin^(k+1)(Z) cos^(k+1)(Z); for even k it is, up to sign,
sin^(k+2)(Z) cos^k(Z). All exponents are even, so the expectation has
strictly positive magnitude. Continuity preserves nonzero value for
nearby distinct spanning inputs.

Such nearby inputs satisfy the required positive feature gap. To verify
this without inferring it from near-collinearity, the functions
sin(g^Tv_j) for distinct non-antipodal v_j are linearly independent.
A putative relation holding Gaussian-almost surely holds everywhere by
continuity; restrict it to g=t u with u chosen so all signed frequencies
u^T v_j are distinct. Differentiating its finite exponential expansion
at t=0 gives an invertible Vandermonde system. Thus all coefficients
vanish. Their Gaussian Gram (21) is positive definite. A Gaussian vector
with this covariance has positive density on R^m, and the coordinate
functions 1+alpha sin Z_a are likewise linearly independent under that
density. Hence their Gram also has a strictly positive smallest eigenvalue.
That eigenvalue can be small but is fixed before the width limit; labels
can be fixed inside the corresponding original allowance.

There is an exact tensor representation of (22). Write each sine or cosine
as a sum of its two Fourier modes. For any centered Gaussian p-vector
with covariance Q and trigonometric factors theta_j, each equal to sine
or cosine, one obtains

\[
 \mathbb E\prod_{j=1}^p\theta_j(Z_j)
 =2^{-p}e^{-\operatorname{tr}Q/2}
  \sum_{s\in\{-1,1\}^p}
     \prod_j d_j(s_j)\prod_{i<j}e^{-Q_{ij}s_i s_j},
 \tag{23}
\]

where d_j(s)=1 for cosine and d_j(s)=s/i for sine. The phase from
sin(Z_v+k pi/2) is a known overall sign and chooses the last sine/cosine
factor. Formula (23) follows from
E exp(i s^T Z)=exp(-s^TQs/2); it needs no external complexity theorem.

For the nearby inputs above, all Q_ij are nonzero. The direct pair-factor
graph of (23) is therefore the complete graph on p binary variables.
In ordinary elimination, the first eliminated variable already has p-1
neighbors and produces a table on all of them. This representation has
elimination width p-1 and uses a table of 2^(p-1) entries, or comparable
enumeration work if tables are streamed. Chronological origin of (19)
does not prevent these Gaussian covariance couplings.

The conclusion is deliberately representation-specific. A complete
Gaussian covariance graph alone is not a hardness proof: pure Gaussian
integration has polynomial algorithms, some dense covariances have a small
latent factor representation, and cancellations or generating functions
can compress some sign sums. Equation (23) only proves that the direct
binary-factor elimination plan has no absolute width bound over the
admissible data class. It gives neither a lower bound for all contraction
algorithms nor a no-go theorem for the desired neural decoder.

There are also two quantifier limits. For one fixed m, the training-index
count in this particular branch saturates at m; it does not itself show
unbounded Gaussian dimension as k tends to infinity at fixed m. Across
the stated general-data class, however, choose any k and then fix
m=d>=2k+1 before taking n large. This disproves an absolute treewidth
claim for the displayed chronological construction independently of m,d,k.
Whether fresh later-history Gaussian directions force growing contraction
width even for one fixed small m remains unresolved by this branch.

This continuation identifies a concrete reusable-algorithm target: sum the
actual correlated Gaussian expression (20), including the remaining
Taylor branches and later history, without enumerating the sign graph in
(23). The bivariate product (12) solves its independent-coordinate version.
General correlated covariance destroys that product. No replacement
factorization with a proved absolute size bound is obtained here.

## 11. Frozen author audit

This scoped route stops after the continuation above. The author checked:

* The n and m factors in (1)--(5) directly against the physical weight
  equations and the diagonal/off-diagonal row counts. In particular the
  order-one transpose response in (1) is retained.
* The zero-readout identities, vanishing first hidden velocities, both
  trained hidden-block accelerations, and every term of the third output
  derivative. No fixed-first-layer substitution is made in (4)--(5).
* Singular covariance cases in (1), (6), and the Gaussian quadrature,
  sigma_v=0 in (8)--(11), zero M_S or M_C in the generating evaluator,
  and vanishing falling factorials when n is smaller than a partition size.
* The coefficient factorial in (13), the tail in (14), and the precision
  amplification through the finite polynomial products. Formula (16)
  includes the m-dependent precision cost from (17).
* The actual admissibility, positive feature gap, positive small labels,
  and nonzero-value argument for the higher-order branch. Initial Gaussian
  row laws, empirical row arrays, and deterministic limiting moments are
  distinguished throughout.
* The scope of both rank and graph arguments. Neither is an approximate
  rank lower bound or a lower bound against arbitrary query circuits.
  The branch in (19) is not asserted to survive every possible cancellation
  in the full coefficient. Its projection count saturates at fixed m.

These are algebraic author checks, not independent review or a completed
algorithmic theorem for the original target. No numerical experiment was
used. The unresolved full-flow factorization and error bounds remain
major gaps; they are not labeled technical consequences of these checks.
