# The nonlinear part of the first-layer features learns

Date: 2026-10-10. Continuation of the same mechanism certificate. This
supplements the simultaneous observable separations in
`INPUT_NONLINEARITY_RESULT.md`; it does not change a compression algorithm or
assert identification of compressed internal coordinates with dense features.

## Statement and dependencies

Use exactly the compatible-data hypotheses in `COMPATIBLE_RESULT.md`: the
paper's Gaussian initialization, zero readout, squared loss and mobilities,
fixed depth, analytic nonaffine activations with bounded derivative, nonzero
labels and at least two pairwise nonparallel sphere inputs. Unbounded
activation values remain allowed. The existing small-label condition is
needed when invoking compression, not by the local argument below.

Let \(V=\operatorname{span}\{x_1,\ldots,x_m\}\), and let \(\sigma_V\) be
normalized uniform measure on the unit sphere in \(V\). Its dimension is
at least two. For neuron \(i\), its first-layer feature at normalized input
\(v\in V\), \(\|v\|=1\), is
\(h_i^{(1)}(t,\sqrt d\,v)=\phi_1(W_i^{(1)}(t)^\top v)\), where
\(W_i^{(1)}\) denotes the stored first-layer row as a column vector.

There are constants \(c,t_*>0\), independent of width, such that for every
fixed \(0<t\le t_*\),

\[
\Pr\left\{
 \frac1n\sum_{i=1}^n
 \inf_{a\in V,\ b\in\mathbb R}
 \int\left|
 h_i^{(1)}(t,\sqrt d\,v)-h_i^{(1)}(0,\sqrt d\,v)
          -a^\top v-b\right|^2\,d\sigma_V(v)
 \ge ct^4
\right\}\longrightarrow1.
\tag{1}
\]

The affine approximation is chosen separately for every neuron and time.
Thus (1) is stronger than nonzero feature movement: even after allowing
each neuron an arbitrary affine-in-input increment, a nonvanishing nonlinear
feature increment remains. It is a first-layer statement, not a claim that
this stronger nonlinear-increment property holds at every depth.

The input from the repaired compatible-data proof is a positive mean-square
first-row acceleration and its strong small-time expansion. Its finite-width
transfer uses the established local population theorem's Wasserstein-2
convergence of joint training preactivation paths. Those dependencies are
explicit, not re-proved here. The new non-affinity lemma and its use are proved
below.

## 1. A nonzero first-layer acceleration cannot be affine in the input

Work in any Euclidean space of dimension at least two. Let \(g,r\ne0\) be
fixed vectors and \(\phi\) real analytic and nonaffine. Then

\[
 v\longmapsto \phi'(g^\top v)(r^\top v),\qquad \|v\|=1,
\tag{2}
\]

is not affine on the sphere. Suppose it equals \(b+a^\top v\). On the
equator perpendicular to \(r\), evaluate at both \(v\) and \(-v\). This
gives \(b=0\) and \(a\) parallel to \(r\), say \(a=\lambda r\).
Consequently

\[
 [\phi'(g^\top v)-\lambda](r^\top v)=0.
\]

The second factor is nonzero on a dense subset of the sphere. Continuity
therefore makes \(\phi'(g^\top v)=\lambda\) on the whole sphere. The
values of \(g^\top v\) fill \([-\|g\|,\|g\|]\). Analyticity makes
\(\phi'\) constant on the entire real line, contradicting nonaffinity.
The argument includes dimension two, where the equator is an antipodal pair.
No parity or independence assumption is used.

## 2. Apply the lemma along the strong population curve

All first-layer weight increments lie in \(V\), by their exact gradient-flow
update. Let \(g(t)\in V\) be the population projected weight row. Its initial
law is standard Gaussian on \(V\), so \(g(0)\ne0\) almost surely. The repaired
activity theorem gives, in \(L^2(\Omega;V)\),

\[
 g(t)=g(0)+\tfrac12 t^2 r+o_{L^2}(t^2),
 \qquad 0<\mathbb E\|r\|^2<\infty.
\tag{3}
\]

The finite and population acceleration have no component outside \(V\),
so projection has not removed their positive squared norm.

The linear map \(u\mapsto[v\mapsto u^\top v]\) is bounded from
\(L^2(\Omega;V)\) into \(L^2(\Omega\times\sigma_V)\). The bounded
continuous multiplier rule applied to the mean-value formula and (3) gives

\[
 \phi_1(g(t)^\top v)-\phi_1(g(0)^\top v)
 =\tfrac12t^2\phi_1'(g(0)^\top v)(r^\top v)
       +o_{L^2(\Omega\times\sigma_V)}(t^2).
\tag{4}
\]

Explicitly, the normalized input increment converges in product \(L^2\);
the integral multiplier \(\int_0^1\phi_1'(g(0)^\top v+s(g(t)-g(0))^\top v)ds\)
is bounded uniformly and converges in probability to \(\phi_1'(g(0)^\top v)\).
Multiplying by the strongly convergent normalized increment is justified by
truncating its fixed \(L^2\) limit. No Fréchet smoothness on \(L^2\) is used.

Let \(P\) be orthogonal projection in the input variable onto affine
functions, separately at each neuron. If \(k=\dim V\), its explicit formula
is

\[
 (Pu)(v)=\int u(s)\,d\sigma_V(s)
       +k\,v^\top\int s\,u(s)\,d\sigma_V(s).
\]

It is a contraction in product \(L^2\). Apply \(I-P\) to (4) and square
the norm. The coefficient of \(t^4\) is

\[
 \frac14\mathbb E\left\|(I-P)
 [\phi_1'(g(0)^\top v)(r^\top v)]\right\|_{L^2(\sigma_V)}^2>0.
\tag{5}
\]

Indeed, \(\Pr(r\ne0)>0\), \(g(0)\ne0\) almost surely, and Section 1
gives a strictly positive distance for every such neuron. Continuous
functions that agree almost everywhere on this sphere agree everywhere.
The integrand is integrable, bounded by
\(\|\phi_1'\|_\infty^2\|r\|^2\). Hence the population nonlinear-increment
energy is a strictly positive constant times \(t^4\), plus \(o(t^4)\).

## 3. Transfer to finite width without extra input assumptions

Choose an orthonormal basis of \(V\), and form the matrix whose rows are
the training vectors \(v_a=x_a/\sqrt d\) in this basis. It has full column
rank. Its fixed left inverse reconstructs the projected row \(g_i(t)\)
from the first-layer training preactivation tuple \((z_{i,a}^{(1)}(t))_a\).
The local theorem uses the uniform path norm, which controls evaluations
at both zero and the fixed time. Thus its joint path-law convergence in
Wasserstein-2 also holds
for \((g_i(0),g_i(t))\). No new trained sample or population theorem on an
uncountable query domain is needed.

The map

\[
 (u,w)\longmapsto
 \|(I-P)[\phi_1(w^\top v)-\phi_1(u^\top v)]\|_{L^2(\sigma_V)}^2
\]

is continuous, because the unsquared map is Lipschitz into \(L^2\), and
has at most quadratic growth in \((u,w)\), because \(\phi_1\) is globally
Lipschitz. Wasserstein-2 convergence transfers its empirical mean to the
population expectation. Choose each fixed sufficiently small positive time
first; then let width grow. The positive coefficient (5) proves (1).

## Meaning for the compression paper

The combined message now has three distinct pieces: nonlinear predictions
cannot be reproduced by any input-affine model; the trained trajectory cannot
be replaced by its initialization kernel; and the nonlinear part of the dense
first-layer features really evolves. Every hidden layer also moves by the
earlier result. None of these statements asserts a test-risk or fitted-endpoint
advantage, or that every later layer's nonlinear component moves.

The compression theorem transfers the two prediction-level separations at
its unchanged rates. The internal statement (1) certifies the dense dynamics
being compressed; prediction accuracy alone is not a proof of analogous
neuronwise movement in the compressed representation.

Check status: `nonlinear_feature_increment` independently derived the
pointwise lemma and product-space projection argument in a prompt-only scoped
check, and separately checked the time-transfer proposal. It confirmed the
argument with two explicit qualifications: endpoint evaluation must be
controlled by the path topology, and time is fixed before the width limit.
Both are satisfied here. Its alternative chain-rule proof replaces \(g(t)\)
by \(g(0)+t^2r/2\) using the Lipschitz activation and applies dominated
convergence to the remaining difference quotient, bounded by
\(\|\phi_1'\|_\infty|r^\top v|\). It also verified the observable bound
\(D(u,w)\le\|\phi_1'\|_\infty^2\|w-u\|^2/\dim V\), establishing
quadratic growth without fourth moments. The inherited local theorem was an
input to that check, not re-audited. No live paper changes or promotion were
performed.
