# Intrinsic dimension, nonlinear feature rank, and Gaussian fitting

2026-10-11. Continuation of the canonical-Gaussian label-scale investigation.
The user's objection is correct: low input rank does not impose low nonlinear
feature rank. The earlier near-orthogonal fitting theorem has a proof-specific
geometric restriction, not a demonstrated necessary condition for learning.
This continuation removes unused ambient dimensions exactly and establishes
rank-free coercivity facts. It does **not** yet remove the geometric restriction
from the arbitrary-label-amplitude, high-probability fitting theorem.

This is a theoretical study result, not promoted book material. No simulation,
optimizer change, compression-theorem modification, staging, or commit was
performed. The research workflow was used to separate exact statements from
conditional routes; the rigorous-proof and canonical-notation workflows were
used for the derivations and checks.

## 1. Common setup and the actual target

Let the columns of \(X\in\mathbb R^{D\times m}\) be fixed unit inputs, with
intrinsic dimension \(d=\operatorname{rank}X\). They are distinct and
nonantipodal. Consider the fully trained, two-hidden-layer tanh network

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad
\mathcal L=\|r\|_2^2/m.
\]

Here \(A\in\mathbb R^{n\times D}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\). The independent initialization is
\(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), and exactly \(w=0\).
The gradient-flow mobilities for these three blocks are \((n,1,n)\).
Labels are fixed before initialization, independent of width, and can have
mixed signs. This continuation uses exact zero readout; it does not silently
transfer every new lemma to an order-one Gaussian stored readout.

For inputs originally normalized by \(\|x_a\|=\sqrt D\), the columns of
\(X\) above are \(x_a/\sqrt D\). An ambient embedding must preserve these
normalized inner products. Changing the divisor without rescaling the inputs
would change the model, not merely its representation.

The unresolved target is actual finite-width fitting with probability tending
to one as width grows, for arbitrary fixed label amplitudes and a substantially
broader input class, ideally every such fixed dataset and label vector:

\[
\Pr\!\left\{\lim_{t\to\infty}\mathcal L_n(t)=0\right\}\longrightarrow1.
\]

A population trajectory that fits, an initialized positive Gram, or a
finite-time approximation alone does not establish this order of limits.

## 2. Ambient dimension disappears exactly

Choose \(Q\in\mathbb R^{D\times d}\) with orthonormal columns spanning the
data, and put \(V=Q^\top X\), \(\Theta=AQ\). Then

\[
AX=\Theta V,\qquad
\dot\Theta=-n\nabla_\Theta\mathcal L,\qquad
\dot A(I-QQ^\top)=0.
\]

Every row of \(\Theta(0)\) is an independent standard Gaussian in
\(\mathbb R^d\), independent of \(W(0)\). Consequently the training
predictions have exactly the law and dynamics of the intrinsic-dimensional
network. This is an exact identity, not an infinite-width approximation.
It also applies to queries in the sample span; it does not identify responses
to arbitrary queries outside that span.

The proof is the chain rule
\(\nabla_A\mathcal L=(\nabla_\Theta\mathcal L)Q^\top\), together with
\(Q^\top Q=I_d\) and Gaussian rotational invariance. Thus adding unused
ambient coordinates cannot overcome a restriction requiring linearly
independent sample columns. But there is no reason from this identity for
such a restriction to be necessary for nonlinear fitting.

## 3. Nonlinear rank does not require independent input columns

For a standard Gaussian \(g\in\mathbb R^D\), the initialized first-feature
population Gram satisfies

\[
\mathbb E\big[\tanh(X^\top g)\tanh(X^\top g)^\top\big]\succ0.
\]

There is no requirement \(m\le d\). For example, there can be arbitrarily
many distinct nonantipodal samples in a plane.

Here is the rank argument. A zero quadratic form would make a linear
combination of the ridge functions \(g\mapsto\tanh(g^\top x_a)\) vanish
everywhere, by continuity and full Gaussian support. Choose a direction
whose projections onto the samples are nonzero and have distinct absolute
values; the excluded directions are a finite union of proper hyperplanes.
On this line the identity is a linear combination of
\(\tanh(\lambda_a t)\), with distinct positive \(\lambda_a\), after
absorbing the projection signs into the coefficients. Letting \(t\to\infty\)
first removes the constant term. The unique slowest term in
\(\tanh(\lambda t)-1=-2e^{-2\lambda t}+o(e^{-2\lambda t})\)
then forces its coefficient to vanish. Repeating proves independence.

The same argument provides \(m\) first-weight rows whose feature vectors
are independent. The determinant of the corresponding \(m\times m\)
feature matrix is therefore a nonzero real-analytic function of the rows.
Its zero set has Lebesgue measure zero. Hence, for every \(n\ge m\),

\[
\operatorname{rank}U(0)=\operatorname{rank}H(0)=m
\quad\text{almost surely}.
\]

For the second equality, condition on \(U(0)\): each row of \(W(0)U(0)\)
has nonsingular Gaussian covariance \(U(0)^\top U(0)/n\), and coordinatewise
tanh maps that full-support law onto an open cube. The limiting second-feature
population Gram is positive definite for the same reason. Conditional
concentration and continuity in the covariance justify this population limit;
unconditional independence of the top rows is not assumed.

These statements give positivity for each fixed dataset, not a quantitative
gap uniform over growing sample counts or nearly coincident samples. Also,
the no-antipodes qualification matters: bias-free tanh is odd, so an antipodal
pair creates an exact dependence. General nonlinear activations need their
own nondegeneracy condition; distinct samples alone do not suffice for every
nonlinearity.

### A further finite-time Gaussian statement

For every fixed label vector, every \(n\ge m\), and each deterministic finite
physical time \(T\),

\[
\Pr\{\operatorname{rank}U(T)=m\}=1.
\tag{1}
\]

This does not require a small label or an input-rank condition. Here is a
complete argument. The finite-dimensional vector field is real analytic.
The energy identity

\[
-\dot{\mathcal L}
=\|\dot A\|_F^2/n+\|\dot W\|_F^2+\|\dot w\|_2^2/n
\]

bounds parameter displacement over a finite interval by its square-root
length times \(\sqrt{\mathcal L(0)}\), in the displayed weighted norm.
Thus solutions do not escape in finite time. On every compact segment of
a solution, the analytic ODE has an analytic local solution map in the
initial parameters; finitely many such maps compose to an analytic time-\(T\)
map. This proves real-analytic dependence locally at every initial state.

The determinant of the first \(m\) rows of \(U(T)\), as a function of
\((A(0),W(0))\) with \(w(0)=0\), is therefore real analytic on connected
Euclidean space. It is not identically zero: set \(W(0)=0\). Then
\(H=w=0\), all velocities vanish, and \(A(T)=A(0)\). Choose the initial
rows from the independent feature vectors above. The resulting determinant
is nonzero. This zero-middle-matrix choice is only a witness for analytic
nonidentity, not a chosen initialization event in the probability theorem.
The actual joint Gaussian initialization has a density, so the zero set has
probability zero, proving (1).

For completeness, the analytic-zero-set fact used here follows by covering
each zero by a zero set of a derivative with nonzero gradient: choose the
first nonvanishing derivative and then a derivative of one lower order.
Each such regular zero set is locally a hypersurface. Countably many
derivatives and coordinate neighborhoods suffice. Analyticity on a connected
domain excludes a point at which all derivatives vanish for a nonzero
analytic function.

Moreover, for almost every initial draw the same initial nonzero minor is an
analytic, nonidentically-zero function of time. Its zeros are isolated on
finite intervals. This allows random isolated rank-loss times; (1) cannot
be strengthened to simultaneous full rank at every time merely by taking
an uncountable union. Neither statement supplies a gap uniform in width or
as \(t\to\infty\). Asymptotic rank collapse remains possible under these
statements. The separate check is in
[INTRINSIC_FINITE_TIME_CHECK.md](INTRINSIC_FINITE_TIME_CHECK.md).

## 4. The useful coercivity condition is nonlinear and moving

For sample \(a\), write \(u_a,h_a\) for the columns of \(U,H\), and define
\(b_a=w\odot(1-h_a^2)\). Let \(K\) be the full tangent Gram with the
canonical mobilities, so that

\[
\dot r=-2Kr/m,\qquad
\dot{\mathcal L}=-4r^\top Kr/m^2.
\]

The middle-weight contribution alone is

\[
(K_W)_{ab}=\frac{u_a^\top u_b}{n}\frac{b_a^\top b_b}{n},
\qquad
K\succeq K_W\succeq
\lambda_{\min}(U^\top U/n)
\operatorname{diag}\!\left(\frac{\|b_a\|_2^2}{n}\right).
\tag{2}
\]

To prove the second inequality, subtract
\(\lambda_{\min}(U^\top U/n)I\) from the first positive-semidefinite Gram
and take its entrywise product with the Gram of the \(b_a\). This product
is positive semidefinite: it is the Gram of tensor products of the two
families of feature vectors. This establishes (2), including its normalization.

At a finite parameter state, full column rank of \(U\) and \(w\ne0\)
make the right side strictly positive, since every finite tanh derivative
is positive. This is independent of the rank of \(X\). It also works at a
strong population state with finite preactivations almost surely.

Thus a quantitative version of the desired stability condition is

\[
\lambda_{\min}(U(t)^\top U(t)/n)
\min_a\frac1n\sum_i w_i(t)^2
       \operatorname{sech}^4((W(t)U(t))_{ia})\ge\kappa>0.
\tag{3}
\]

If (3) holds eventually, loss decays exponentially thereafter at rate at
least \(4\kappa/m\). A positive endpoint value plus sufficiently small
residual can instead trigger a width-uniform local capture argument; the
complete conditional capture proof is in the symmetry route and its check.

Pointwise positivity, including (1), does not prove (3). At a finite critical
point with full-rank \(U\), a nonzero residual forces \(w=0\), and such a
point is a strict saddle, as proved in the feature route. Starting from the
canonical initialization and \(y\ne0\), initial loss decreases strictly
almost surely because \(H(0)\) has full rank. Thus no finite limiting
nonfitting state with \(w=0\) can be reached: it would have the original
loss. A finite nonfitting limit must therefore lose the rank of \(U\).
Unbounded trajectories are not excluded by this finite-endpoint statement.

There is also a finite-time corollary for the actual full tangent Gram:
for each deterministic finite \(T\), \(K(T)\succ0\) almost surely, for
every fixed label vector. At \(T=0\), the readout Gram is already positive
definite. For \(y\ne0\), its initial strict loss decrease and subsequent
monotonicity exclude \(w(t)=0\) at any \(t>0\), because that would restore
the original loss. Combine (1) with (2). For \(y=0\), the initialized flow
is stationary and the positive initial readout Gram is unchanged. This
corollary remains pointwise in deterministic time; it does not establish
a width-uniform or infinite-time positive lower bound.

## 5. What the proof search adds, and what remains missing

The raw first-layer dynamics still contains the input inner products:

\[
\dot u_a=-\frac2m(1-u_a^2)\odot
 \sum_b(x_a^\top x_b)r_b(1-u_b^2)\odot W^\top b_b.
\]

One cannot replace this input Gram by a nonlinear feature Gram without
changing the optimizer. The old orthogonal proof removes the first-layer
gate by a scalar coordinate change. The geometry route proves that a
simultaneous such change exists only for mutually orthogonal directions,
allowing signed duplicates. More generally, for a genuinely nonorthogonal
pair no fixed positive row metric near the origin can cancel all arbitrary
signed sample forcings. These are exact obstructions to that proof mechanism,
not to the actual Gaussian training dynamics. The actual forcings are
coupled, not arbitrary.

The alternative pursued here uses a transitive symmetry rather than
near-orthogonality. For odd \(k\ge3\), take two reflected regular \(k\)-gons
on the unit circle, at a generic relative angle, and assign labels \(+a\)
to one and \(-a\) to the other. There are \(m=2k\) distinct nonantipodal
points of intrinsic dimension two, and \(a>0\) is any fixed amplitude.
The exact construction and its group action are in
[INTRINSIC_SYMMETRY_ROUTE.md](INTRINSIC_SYMMETRY_ROUTE.md).

Gaussian symmetry would make an identified deterministic population prediction
a scalar multiple of this sign pattern. Along a constructed strong scalar
ascent flow, readout linearity then gives a strictly positive lower bound
on scalar progress, so every fixed amplitude is reached at a finite feature
time. A positive readout-plus-middle endpoint Gram, together with the required
compact-time limits, would transfer this to actual finite-width all-time
fitting by a late finite-snapshot capture argument.

The new support lemma supplies that endpoint gap **conditionally**: if the
first-neuron backward drive is a Gaussian source with integrable paths,
independent of its initial row, plus a causal linear response in the bounded
first features with deterministic measurable signed response measures whose
total variation is integrable over that finite feature horizon,
the row's law keeps full support. Conditional on the source, the row endpoint
is a continuous map equal to the initial row plus a uniformly bounded
displacement. Brouwer's theorem makes that map onto. Gaussian full support,
ridge independence, and (2) then give the full endpoint gap. The proof
allows same-time response atoms and does not assume backward invertibility
of a memory equation.

The missing obligations are substantive:

1. Construct and identify the uncut correlated-input strong population flow,
   with the required compact-time finite-width prediction and Gram limits.
2. Prove the integrable total-variation bound for the adaptive response of the
   initialized Gaussian middle matrix, uniformly as the time mesh is refined
   and proof cutoffs are removed.

The learned part of the middle-matrix response is directly bounded on finite
feature horizons. The initialized adaptive action is not. A bounded common
operator on \(L^2\), or a finite response at every fixed mesh, does not
provide this missing estimate. No existing fixed-program result is treated
as if it already supplied that continuum bound. Even closing these obligations
would first prove the stated character-label family, not all label ratios.

Two further endpoint alternatives are proved conditionally in
[INTRINSIC_ENDPOINT_ROUTE.md](INTRINSIC_ENDPOINT_ROUTE.md). First, one can
protect a spanning collection of saturated sign patterns if the backward
drive has a finite time-integrated second-moment bound uniformly conditional
on the initial Gaussian first-neuron row. This does not require a causal
response representation. The ordinary unconditional second-moment bound does
not imply this conditional bound, and the latter remains unproved for the
actual coupled network.

Second, take regular-simplex inputs with \(m\ge3\), hence input rank
\(m-1\). At any constructed state whose readout-plus-middle Gram is invariant
under every sample permutation and whose mean prediction is positive, that
Gram is necessarily positive definite. If its contrast eigenvalue vanished,
the readout block would make all top features equal. The middle block would
then make all first features equal. Injectivity of tanh and the zero sum of
the simplex vertices would force all first preactivations, hence all
predictions, to vanish: a contradiction. The common eigenvalue is positive
because the mean prediction is positive. This removes any feature-support
or backward-tail premise from that endpoint argument.

By oddness of the bias-free network, flipping selected simplex inputs and
the corresponding label signs leaves the loss identical as a function of
the parameters. The parameter trajectories are exactly the same, and the
sample kernels are conjugate by the diagonal sign matrix. Thus the
conditional simplex route includes arbitrary fixed common amplitude and
mixed signs without changing Gaussian initialization. It still requires
construction and finite-width identification of the symmetric correlated
population path. It is not an arbitrary-label-ratio theorem and does not
settle the much lower-dimensional planar family.

The rank-free small-label theorem was also reconstructed with explicit
constants in [INTRINSIC_FEATURE_ROUTE.md](INTRINSIC_FEATURE_ROUTE.md).
It already allows singular input Grams and proves actual finite-width
exponential fitting with probability tending to one. It is a baseline, not
a new removal of the label restriction.

## 6. Evidence, qualifications, and next proof obligation

The complete geometry proof and its fresh scoped internal check are
[INTRINSIC_GEOMETRY_ROUTE.md](INTRINSIC_GEOMETRY_ROUTE.md) and
[INTRINSIC_GEOMETRY_CHECK.md](INTRINSIC_GEOMETRY_CHECK.md).
The complete feature and conditional symmetry proofs have the separate
[INTRINSIC_FEATURE_SYMMETRY_CHECK.md](INTRINSIC_FEATURE_SYMMETRY_CHECK.md).
Those reports record source hashes, independent reconstruction, assumptions,
and limitations. They are internal checks, not promotion reviews. The
finite-time proposition has its own separately scoped check linked above.
The additional endpoint alternatives and their quantitative qualifications
are checked in [INTRINSIC_ENDPOINT_CHECK.md](INTRINSIC_ENDPOINT_CHECK.md).

The earlier arbitrary-amplitude near-orthogonal tanh fitting theorem in
[GAUSSIAN_BOUNDARY_RESULT.md](GAUSSIAN_BOUNDARY_RESULT.md) is unchanged.
Its restriction is not reinterpreted as a necessary condition. The new exact
statements apply much more broadly, but do not by themselves extend that
all-time theorem. No nonvanishing-probability Gaussian failure event has been
proved. A prescribed-forcing instability or an engineered bad basin is not
such an event, and failure to fit would not itself prove incompressibility.

The highest-leverage unresolved step is quantitative control of the adaptive
initialized backward response over a finite scalar-ascent horizon. The
conditional planar mixed-sign construction gives a concrete nonorthogonal,
rank-deficient test class for that step without adding a small-label assumption.
