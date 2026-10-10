# Sample compression under geometric and spectral structure

Date: 2026-10-10. Author-derived bounded exploration, not a new theorem for
all three complete-trajectory compression methods. The finite-time and
finite-moment statements below have direct proofs. The all-time extension
is explicitly conditional. No experiment or paper change is made.

## 1. What should become independent of the sample count?

Use the paper's scalar-output dense network, normalized inputs
v=x/sqrt(d), zero initial readout, squared loss averaged over samples,
and block mobilities (n,1,...,1,n). The requested observable is prediction
error against the same-initialization dense network, not merely error
against a simple target. Keep the whole-sphere query domain for Legendre
and Harmonic and the declared-panel domain for Taylor distinct.

At fixed accuracy, the desired retained data description and compressed
state should stop growing with m. Reading the data, finding its weights,
and constructing the compressed initialization can still cost O(m) or
more. Keeping an external full-data oracle is not sample compression.
There is no claim here that an arbitrary ambient input vector can be
stored or read in space independent of d.

This is a new direction. The current theorem fixes the dataset as width
grows and explicitly excludes a uniform growing-data limit. Simple labels
or low latent dimension do not, by themselves, establish such a limit.

## 2. Compress the empirical measure, not just the label vector

Replace the averaged loss by a weighted loss

\[
 \mathcal L(\theta)=\frac1m\sum_a(f_\theta(x_a)-y_a)^2,
 \qquad
 \mathcal L_{\rm rep}(\theta)
       =\sum_{j=1}^{N}\omega_j(f_\theta(x_j)-y_j)^2,
 \quad \omega_j>0,\quad\sum_j\omega_j=1.
\]

The representatives and weights are computed from the initial data,
not from later dense training. They are then fixed. Training stays
autonomous. For exact repeated observations, retain each distinct pair
with its frequency weight: the loss, gradient and complete dense trajectory
are identical. Repeating the entire dataset therefore requires no extra
training information. Unequal cluster masses cannot be replaced by equal
weights without changing the objective.

In mobility-normalized parameter coordinates
theta=(W^(1)/sqrt(n),W^(2),...,W^(L),w/sqrt(n)), define the per-example
force locally in this section by

\[
 F(\theta,v,y)=-2(f_\theta(\sqrt d\,v)-y)
                   \nabla_\theta f_\theta(\sqrt d\,v).
\]

The dense parameter velocity is exactly the empirical average of F.
Thus the relevant sample complexity is the complexity of these evolving
forces, not the complexity of y alone.

## 3. A proved finite-horizon sample cap

Fix n, the realized initialization, a finite T, and a uniform label bound
|y|<=M. Assume the paper's smooth activation class; unbounded activation
values are permitted. In the normalized coordinates, both original and
weighted-representative flows are ordinary gradient flows. Since their
initial outputs vanish, their initial losses are at most M^2, and

\[
 \frac{d\mathcal L}{dt}=-\|\dot\theta\|_2^2,
 \qquad
 \int_0^T\|\dot\theta\|_2\,dt\le M\sqrt T.
\]

Hence both paths remain in the closed parameter ball of radius M sqrt(T)
about initialization, independently of m. Smoothness and compactness
give finite bounds there for the parameter Lipschitz constant A_T of F,
the data Lipschitz constant B_T of F in the metric
||v-v'||_2+|y-y'|, and the prediction-gradient bound P_T over the whole
input sphere. These are definitions of local bounds, not claims of small
or width-uniform constants. The parameter tube, input sphere and label
interval are compact; derivative bounds can be taken on a slightly larger
compact neighborhood. Energy and local existence also give continuation
through every finite T.

Suppose every observation is assigned to an observed representative with
joint-data distance at most h. Give that representative its assigned
frequency weight. For every parameter state in the tube, the two averaged
forces differ by at most B_T h. Subtract the two ODEs, use the same
initialization, and integrate the scalar differential inequality to get

\[
 \sup_{0\le t\le T}\|\theta_m(t)-\theta_{\rm rep}(t)\|_2
 \le B_T h\frac{e^{A_TT}-1}{A_T},
\]

where the quotient means T when A_T=0. The intervening parameter segment
lies in the same convex tube, so

\[
 \sup_{0\le t\le T}\sup_{\|x\|=\sqrt d}
 |f_m(t,x)-f_{\rm rep}(t,x)|
 \le P_T B_T h\frac{e^{A_TT}-1}{A_T}.             \tag{1}
\]

No minimum sample Gram eigenvalue is used. Choosing h from (1) gives an
m-independent number of representatives whenever the joint-data support
has an m-independent covering bound. The statement is deterministic at
the fixed initialization and is about the actual nonlinear dense flow.
It is not a kernel substitution. Its constants may depend badly on n,T,
the initialization, activation, depth, dimension and M. Consequently this
lemma alone does not preserve the paper's sharp width exponents.

### Latent geometry without a latent-coordinate oracle

Suppose z lies in [0,1]^k and the map
z -> (x(z)/sqrt(d),y(z)) is A-Lipschitz in the preceding joint-data
metric. If A=0 the image is a single pair and one representative suffices.
For A>0, a latent grid with Euclidean cell diameter h/(2A) covers the
image by at most

\[
 \left(1+\frac{2A\sqrt k}{h}\right)^k
\]

sets of diameter at most h/2. Greedily keeping an observed pair only
when it is farther than h from previous representatives therefore keeps
at most this many pairs: two kept pairs cannot lie in one such set.
Every processed point is within h of its assigned representative.
Frequency counts produce the required weights. The algorithm never
needs z or the generator; their existence bounds its output size.
Naive setup costs O(m N(d+1)) scalar work and O(N(d+1)) retained entries,
with O(N) running counts. Finite-bit counts/weights also need precision
accounting; real-coordinate counts do not remove a possible log(m) bit cost.

For fixed n,T and regularity constants, (1) consequently gives a bound
of the form N <= C_T epsilon^(-k), independent of m. The dependence of
C_T just described is essential. Merely continuous maps on a fixed compact
latent set have a modulus of continuity and yield a finite cap through its
inverse, but no rate follows from k alone. For d>=2, every finite data list
on the sphere can be visited by a continuous one-dimensional curve (using
spherical arcs for unit inputs), with arbitrarily poor modulus. For d=1
the input sphere has only two points and its covering problem is trivial.
An unspecified Lipschitz
constant does not repair this lack of a uniform quantitative class.

For sphere inputs and a uniformly Lipschitz target, the graph inherits
the sphere's intrinsic dimension d-1; the analogous covering count is
C_d h^(-(d-1)) with constants depending on target regularity. Low latent
dimension replaces that exponent by k. Self-intersections of the input
generator do not invalidate compression of observed pairs, but may make
the label nondeterministic given x and therefore obstruct exact fitting.

### A square-loss refinement: average labels within input clusters

For finite-time dynamics, smooth labels are not even necessary if synthetic
representative labels are allowed. Cover only the inputs, and give an
input representative the mean label of its cluster. This uses

\[
 F(\theta,v,y)=-2f_\theta(\sqrt d v)\nabla_\theta f_\theta(\sqrt d v)
                         +2y\nabla_\theta f_\theta(\sqrt d v).
\]

The force is affine in y. Let U_T be the input Lipschitz constant of
f grad(f), and V_T that of grad(f), uniformly on the parameter tube.
Within an input cluster of radius h, subtracting the representative force
and averaging gives norm at most 2(U_T+M V_T)h. The term containing the
cluster mean cancels exactly. Apply the same ODE proof with this force
bound. This retains the input covering exponent without requiring smooth
labels. It does not solve the all-time stability question, and the mean
label need not be the target value at the representative input.

## 4. Spectral structure can improve covering to moment matching

There is a sharper, exact algebraic reduction when the relevant scalar
test functions belong to a fixed finite-dimensional space. Choose a basis
psi_1,...,psi_R including the constant function. The empirical vector of
their averages is a convex combination of the observed evaluation vectors.
It can be represented using at most R observations with positive weights.

Here is the finite-data proof. If a representation uses more than R
positive weights, its evaluation columns are linearly dependent. Choose
a nonzero dependence alpha. The constant coordinate gives sum(alpha)=0,
so alpha has both signs. Subtract t alpha from the weights, with t the
smallest positive weight/alpha among positive alpha entries. The new
weights are nonnegative, preserve every moment and total mass, and one
more weight vanishes. Iterate. This is the finite-support form of positive
cubature; it requires no future training state.

If, uniformly throughout a known parameter tube,

\[
 \left\|F(\theta,v,y)-\sum_{j=1}^R a_j(\theta)\psi_j(v,y)\right\|
 \le\eta,
\]

then moment matching cancels the displayed expansion exactly. The full
and weighted force averages differ by at most 2 eta, because both measures
have mass one. Substituting 2 eta for B_T h proves the corresponding
finite-time trajectory estimate. Approximation only at initialization is
not sufficient, nor may the test space be chosen from unavailable future
forces without an initialization-only construction.

For sphere-polynomial force approximations of degree K, the scalar space
has dimension binomial(d+K,d)-binomial(d+K-2,d), of order K^(d-1)
at fixed d>=2. If the *force family*, not merely the label, has a uniform
exponentially decaying spatial approximation tail, K grows logarithmically
with inverse force tolerance and the sample cap is correspondingly much
smaller than a Lipschitz covering bound. Uniform approximation is needed
for arbitrary empirical input measures; small harmonic L2 energy alone
does not control a sphere supremum or points concentrated in a narrow spike.

The general positive-cubature result is Bayer and Teichmann, *The proof of
Tchakaloff's theorem*, Corollary 2; its primary proof was checked at
https://arxiv.org/pdf/math/0502473. Only the finite-data argument just given
is needed here. No literature claim about complete nonlinear all-time
compression is imported from that theorem.

### Exact all-time special case: a fixed finite output dictionary

Suppose an architecture is exactly of the form
f_theta(x)=sum_{i=1}^R a_i(theta) psi_i(x) for every parameter
state, with known fixed functions psi_i and a globally twice continuously
differentiable coefficient map. The coefficients may depend nonlinearly
on all trainable layers. The loss expands as

\[
 \mathcal L(\theta)=a(\theta)^\top G a(\theta)
       -2a(\theta)^\top b+\frac1m\sum_a y_a^2,
 \quad
 G_{ij}=\frac1m\sum_a\psi_i(x_a)\psi_j(x_a),\quad
 b_i=\frac1m\sum_a y_a\psi_i(x_a).
\]

Thus its gradient depends on the data only through
R(R+1)/2+R numbers. Retaining these statistics gives exactly the same
parameter ODE, same initialization and same predictions. The nonnegative
loss and its energy identity prevent finite-time parameter escape exactly
as in Section 3; local smoothness then gives global existence. Thus this
exact sample reduction holds for all times. A positive weighted subset with at most
1+R(R+1)/2+R atoms is another realization. Deep linear networks are an
example within the current analytic activation class. Non-affine polynomial
activations supply further examples, but are outside its bounded-strip-
derivative class. General tanh or other nonpolynomial deep networks are
not asserted to remain in a finite input dictionary.

This proves that all-time sample compression is possible under an actual
finite sufficient-statistic structure. Bandlimited labels alone do not
provide that structure for the network being trained.

## 5. The main unresolved issue is all-time stability, not data averaging

Let P be the orthogonal projection in normalized sample space onto a
proposed low-dimensional label/response space. With the paper's unnormalized
tangent Gram K(t), the dense residual satisfies dot(r)=-2 K(t)r/m. Even
if the initial residual lies in range(P), its omitted derivative is

\[
 (I-P)\dot r(0)=-\frac2m(I-P)K(0)P r(0).
\]

It need not vanish. A nonuniform input distribution and feature learning
can couple low label frequencies to high response frequencies. The relevant
positive condition is control of this leakage over training, together with
conditioning on the resolved response space. An initial spectral gap only
on the label vector is not enough by itself.

The existing full-sample gap cannot remain a fixed normalized constant:
the population feature Gram has diagonal entries bounded by an activation/
depth constant, so gamma <= trace(Q)/m <= C and gamma/m <= C/m.
For unit normalized inputs the diagonal is in fact the same at every sample.
The current label cap Y <= beta^(-30L) gamma/m therefore does not permit
m -> infinity at fixed nonzero Y. Closely spaced inputs can make gamma
smaller still. These are limitations of the current theorem interface,
not proof that densely sampled smooth tasks require indefinitely growing
state. A growing-data theorem must use accuracy-relevant conditioning and
re-establish stability under a different sufficient label condition.

A precise sufficient all-time bridge is as follows. Suppose both full and
representative flows satisfy, on the promised query domain, a tail bound

\[
 \sup_{t\ge T,x}|f(t,x)-f(T,x)|\le A e^{-\kappa T}
\]

with A,kappa>0 independent of m and uniform over the representative
construction. Choose T with 2A exp(-kappa T)<=epsilon/2, and make the
finite-time comparison at most epsilon/2. The triangle inequality gives
all-time error <=epsilon, including the endpoint. This bridge requires
no change to the optimizer at T; T is only used in the proof. Neither
low-dimensional labels nor Lipschitz latent generation has yet been shown
to imply its hypotheses for the current full feature-learning models.

Small absolute force error alone cannot replace this bridge. Scalar stable
systems with decay rates a and 2a have generators arbitrarily close as
a -> 0, yet their trajectories exp(-at) and exp(-2at) differ by 1/4
at t=log(2)/a. This example demonstrates nonuniform long-time sensitivity,
not an impossibility of compact representations of such simple curves.

## 6. How the three methods would use sample compression

The clean common composition is
full-data dense -> weighted-data dense -> width-compressed weighted model.
Its error is bounded by the sum of the two comparisons, on the same
query set and horizon. Weighted equations are easy to define; a proven
weighted all-time extension with controlled conditioning is a separate
obligation. One cannot substitute an effective count into the old theorem
while retaining the original gamma and every other hypothesis unchanged.

### Legendre

Use one response-memory pair per representative and temporal mode; replace
all uniform sample averages by weighted averages, and use the weighted
residual RMS for its clock. The exact weighted construction has moving
count n(d+1)+1+2(L-1)n N q, plus N(d+2) representative coordinates/labels/
weights and the original fixed (L-1)n^2 mixers. This is an algebraic
inventory, not a proved optimized order for the new data class. Its time
basis need not depend on the data. Selecting a coreset is nevertheless a
new, data-dependent sample preprocessing step, distinct from time-basis
obliviousness. A prescribed geometric cell partition is possible instead.

An alternative is to project the sample index itself onto fixed spatial
modes, sharing memories among nearby inputs. The common-projector
product-tail cancellation remains exact, but the source approximation,
evaluation of sample contractions without the full data, and feedback
stability need a closed reduced construction.

### Harmonic

This is the closest fit to spatial sample compression. Its joint space-time
source basis already shares coefficients across all sphere inputs; new
samples need not create new spatial basis functions. However, the current
runtime retains an m-dimensional deficit, an m-column training feature
matrix and a full m-by-m inverse. It also adds the initialized training
features exactly. Thus the current algorithm is not sample compressed.

Weighted representatives replace these sample-indexed objects by N-sized
objects. A more intrinsic alternative is a readout correction enforcing
only finitely many spatial residual moments, with an inverse on that
resolved space. This removes the structural need to preserve every sample
direction but changes the construction; discarded residual feedback must
be controlled. A pseudoinverse or ridge inserted into the existing exact
readout equation does not automatically preserve its cancellation proof.

### Taylor

The same weighted or projected runtime changes are needed. In addition,
its source dimension counts every declared input curve. Keeping every
original training point as a query after reducing the loss merely makes
those points passive: the panel still has m+p members. Sample compression
does not follow just by reducing the number of update-driving points.

There is a principled spatial-net extension. Suppose a finite anchor set
covers the desired query set within h in normalized input distance, and
both dense and compressed predictors have uniform input Lipschitz bounds
J_dense and J_comp throughout training. Then

\[
 \sup_{t,x}|f_{\rm comp}(t,x)-f_n(t,x)|
 \le \max_{\text{anchors }a}\sup_t
       |f_{\rm comp}(t,x_a)-f_n(t,x_a)|
       +(J_{\rm dense}+J_{\rm comp})h.
\]

This follows by adding and subtracting the two anchor predictions.
Use only training representatives and query anchors in the Taylor source
construction. On a Lipschitz latent image, the anchor count can have
intrinsic exponent k. The network still accepts an ambient x at inference;
no latent decoder is required. For an observed finite panel, a greedy input
cover is computable without the generator. For genuinely unseen points
over the entire latent support, coverage is an extra assumption or needs
a sampling-density/coverage theorem. This does not grant a low-k guarantee
off the latent support or over the whole ambient sphere.

## 7. Current conclusion

There is a concrete sample-compression mechanism, with a proved fixed-time
cap and exact all-time special cases. The low-complexity object should be
the empirical training force/response family, not just the label function.
Harmonic is the most direct spectral extension; Legendre can use an
upstream weighted data reduction; Taylor additionally needs query-space
compression if its original large panel is retained as the accuracy target.

The central open result is an accuracy-dependent, sample-uniform all-time
stability theorem for the evolving nonlinear responses, replacing the full
empirical minimum eigenvalue by controlled resolved-space conditioning and
small leakage. Preserving the current width exponents would additionally
require width-controlled source/transport constants. None of these missing
bridges is silently assumed to have been proved here.
