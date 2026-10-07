# Query-uniform source action: exact gap and a scalar positive example

2026-10-05. Frozen independent bounded route. This is internal research,
not established-book promotion. The full all-time decoder requested in
the assignment remains open. The positive theorem below concerns the
exact initial prediction velocity only; it is not a proposed frozen-feature
replacement for nonlinear training.

## Scope and conclusion

The target is an initialization-derived, restartable compressed nonlinear
model and a decoder for inputs supplied after compilation, with

\[
\sup_{t\in[0,\infty],\,\|v\|_2=1}
 |f_C(t,v)-f_n(t,v)|\le C n^{-1/2+o(1)},
\]

and total retained state, fixed arrays, and live decoder workspace at most
\(C[\log(en)]^5\). The exponent must be independent of input dimension
\(d\), sample count \(m\), and hidden depth \(L\). Constants may have
the permitted fixed-problem dependence. The dense initialization is the
matched realized initialization, not a fresh narrower network. No dense
oracle, hidden program encoding, precision packing, declared test panel,
or frozen-feature substitution is allowed.

The architecture, zero initial readout, block mobilities
\((n,1,\ldots,1,n)\), mean squared loss, analytic activations, spanning
training data, positive initialized training Gram gap, and original full
small-label allowance are unchanged. The requested decoder has not been
constructed here.

Three concrete results locate the remaining issue.

1. The exact observation needs mixed-time training/query feature overlaps.
   A low-dimensional training source space does not itself compute those
   overlaps at an unseen query.
2. Matching weak linear source observations does not control the nonlinear
   image of the omitted preactivation. A two-coordinate example gives a
   nonvanishing defect despite exact agreement on the retained projection.
   This is an obstruction to that closure rule, not to all decoders.
3. At the variability scale, a scalar decoder really can bypass spatial
   basis storage. For deep sine networks the exact initial prediction
   velocity has a uniform \(n^{-1/2}\sqrt{\log n}\) approximation using
   \(O(md+m+L)\) retained coordinates. A full concentration proof is below.
   This prevents interpreting a spatial coefficient count as a general
   impossibility theorem.

## 1. Exact information required by an unseen query

Write \(v_a=x_a/\sqrt d\), with \(\|v_a\|_2=1\), and use the
maintained notation

\[
z^{(1)}(t,v)=W^{(1)}(t)v,\qquad
z^{(j)}(t,v)=W^{(j)}(t)h^{(j-1)}(t,v),\qquad
h^{(j)}=\phi^{(j)}(z^{(j)}),
\]
\[
f_n(t,v)=\frac{(W^{(L+1)}(t))^T h^{(L)}(t,v)}n,
\qquad r_a(t)=f_n(t,v_a)-y_a.
\]

The stored readout starts at zero and obeys
\(\dot W^{(L+1)}=-(2/m)\sum_a r_a h_a^{(L)}\). Therefore

\[
f_n(t,v)=-\frac2m\sum_{a=1}^m\int_0^t r_a(s)
 \frac{h^{(L)}(s,v_a)^T h^{(L)}(t,v)}n\,ds. \tag{1}
\]

This identity follows by integrating the readout equation and substituting
the result into its current observation. It requires neither a limit nor
a kernel approximation. Its kernel is mixed-time and uses the fully
trained feature at the query. A current training Gram is not that kernel.

For example, let \(b_1,\ldots,b_R\) be orthonormal training source
vectors under the pairing \(u^Tv/n\), and suppose for this paragraph
that the readout has exact expansion
\(W^{(L+1)}(t)=\sum_{k=1}^R a_k(t)b_k\). Then

\[
f_n(t,v)=\sum_{k=1}^R a_k(t)
              \frac{b_k^T h^{(L)}(t,v)}n. \tag{2}
\]

The small number of coefficients \(a_k\) does not produce an algorithm
for the scalar functions \(b_k^T h^{(L)}(t,v)/n\). Retaining the dense
\(b_k\) costs \(nR\); evaluating dense \(h^{(L)}\) requires the
discarded initialized mixers. Equation (2) identifies a desired scalar
decoder interface, not an implementation of it.

The learned mixer increment has the exact form

\[
W^{(j)}(t)-W^{(j)}(0)
=-\frac2{mn}\sum_a\int_0^t
 r_a(s)\delta_a^{(j)}(s)h_a^{(j-1)}(s)^T\,ds. \tag{3}
\]

Temporal approximation can represent the factors in (3) by training
source spaces. It does not remove the initialized action
\(W^{(j)}(0)h^{(j-1)}(t,v)\) at an arbitrary query.

More specifically, the supplied selection construction preserves
\(B_0 Rb=R'W_0b\) for its retained paired preimages \(b\). If
\(h=b+e\), this exact identity gives

\[
B_0Rh-R'W_0h=(B_0R-R'W_0)e. \tag{4}
\]

The finite-panel proof makes \(e\) small at every declared query.
Training-only temporal sources make it small only at training inputs.
There is no query-uniform bound on the right side of (4) in the supplied
finite-panel result. One must either bound this action in an adequate
weaker norm or reconstruct its effect through the ensuing nonlinear
layers. The final readout being scalar does not by itself supply that
bound.

## 2. Restricted nonlinear obstruction, with its precise limit

Take the allowed analytic activation
\(\phi(z)=z+\cos z\). It is real on the real axis, entire, has
unbounded real values, and satisfies
\(|\phi'(z)|\le1+\cosh a\) on \(|\operatorname{Im}z|<a\).
Its second derivative is bounded on every such strip as well.

Let \(P\) project onto the constant vectors in \(\mathbb R^2\),
and compare preactivations \(z=(a,-a)^T\) and \(\widetilde z=0\).
Their retained projections agree: \(Pz=P\widetilde z=0\). With
the constant readout \(w=\rho(1,1)^T\), however,

\[
\frac{w^T\phi(z)}2=\rho\cos a,\qquad
\frac{w^T\phi(\widetilde z)}2=\rho. \tag{5}
\]

For \(a=1\) the discrepancy is \(|\rho|(1-\cos1)>0\).
Repeating the two coordinates preserves (5) at every even width under
the normalized pairing. The readout scale \(\rho\) can be arbitrarily
small but fixed with respect to width. Thus exact preservation of all
linear overlaps with this source space does not force even a vanishing
postactivation scalar error.

This proves only that projecting away unresolved preactivations and then
applying the activation is not a valid general closure. It does not show
that the displayed local configurations occur with nonvanishing
probability in the specified dense training problem. It does not exclude
a decoder that retains conditional moments, evaluates Gaussian integrals,
or otherwise accounts for the discarded directions.

Indeed, if an omitted real Gaussian coordinate has conditional mean
\(\mu\) and variance \(\sigma^2\), its expected cosine is
\(e^{-\sigma^2/2}\cos\mu\). Adding conditional variance repairs
this particular example. A successful deep decoder would need the
corresponding correct conditional-law or response closure through actual
feature learning and the reused forward/transpose actions. The supplied
sources do not establish that closure.

## 3. A scalar decoder with no spatial basis at initial velocity

Here every activation is \(\phi^{(j)}(z)=\sin z\), for an arbitrary
fixed \(L\ge2\). This is a subclass of the allowed activation family:
it is nonlinear, real on the real axis, entire, and its derivatives are
bounded on every fixed horizontal strip. The initialization and actual
training equations are unchanged. Take any fixed training data satisfying
the question's spanning, gap, and label assumptions.

Define scalar functions and numbers recursively by

\[
q_0=1,\qquad \kappa_0(c)=c,\qquad
q_j=\frac{1-e^{-2q_{j-1}}}{2},\qquad
\kappa_j(c)=e^{-q_{j-1}}\sinh(\kappa_{j-1}(c)),
\quad -1\le c\le1. \tag{6}
\]

Define the query decoder

\[
g(v)=\frac2m\sum_{a=1}^m y_a\kappa_L(v_a^Tv).
\tag{7}
\]

It stores the training inputs and labels and, optionally, \(q_0,\ldots,q_L\).
Each query is handled one training input at a time, using a dot product
and the scalar recurrence (6). Retained coordinates plus workspace are
\(O(md+m+L+d)\); neither spatial coefficients nor dense initialized
weights are stored. No realized random data are encoded in a scalar
constant. The decoder is deterministic given the training data.

### Quantified theorem

Put \(Y=\|y\|_2/\sqrt m\). For every \(0<\delta<1\), define

\[
\eta_n=\sqrt{\frac2n\log
       \frac{8L(m+1)(1+2n)^d}{\delta}}. \tag{8}
\]

Let \(\mathcal O_n\) be the initialization event

\[
\frac{\|W^{(1)}(0)\|_{\rm op}}{\sqrt n}\le8,
\qquad \max_{2\le j\le L}\|W^{(j)}(0)\|_{\rm op}\le8.
\tag{9}
\]

At every width for which
\(\mathbb P(\mathcal O_n)\ge1-\delta/2\), with probability at least
\(1-\delta\),

\[
\sup_{\|v\|_2=1}|\partial_t f_n(0,v)-g(v)|
\le 2Y\left[(2^L-1)\eta_n+\frac{8^L+1}{n}\right].
\tag{10}
\]

The source packet's Gaussian initialization interface supplies (9) with
probability tending to one for fixed \(d,L\), so its eventual-width
qualification gives an unconditional sufficiently-large-width version of
(10). No effective threshold for that inherited event is claimed here.
Every other probability bound in (10) is explicit. In particular, the
error is \(n^{-1/2+o(1)}\) at fixed structural parameters.

### Proof

For zero-mean jointly Gaussian \((U,V)\) with variances \(u,w\)
and covariance \(c\), the identity
\(\sin U\sin V=[\cos(U-V)-\cos(U+V)]/2\) gives

\[
F(u,w,c):=\mathbb E[\sin U\sin V]
 =\tfrac12[e^{-(u+w-2c)/2}-e^{-(u+w+2c)/2}]
 =e^{-(u+w)/2}\sinh c. \tag{11}
\]

Here \(\mathbb E\cos Z=e^{-\operatorname{Var}(Z)/2}\) follows
from the Gaussian characteristic function, obtained by completing the
square in its one-dimensional integral (or by integrating the density
derivative and solving its characteristic-function differential equation).
The equal-variance population recursion is exactly (6); in particular
\(\kappa_j(1)=q_j\).

On the cone \(u,w\ge0\), \(c^2\le uw\), both exponentials in
(11) lie in \([0,1]\). Direct differentiation gives

\[
|\partial_uF|,|\partial_wF|\le\tfrac12,
\qquad |\partial_cF|\le1. \tag{12}
\]

The line segment between two covariance triples remains in that convex
cone. Integrating derivatives along it shows that perturbing every entry
of a covariance triple by at most \(E\) perturbs \(F\) by at most
\(2E\). Also, \(|\kappa_j(c)|\le q_j\) by covariance
Cauchy--Schwarz. For \(|z|\le q\),
\(e^{-q}\cosh z\le e^{-q}\cosh q\le1\). Differentiating
(6) thus proves \(|\kappa_j'(c)|\le1\) inductively.

Fix a deterministic \(1/n\)-net \(\mathcal N\) of the unit sphere
with size \(N\le(1+2n)^d\). For completeness, take a maximal
\(1/n\)-separated subset. Its disjoint open Euclidean balls of radius
\(1/(2n)\) lie in the radius-\(1+1/(2n)\) ball; the volume ratio
gives the stated bound, and maximality gives the covering property.

At each layer set
\(Q_n^{(j)}(u,v)=h^{(j)}(0,u)^Th^{(j)}(0,v)/n\).
Consider only the pairs \((v_a,v)\), \((v,v)\), and
\((v_a,v_a)\), for \(v\in\mathcal N\), \(1\le a\le m\).
There are at most \((m+1)N+m\le2(m+1)N\) pairs.

Conditional on preceding layers, each empirical entry at layer \(j\)
is the average of \(n\) independent variables in \([-1,1]\).
Its conditional mean is (11) applied to the preceding empirical
covariances; for layer one those covariances are the exact input inner
products. For independent variables in \([-1,1]\),

\[
\mathbb P\{|\overline X-\mathbb E\overline X|>\eta\}
 \le2e^{-n\eta^2/2}. \tag{13}
\]

One proof of (13) is to tilt the scalar law. The second derivative of
the log moment generating function is its tilted variance, bounded by
one because the support has length two. Integrating twice gives
\(\mathbb E e^{t(X-\mathbb EX)}\le e^{t^2/2}\).
Independence and exponential Markov, optimized at \(t=\eta\), give
each one-sided bound in (13). This proof also applies conditional on
the preceding layers.

Union bounding over all these pairs and layers, then removing the
conditioning by expectation, gives failure probability at most

\[
4L(m+1)N e^{-n\eta_n^2/2}\le\delta/2. \tag{14}
\]

On the complementary event, let \(E_j\) be the maximum difference
between the finite and population covariance entries on the listed
pairs. All three preceding covariances needed by each pair are in that
same list. Equation (12) yields
\(E_j\le\eta_n+2E_{j-1}\), with \(E_0=0\), hence

\[
E_j\le(2^j-1)\eta_n. \tag{15}
\]

On \(\mathcal O_n\), the sine Lipschitz constant one gives

\[
\frac{\|h^{(j)}(0,u)-h^{(j)}(0,v)\|_2}{\sqrt n}
 \le8^j\|u-v\|_2.
\]

Every sine feature has RMS at most one, so
\(|Q_n^{(j)}(v_a,u)-Q_n^{(j)}(v_a,v)|\le8^j\|u-v\|_2\).
The population entry \(\kappa_j(v_a^Tv)\) is Lipschitz with
constant one by the derivative bound following (12). Approximation by
the net in (15) therefore gives

\[
\sup_{a,\|v\|_2=1}
 |Q_n^{(L)}(v_a,v)-\kappa_L(v_a^Tv)|
 \le(2^L-1)\eta_n+(8^L+1)/n. \tag{16}
\]

Initially the zero readout makes every hidden backward response zero.
Thus the hidden velocities are zero at time zero, and differentiating
the predictor gives the exact identity

\[
\partial_t f_n(0,v)=\frac2m\sum_a y_a Q_n^{(L)}(v_a,v).
\]

Finally \(m^{-1}\sum_a|y_a|\le Y\) and (16) imply (10).
Intersecting (14)'s success with (9) costs at most \(\delta\).
This proves the theorem, including adaptive query choice after observing
the initialization, because (16) already holds for every sphere input.

### What this proves and does not prove

The result approximates an observable of the matched dense initialization
without retaining its realization, because the allowed error already
contains its empirical averaging fluctuations. It does not imply a
near-\(1/n\) matched approximation. It also does not propagate through
nonlinear training: after training, rows are not conditionally independent
Gaussian samples given the previous layer in the manner used in (14).
The actual hidden updates are retained in the target problem, and no
kernel flow is proposed as its replacement.

## 4. Why two immediate extensions do not finish the target

First, lowering the existing uniform vector-source tolerance from
\(1/n\) to \(n^{-1/2+o(1)}\) changes constants in the analytic
coefficient cutoff, not its logarithmic exponent. In the supplied
whole-sphere construction, the reciprocal angular radius is
\(O(\sqrt{\log n})\); the required logarithmic accuracy factor is
still \(\Theta(\log n)\). Angular degree remains
\(O((\log n)^{3/2})\). The temporal degree remains
\(O((\log n)^{5/2})\), and the same coefficient counting argument
still gives source rank \(O((\log n)^{3d/2+1})\) and quadratic
runtime storage \(O((\log n)^{3d+2})\). These are sufficient counts
for that construction, not lower bounds for arbitrary scalar decoders.

Second, replacing the retained source quadrature by ordinary independent
coordinate averaging with \(q\) terms generally creates
\(q^{-1/2}\) sampling noise. A precise elementary example is useful:
if \(X_1,\ldots,X_n\) are independent signs and
\(\widehat\mu_q=q^{-1}\sum_{i\le q}X_i\),
\(\mu_n=n^{-1}\sum_{i\le n}X_i\), then

\[
\mathbb E(\widehat\mu_q-\mu_n)^2=q^{-1}-n^{-1}.
\tag{17}
\]

For \(q<n\), the fourth moment of this centered signed sum is at
most three times the square of (17). Applying Cauchy--Schwarz to its
squared value above half its mean proves probability at least \(1/12\)
of an error at least \(\sqrt{(q^{-1}-n^{-1})/2}\). Thus ordinary
polylogarithmic subsampling cannot supply root-\(n\) accuracy in this
example. This does not rule out adaptive quadrature, general sketches,
or the population scalar decoder just constructed; estimating \(\mu_n\)
by zero already has root-\(n\) error. The issue is the selected method's
extra sampling noise, not information-theoretic impossibility.

## 5. Remaining proof obligation and provenance

The sharp unresolved bridge is a decoder for the scalar overlaps in
(1) or (2), or an equivalent source-action closure, with error
\(n^{-1/2+o(1)}\) uniformly in physical time and every sphere query,
using the counted finite training state and no discarded dense arrays.
It must account for nonlinear omitted directions as in (5). It must
also have a valid trained concentration or stability argument; initialized
conditional independence is not enough. Given such an action theorem,
the supplied independent fitting tails provide a plausible all-time
extension, but no such theorem is assumed here.

Scientific inputs read completely, with links not followed beyond the
assigned scope:

- `studies/finite_panel_absolute_compression_20261005/RESULT.md`, SHA-256
  `38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`.
- `studies/finite_panel_absolute_compression_20261005/PANEL_SOURCE.md`, SHA-256
  `ca1066cf168829bea642db013a4fbc24166b224df0731783a51b4c85e4fdbaed`.
- `studies/integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md`,
  SHA-256 `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.
- `docs/notation.qmd`, SHA-256
  `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.

The assigned prompt is the other scientific input. Research workflow,
`investigate-conjectures` with research-contract and adversarial-audit
references, and `solve-math-rigorously` were read. The required custom
canonical-notation skill was permission-denied at its assigned path;
the explicit user instructions and maintained notation contract were
applied. No other studies or agents' research were read. No experiment,
external literature retrieval, Git mutation, or maintained-file edit was
performed. Metadata-only Git checks found HEAD
`3834145d910202a84824d943fe7d7f65714d96f2` and an empty staged index;
concurrent work was preserved.

Author check: the initial-velocity derivation was checked algebraically
against conditional row distributions, the covariance recurrence,
conditional union bounds, net extension, and zero-readout dynamics.
The elementary identities and restricted obstruction are complete above.
This route has not received independent complete review and is not marked
internally checked. Its primary output is a proved partial mechanism plus
an explicit open nonlinear decoding obligation.
