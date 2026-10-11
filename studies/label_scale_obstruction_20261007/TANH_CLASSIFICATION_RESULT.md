# Toward a classification of bad two-hidden-layer tanh dynamics

2026-10-10. Continuation of the same study, following the user's request to
generalize the constructed bad attractor and investigate necessary conditions.
This is an internally checked research result, not promoted book material.
The exact check scope and source versions are recorded in
`TANH_CLASSIFICATION_CHECK.md`.

## Headline: a broader class and strong necessary conditions, not completeness

The earlier example belongs to a general duplicated-profile construction.
There is now an exact second-order test for this entire construction, and
strict versions of three curvature conditions imply a genuinely attracting
positive-loss critical manifold. A corresponding exact test applies to
replicating an arbitrary smaller two-hidden-layer network. Replication does
not automatically preserve stability: newly available neuron-splitting
directions can make a smaller-network local minimum into a saddle.

There is also a universal necessary condition, not restricted to replicated
networks. At every finite positive-loss local minimum, both feature matrices
lose column rank, and the residual remains invisible to certain derivatives
of the first-layer features. Equivalently, many first-layer neurons must lie
at simultaneous critical zeros of explicit residual-weighted analytic
functions. The neurons need not coincide; that conclusion is not proved.

For linearly independent training inputs and width at least the sample count,
**every finite local minimum fits**. More precisely, every positive-loss
stationary point either has negative Hessian curvature or belongs to an
explicit family of flat saddles with cubic descent directions.

These finite-parameter results do not classify every bad trajectory. Besides
exactly stalled saddles, there are actual moving two-hidden-layer tanh
trajectories with positive limiting loss and parameters tending to infinity.
An explicit class with any even sample count at least four is proved below.
Consequently, ruling out bad finite local minima alone cannot establish that
every remaining initial configuration fits.

The general dependent-input classification, the basins of all bad stationary
sets, and positive-loss escape from initially full-rank Gaussian hidden weights
remain unresolved. No unconditional multi-input fitting theorem, width-uniform
failure probability, or incompressibility theorem is claimed.

## 1. Common setup and meaning of stability

There are \(m\geq2\) distinct, nonantipodal sphere inputs
\(x_a\in\mathbb R^d\), \(\|x_a\|=\sqrt d\), fixed labels
\(y\in\mathbb R^m\), and width \(n\geq m\). Define

\[
X=[x_1/\sqrt d,\ldots,x_m/\sqrt d],\qquad
U=\tanh(AX),\qquad H=\tanh(WU),
\]
\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},
\quad w\in\mathbb R^n,\qquad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|^2/m.
\]

All nonlinearities are entrywise. The exact physical gradient flow is

\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L,
\qquad w(0)=0.
\]

These are the maintained model's two hidden layers and canonical mobilities;
there are no biases or frozen hidden blocks. The matrix \(X\) here is exactly
the unit-column matrix called \(X\) in `GLOBAL_FAILURE_ALTERNATIVES.md`;
the latter file calls its unit columns \(x_a\), whereas here they are
\(x_a/\sqrt d\). No mathematical normalization differs.

A stationary point is a parameter configuration with zero full gradient.
A second-order stationary point additionally has positive-semidefinite full
Hessian. Every local minimum is second-order stationary, but the converse
fails even in this model. The attracting sets constructed below are actual
critical manifolds with strictly positive curvature transverse to the
manifold, not merely points with a nonnegative Hessian. Attraction of such a
manifold does not by itself show that its basin meets the exact zero-readout
initialization slice; that entrance is a separate argument.

An exact stationary saddle stalls if initialized exactly there, despite not
being a local minimum. An unbounded trajectory can retain positive loss
without having any finite equilibrium as its limit. Both phenomena matter
for the user's broader definition of "bad."

## 2. A general family containing the previous stable construction

Consider the one-profile loss, with local variables
\(p\in\mathbb R^d\), \(q,s\in\mathbb R\):

\[
J(p,q,s)=\frac1m\sum_{a=1}^m
\big[s\tanh(q\tanh(p^\top X_{:,a}))-y_a\big]^2.
\]

Take a critical point with \(qs\ne0\), and duplicate its parameters as

\[
A_{j,:}=p^\top,\qquad W_{ij}=q/n,\qquad w_i=s.
\]

The full network has the same predictions and is stationary. Define only
within this section

\[
u_a=\tanh(p^\top X_{:,a}),\quad h_a=\tanh(qu_a),
\quad r_a=sh_a-y_a,
\]
\[
\alpha=\sum_a r_a\tanh''(qu_a)u_a^2,\qquad
B=\sum_a r_a\tanh'(qu_a)\tanh''(p^\top X_{:,a})
X_{:,a}X_{:,a}^\top.
\]

For every \(n\geq2\), the full-network Hessian is positive semidefinite
**if and only if**

\[
\nabla^2J\succeq0,\qquad s\alpha\geq0,\qquad sqB\succeq0.
\tag{1}
\]

These three tests respectively measure collective changes of the shared
profile, separation of second-layer neurons, and separation of first-layer
neurons. If all three inequalities are strict, the duplicated configuration
belongs to an attracting local-minimum manifold. If additionally \(J>0\),
that manifold is non-fitting.

Here is the complete second-variation identity behind the test. For any
parameter variation write \(a_j=\delta A_{j,:}^\top\),
\(b_i=\sum_j\delta W_{ij}\), and let
\(\bar a,\bar b,\bar c\) be the respective neuron averages of
\(a_j,b_i,\delta w_i\). Then

\[
\begin{aligned}
D^2\mathcal L[\delta\theta,\delta\theta]
={}&D^2J[(\bar a,\bar b,\bar c),(\bar a,\bar b,\bar c)]\\
&+\frac{2s\alpha}{mn}\sum_i(b_i-\bar b)^2
+\frac{2sq}{mn}\sum_j(a_j-\bar a)^\top B(a_j-\bar a).
\end{aligned}
\tag{2}
\]

All omitted allocation directions have exactly zero quadratic form. Under
strict (1), they are precisely tangent to the actual critical manifold

\[
A_{j,:}=p^\top,\qquad W\mathbf1=q\mathbf1,
\qquad \mathbf1^\top w/n=s.
\tag{3}
\]

Stationarity throughout (3) follows from the one-profile critical equations,
not from the Hessian calculation alone. Taylor expansion in normal
coordinates gives quadratic growth of the loss and linear growth of its
gradient away from (3); the gradient flow therefore converges to a nearby
point of this manifold. The full expansion, trapping proof, and robust
continuation in the input and label data are in
[TANH_REPLICATION_CLASS.md](TANH_REPLICATION_CLASS.md).

This test does not require paired inputs, eighteen samples, a particular
moment-solving recipe, or small labels. Those restrictions belonged to the
previous explicit construction of a seed and proof of zero-readout entrance,
not to the test. They must not be silently dropped when asserting existence
of such an entrance. The previous seed satisfies strict (1); its attracting
manifold and zero-readout basin persist under sufficiently small arbitrary
input and label perturbations. Its finite-width Gaussian basin probability
is positive but is not bounded below uniformly in width.

### More than one profile

The same note gives an exact second-order classification for duplicating
every neuron of any width-\(k\) critical network an equal number of times.
Besides the base Hessian, the test consists of explicit residual-weighted
splitting curvatures and mixed splitting terms. Some mixed terms must vanish
individually; base-network stationarity only forces certain sums of them to
vanish. This explains precisely why arbitrary neuron duplication can destroy
local stability.

Strict versions of those tests give an attracting critical manifold. This is
a conditional theorem: no explicit strict seed with more than one profile
has yet been constructed here. Arbitrary-data robustness of that larger
class is not automatic, because its additional mixed equalities can break
under perturbation. Neither theorem says that every bad minimum is a replica.

## 3. Necessary geometry at every finite bad local minimum

For a first-layer row \(j\) and second-layer row \(i\), define the sample
vectors of activation derivatives

\[
e_j=(1-U_{j,:}^2)^\top,\qquad
d_i=(1-H_{i,:}^2)^\top.
\]

Their entries are strictly positive at every finite parameter configuration.
Call row \(j\) redundant if its feature row \(U_{j,:}\) lies in the span of
the other rows. Equivalently, some \(b\in\ker U^\top\) has \(b_j\ne0\).

At every second-order stationary point,

\[
Hr=0,\qquad U(d_i\odot r)=0\quad\text{for every }i.
\tag{4}
\]

The second identity holds even if \(w_i=0\): varying that row of \(W\)
alone leaves predictions unchanged, so its Hessian diagonal is zero;
positive semidefiniteness forces its mixed Hessian pairing with \(w_i\)
also to vanish. At positive loss, (4) implies
\(\operatorname{rank}U<m\) and \(\operatorname{rank}H<m\).

For every redundant first-layer row \(j\) and active readout \(w_i\ne0\),
there is the stronger condition

\[
X(e_j\odot d_i\odot r)=0.
\tag{5}
\]

To see this, change row \(i\) of \(W\) along \(b^\top\) with
\(b\in\ker U^\top\). This leaves \(WU\), hence the loss, exactly fixed.
Its zero Hessian diagonal forces zero pairing with every perturbation of
row \(j\) of \(A\). The pairing is
\(2w_i b_j\delta A_{j,:}X(e_j\odot d_i\odot r)/(mn)\), proving (5).

Consequently every positive-loss local minimum has a nontrivial kernel in
the following explicitly augmented first-layer feature matrix:

\[
\operatorname{rank}
\begin{pmatrix}
U\\
X\operatorname{diag}(e_j),\quad j\text{ redundant}
\end{pmatrix}<m.
\tag{6}
\]

In using (6), a zero readout cannot be an exception: on distinct nonantipodal
inputs there is no positive-loss local minimum with \(w=0\). The proof is
given below. Thus an active readout always exists at such a minimum, and
\(d_i\odot r\ne0\) supplies the kernel vector in (6).

There is a useful geometric reading. At the fixed candidate configuration,
hold \(r,d_i\) fixed and form

\[
\Phi_i(v)=\sum_a r_a d_{i,a}\tanh(v^\top X_{:,a}),
\qquad v\in\mathbb R^d.
\]

Every first-layer neuron lies on the zero set of every \(\Phi_i\). Every
redundant neuron is a critical zero of each active \(\Phi_i\): both its
value and its gradient vanish there. At most \(\operatorname{rank}U\)
rows can be nonredundant, so at least \(n-\operatorname{rank}U\) neurons
must satisfy these simultaneous critical-zero conditions. The functions are
nonzero real-analytic functions at positive loss: distinct nonantipodal
inputs give linearly independent tanh ridge evaluations, as proved in the
companion note.

This is a broad necessary class that contains the previous examples and
does not assume neuron duplication. It is not a sufficient condition for
stability; residual-weighted second and higher derivatives still matter.

### Why zero readout is not a bad local minimum

If a point with \(w=0\) were a positive-loss local minimum, every sufficiently
nearby hidden configuration with \(w=0\) would have the same loss and also
be a local minimum. Its readout gradient would vanish, so every top-neuron
feature would be orthogonal to \(y\) throughout an open set of hidden
parameters. Real analyticity extends this identity to all hidden parameters.
Choose a first-layer weight with nonzero pairwise distinct absolute input
projections; such choices avoid finitely many proper hyperplanes. Its tanh
values are also nonzero with distinct absolute values. A top neuron supported
on that one first-layer neuron and with arbitrary scalar weight then gives
\(\sum_a y_a\tanh(tu_a)=0\) for all real \(t\). The scalar functions
\(\tanh(tu_a)\) are linearly independent for such \(u_a\), forcing
\(y=0\), a contradiction. The same argument excludes a positive-loss local
minimum with an unused first-layer neuron, meaning \(W_{:,j}=0\).

Complete proofs, the scalar independence lemma, inactive-readout refinements,
and an exact full-Hessian Schur-complement test are in
[TANH_NECESSARY_GEOMETRY.md](TANH_NECESSARY_GEOMETRY.md).

## 4. A complete finite-local-minimum result for independent inputs

Suppose additionally \(\operatorname{rank}X=m\). Every finite local minimum
then satisfies \(r=0\).

Indeed, at a hypothetical positive-loss local minimum, \(w\ne0\), and
\(\operatorname{rank}U<m\leq n\) guarantees a redundant first-layer row.
For an active readout and such a row, (5) contradicts the injectivity of
\(X\), since \(e_j\odot d_i\odot r\ne0\).

More precisely, the complete set of positive-loss second-order stationary
points for these inputs is

\[
w=0,\qquad W=0,\qquad Uy=0,\qquad y\ne0.
\tag{7}
\]

Their Hessian is identically zero. To check this classification, if
\(w\ne0\), (4)--(5) imply (6), contradicting full column rank of \(X\);
hence \(w=0\). At zero readout, the mixed first-layer/readout
Hessian condition is
\(W_{ij}X(e_j\odot d_i\odot r)=0\); injectivity forces \(W=0\), and
the mixed second-layer/readout condition reduces to \(Uy=0\). Conversely,
these identities make every Hessian block vanish.

These flat points are not local minima. Choose a perturbation of one row
of \(A\) whose first-order feature change is \(y^\top\), possible because
\(X\) has full column rank and \(e_j\) is strictly positive. Set one
entry of \(W\) and its corresponding readout both equal to a small real
number \(t\). Along this curve,

\[
\mathcal L(t)-\mathcal L(0)
=-\frac{2\|y\|^2}{mn}t^3+O(t^4).
\tag{8}
\]

Thus every positive-loss stationary point either has a negative Hessian
direction or is a flat saddle of (7). This is a complete local-minimum
classification under the independent-input assumption, not a theorem that
every trajectory converges or every zero-readout initialization fits.

## 5. A general moving failure class with no finite limiting equilibrium

Let \(m=2k\), \(k\geq2\), \(d=2\), and \(n\geq m\). Choose

\[
\frac34<s_1<\cdots<s_k<1,\qquad
x_{j,\pm}=\sqrt2\,(s_j,\ \pm\sqrt{1-s_j^2})^\top.
\tag{9}
\]

These inputs are distinct and every pair has positive inner product. Assign
the same label to the two signs of each pair, with pair labels
\(y_1\geq\cdots\geq y_k>0\) that are not all equal. Initialize

\[
A_{i,:}=p(0)(1,0),\qquad W_{ij}=q(0)/n,\qquad w_i=0,
\qquad p(0),q(0)>0.
\tag{10}
\]

The invariant full-network trajectory has all first rows \(p(t)(1,0)\),
all second weights \(q(t)/n\), and common readout \(v(t)\). On pair \(j\),

\[
u_j=\tanh(ps_j),\qquad h_j=\tanh(qu_j),\qquad f_j=vh_j,
\qquad r_j=vh_j-y_j,
\quad \mathcal L=\frac1k\sum_j r_j^2.
\]

The induced metric is exactly \(dp^2+dq^2+dv^2\), and the exact reduced
gradient flow, with both hidden layers trained, is

\[
\begin{aligned}
\dot v&=-\frac2k\sum_j r_jh_j,\\
\dot q&=-\frac{2v}{k}\sum_j r_ju_j(1-h_j^2),\\
\dot p&=-\frac{2vq}{k}\sum_j r_js_j(1-u_j^2)(1-h_j^2).
\end{aligned}
\tag{11}
\]

All three coordinates are strictly positive for \(t>0\). Initially
\(\dot v>0\), while the vector field is inward on each face of the
nonnegative octant; comparison with its face values on a finite-time compact
box gives \(\dot p\geq-Cp\), \(\dot q\geq-Cq\), and
\(\dot v\geq-Cv\) for a finite box-dependent Lipschitz constant \(C\).
This prevents any later finite-time boundary hit. This local \(C\) is not
a theorem prefactor or asymptotic parameter.

Consequently the predictions are strictly increasing in the pair index,
whereas the labels are nonincreasing. Writing averages over the \(k\)
pairs as bars, their covariance is nonpositive, and hence

\[
\begin{aligned}
\mathcal L
&=\frac1k\sum_j(f_j-\bar f)^2
+\frac1k\sum_j(y_j-\bar y)^2
-\frac2k\sum_j(f_j-\bar f)(y_j-\bar y)
+(\bar f-\bar y)^2\\
&\geq\frac1k\sum_j(y_j-\bar y)^2>0.
\end{aligned}
\tag{12}
\]

There is no finite stationary point in the positive octant. At such a point
the readout equation would give \(\sum_j r_jh_j=0\). Define, only for this
calculation, positive weights \(\pi_j=h_j^2/\sum_bh_b^2\). Then
\(r_j/h_j=v-y_j/h_j\) is strictly increasing in \(j\), has
\(\pi\)-weighted mean zero, while

\[
\frac{\partial_qh_j}{h_j}=\frac{2u_j}{\sinh(2qu_j)}
\]

is strictly decreasing. The weighted covariance is strictly negative:

\[
\begin{aligned}
\frac{\sum_j r_j\partial_qh_j}{\sum_jh_j^2}
&=\frac12\sum_{a,b}\pi_a\pi_b
\left(\frac{r_a}{h_a}-\frac{r_b}{h_b}\right)
\left(\frac{\partial_qh_a}{h_a}-\frac{\partial_qh_b}{h_b}\right)<0.
\end{aligned}
\]

The \(q\) equation in (11) would therefore have \(\dot q>0\), a
contradiction. Every finite boundary point has zero predictions, hence the
initial loss; strict initial descent excludes such a point as an accumulation
point. Every finite accumulation point of a gradient-flow trajectory is
stationary, by the elementary local energy argument in the next section.
There are consequently no finite accumulation points at all. Compactness of
bounded subsets of \(\mathbb R^3\) now gives

\[
p(t)^2+q(t)^2+v(t)^2\longrightarrow\infty,
\qquad
\mathcal L_\infty\geq\frac1k\sum_j(y_j-\bar y)^2>0.
\tag{13}
\]

Both hidden coordinates have strictly positive second derivatives at zero:
differentiate the last two lines of (11), use \(v(0)=0\),
\(\dot v(0)>0\), and \(r_j(0)=-y_j<0\). Thus this is not readout-only
training. The special rank-one hidden initialization has Gaussian probability
zero. No basin open in all network parameters, robustness to arbitrary input
perturbations, or escape from full-rank initialization is established here.
Nor is an exact value of the limiting loss or the individual diverging
coordinate asserted. With \(k=2\), (13) gives
\(\mathcal L_\infty\geq(y_1-y_2)^2/4\), the independently checked
four-sample case in `GLOBAL_FAILURE_ALTERNATIVES.md`.

## 6. What a complete trajectory classification would still require

Let \(\theta=(A,W,w)\) and use the mobility metric

\[
\|\delta\theta\|_{M^{-1}}^2
=\|\delta A\|_F^2/n+\|\delta W\|_F^2+\|\delta w\|^2/n.
\]

The energy identity and Cauchy--Schwarz give

\[
\dot{\mathcal L}=-\|\dot\theta\|_{M^{-1}}^2,
\qquad
\|\theta(t)-\theta(s)\|_{M^{-1}}
\leq\sqrt{(t-s)(\mathcal L(s)-\mathcal L(t))}.
\tag{14}
\]

This prevents finite-time parameter blowup and proves global existence, but
not boundedness as \(t\to\infty\). Every finite accumulation point is
stationary: if its gradient were nonzero, a small fixed neighborhood would
have a uniform positive dissipation rate and bounded speed. Infinitely many
returns would then force repeated fixed positive losses, contradicting
convergence of the decreasing nonnegative loss.

If \(w(0)=0\), \(y\ne0\), and \(H(0)y\ne0\), the loss initially
strictly decreases. Every finite positive-loss accumulation point must then
have \(w\ne0\), and both \(U,H\) must have deficient column rank.
Indeed, \(w=0\) would restore the initial loss; at any stationary point
with \(U\) of full column rank, the second-layer gradient equations and
strictly positive tanh derivatives force \(w=0\). Readout stationarity
similarly precludes full column rank of \(H\) when \(r\ne0\).

One useful sufficient fitting criterion is therefore

\[
\text{bounded parameters and }
\limsup_{t\to\infty}\sigma_{\min}(U(t))>0
\quad\Longrightarrow\quad \mathcal L(t)\to0.
\tag{15}
\]

The assumptions of initial descent above are retained in (15). A bounded
subsequence at times of nonvanishing feature gap produces a full-rank finite
stationary accumulation point, which cannot have positive limiting loss.
The condition is not yet an initial-data criterion.

For completeness there is an exact all-trajectory identity. If
\(K=(\partial f/\partial\theta)M(\partial f/\partial\theta)^\top\)
is the mobility-weighted tangent Gram, then

\[
\mathcal L(t)=\mathcal L(0)
\exp\left[-\frac4m\int_0^t
\frac{r(s)^\top K(s)r(s)}{\|r(s)\|^2}\,ds\right]
\tag{16}
\]

for a nonzero initial residual. A nonstationary smooth trajectory cannot
reach a zero-loss equilibrium at finite time by uniqueness, so the ratio
is well-defined at every finite time. Identity (16) is an exact criterion
for fitting, but is retrospective: evaluating it requires the trajectory.
It does not solve the geometric classification of initial configurations.

A complete answer to the requested classification would still need:

1. A necessity-and-sufficiency description of arbitrary finite bad local
   minima for linearly dependent inputs, including higher-order degeneracies.
   The critical-zero condition and exact Hessian test are not sufficient.
2. A description of which stationary sets can be approached from the exact
   zero-readout slice. Ambient strict-saddle avoidance results cannot simply
   be applied to a law supported on that lower-dimensional slice.
3. A characterization of positive-loss escape, or a way to rule it out on
   the intended initialization class. Section 5 proves that unrestricted
   exclusion is false even for moving two-hidden-layer tanh training.

These are genuine remaining obligations, not consequences hidden in the
finite-equilibrium results. In particular, the present results neither
remove the integrated small-label assumption nor prove that bad dynamics
are incompressible.
