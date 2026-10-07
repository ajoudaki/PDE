# Gaussian calculus can generate synthetic compact initialization components

2026-10-06. Current synthesis of the Gaussian-jet continuation of this
study. The strongest complete positive result below constructs theoretical
tanh neurons and their feature metric on the circle. A second finite-source
theorem constructs reduced mixers from computable Gaussian source laws.
Neither is yet the requested full nonlinear, all-time dense comparison.

The research and rigorous-proof workflows were used to separate exact
identities, complete initialization modules, and unresolved dynamical
claims. All new author proofs were read by the lead. The selection and
general-dimensional quadrature modules additionally passed a bounded
same-study reconstruction; this is not promotion or a blind review.

## 1. Target and bottom line

The reference remains the two-hidden-layer tanh network

\[
h(x)=\tanh(Ax/\sqrt d),\qquad g(x)=\tanh(Wh(x)),\qquad
f_n(x)=w^Tg(x)/n,
\]

with independent standard Gaussian first-layer entries, hidden entries
of variance \(1/n\), zero readout, squared mean loss, and mobilities
\((n,1,n)\). The desired direct model must use only the data and the
initialization law, preserve nonlinear feature learning, and approximate
an independent canonical dense run over the entire physical training
trajectory and sphere, including the endpoint. The previous strict target
\(C_{\mathrm{data},\delta}/\sqrt n\), and the weaker inherited
dense-variability scale, remain distinct.

Gaussian calculus is useful here in a concrete way. It can compute joint
jet/harmonic moments and, at fixed program size, jointly evaluable source
laws and forward/transpose contractions. Those can replace the empirical
source Gram and initialized action matrices in a synthetic selection step.
That selection needs only a constant-factor increase in neuron count and
preserves the quadratic retained-storage format.

It is **not** correct to replace each neuron's coefficients or weights by
their expectation. Their marginal means can all vanish. Nor does a source
Gram determine the joint source law or its future nonlinear actions.

## 2. Complete positive theorem: theoretical tanh neurons on the circle

For this theorem only, use \(d=2\), let
\(v_\theta=(\cos\theta,\sin\theta)\), and define the initial
first-layer population pairing

\[
K(\theta,\psi)=\mathbb E_{a\sim N(0,I_2)}
 [\tanh(a^Tv_\theta)\tanh(a^Tv_\psi)].
\]

For every \(0<\varepsilon\le1/2\), a deterministic construction
produces rows \(a_1,\ldots,a_q\in\mathbb R^2\) and a positive definite
\(q\)-by-\(q\) metric \(H\), using no data and no dense realization,
such that, with \(h_C(\theta)_i=\tanh(a_i^Tv_\theta)\),

\[
\sup_{\theta,\psi}
|h_C(\theta)^THh_C(\psi)-K(\theta,\psi)|\le\varepsilon,
\qquad q\le C[\log(C/\varepsilon)]^{3/2}.
\tag{1}
\]

The delivered initialization stores \(2q\) row entries and \(q^2\)
metric entries: \(O((\log(1/\varepsilon))^3)\) reals in total. In
particular \(\varepsilon=1/n\) gives \(q=O((\log n)^{3/2})\) and retained storage
\(O((\log n)^3)\). There are no moving variables in this initialization
module itself; it does not specify a trained two-layer surrogate.

Here is its constructive proof. Use an angular cutoff \(J\ge1\), and
write

\[
c_j(a)=\int_0^{2\pi}\tanh(a^Tv_\theta)e^{-ij\theta}
                         \frac{d\theta}{2\pi},\qquad
h_{a,J}(\theta)=\sum_{|j|\le J}c_j(a)e^{ij\theta}.
\]

The [harmonic calculation](GAUSSIAN_HARMONIC_JETS.md), Sections 1–2,
proves that even modes vanish, every odd mode has positive second moment,
different complex modes have diagonal covariance, and the following
continuous, computable radial envelope bounds the entire angular tail:

\[
\sup_\theta|\tanh(a^Tv_\theta)-h_{a,J}(\theta)|\le e_J(a),
\qquad \mathbb Ee_J^2\le C e^{-cJ^{2/3}}.
\tag{2}
\]

For an explicit formula without a singularity at zero, put, within this
formula only,

\[
u=\frac{4\|a\|}{\pi+\sqrt{\pi^2+16\|a\|^2}},
\qquad e_J(a)=\frac{2u^{J+1}}{1-u}.
\]

Indeed \(u=\exp[-\operatorname{arsinh}(\pi/(4\|a\|))]\) away
from zero, so this is exactly the geometric Fourier-tail envelope in that
proof. Gaussian radial tails give the second inequality in (2).

Form a real source basis from the real and imaginary parts of \(c_j\)
for positive odd \(j\le J\), together with \(1,e_J\). Its dimension is

\[
R=2\#\{1\le j\le J:j\text{ odd}\}+2\le J+3.
\]

This basis is independent. Polar angle orthogonality separates all
nonzero harmonic modes; each real sine/cosine pair has positive variance.
The remaining two radial functions are independent because \(e_J\) is
zero at radius zero and strictly positive, nonconstant, at positive
radii. All coefficients, their covariances, and their derivatives on
bounded boxes are computable by ordinary finite-dimensional quadrature.
The coefficient functions are bounded; the envelope grows at most
linearly in radius. Thus Gaussian second-moment tail bounds are effective.
Positive definiteness of the finite Gram follows from the independence
just proved, so increasing-precision integration eventually certifies a
positive eigenvalue bound and permits computable whitening.

Apply [synthetic source selection](GAUSSIAN_SYNTHETIC_SELECTION.md) to
this whitened basis. It chooses at most \(16R\) Gaussian-parameter marks,
which are precisely the initial rows \(a_i\), and a metric \(H\) giving
exact source pairings. A positive diagonal comparison metric also controls
selected residuals. Since \(e_J\) belongs to the source space, the
[envelope-transfer lemma](GAUSSIAN_ENVELOPE_TRANSFER.md) applies uniformly
to every angle. If \(\eta=(\mathbb Ee_J^2)^{1/2}\), it gives

\[
\sup_{\theta,\psi}
|h_C(\theta)^THh_C(\psi)-K(\theta,\psi)|
\le6\eta+11\eta^2.
\]

Choose \(J=C[\log(C/\varepsilon)]^{3/2}\), with an integer rounding
and sufficiently large absolute constants, so that \(\eta\le
\varepsilon/17\). This proves (1). The constants are effective: the
proof of (2) bounds explicit Gaussian integrals and geometric tails.

Initialization uses only Gaussian/angular quadrature, finite linear
algebra, and deterministic spectral selection. If its temporary positive
quadrature pool has \(P\) nodes, the exact-real sparsification work is
\(O(PR^3)\), plus source evaluation, moment computation, and whitening.
The pool and source basis can be discarded after the rows and \(H\)
are formed. Its size and required precision are not bounded efficiently
here; it may exceed \(n\). It contains synthetic two-dimensional marks,
not a width-\(n\) initialized network. The effective strict-margin search
in the selection note handles undecidable exact comparisons, at the cost
of having no useful general running-time bound.

This is an initialization-pairing theorem, not a prediction-trajectory
theorem. Freezing this feature block and fitting a readout would not prove
agreement with the specified nonlinear dense learning procedure.

For a simpler fully explicit alternative in arbitrary fixed dimension,
[Gaussian feature quadrature](GAUSSIAN_FEATURE_QUADRATURE.md) constructs
positive-weight rows directly on a lattice. It uses
\(O_d((\log(1/\varepsilon))^{3d/2})\) rows, \(dq+q\) retained reals,
and \(O(dq)\) initialization arithmetic plus elementary-function
evaluations. Its pairing guarantee is uniform on the entire sphere.
It requires no spectral search. This general-dimensional alternative
also concerns only the initial first layer.

## 3. What Gaussian calculus computes, and what it must not erase

The finite Chebyshev/harmonic conversion in the user's calculation is
linear. At fixed jet order, Gaussian integrability justifies exchanging
its angular integrals with expectation and Gaussian integration by parts.
Products of coefficients require joint products of jets, with all reused
matrix dependencies retained. Sines and cosines are deterministic test
functions; they introduce no probabilistic obstruction.

For tanh, flipping one first-layer row and the corresponding hidden-matrix
column leaves predictions unchanged. The Gaussian law, loss, mobilities,
and training flow respect this symmetry. Hence every integrable tagged
feature coefficient or jet has mean zero, even during training. The
nontrivial information is in joint products and shared Gaussian marks.
Section 3 of the harmonic note proves this for arbitrary fixed data and
labels, not only orthogonal data.

There is an explicit feature-learning calculation beyond initialization.
For one training sample, Sections 4–5 of that note derive the exact
finite-width conditional moments of the first nonzero hidden-feature jet.
They then identify its limiting joint source with the initial feature:
two Gaussian coordinates for the initial row and one additional independent
Gaussian for the reverse response. A nonzero conditional mean from reusing
the forward matrix is essential. All its coefficients are scalar Gaussian
integrals; no dense array or population-response oracle is required.
The physical second time derivative is obtained with the stated
\(4y^2\) conversion from feature time. This is a fixed-order limiting
law, not an exact finite-width Gaussian replacement or a trained-model
error theorem.

For prescribed polynomial activations and a fixed finite derivative
program, Section 7 gives an exact finite-width evaluator. Abstract typed
Gaussian contraction graphs are summed over equality partitions; width
appears through falling factorials and known normalizations. Angular
integration becomes finite Fourier coefficient extraction. No initialized
\(n\)-by-\(n\) matrix is generated. The monomial and partition counts
can be enormous, and transferring the evaluator to tanh requires a
separate certified polynomial-approximation error. Exact algebra at a
fixed order is not a high-order convergence theorem.

## 4. The synthetic reduced-network initialization interface

For a finite source family in each layer, suppose its joint Gaussian-mark
law, source Gram, and initialized forward/transpose pairings are directly
computable. Let \(R\) bound its rank. The selection theorem constructs
at most \(16R\) marks per layer, an evaluation matrix \(P_j\), and
fixed metrics \(H_j\) satisfying \(P_j^TH_jP_j=I\).

If \(C\) is the correctly computed matrix of initialized cross-layer
pairings in the orthonormal source bases, initialize

\[
B_0=P_2CP_1^TH_1,\qquad
B_0^*=H_1^{-1}B_0^TH_2=P_1C^TP_2^TH_2.
\tag{3}
\]

First-layer rows are evaluated from the same selected source marks; the
raw readout is zero. The corrected optimizer stores the opposite-sign
fitting state \(y-f_C\), initialized at \(y\); the book's canonical
residual \(f_C-y\) consequently starts at \(-y\). These are theoretical values once the stated source program
is available. They are not expectations of the old randomly selected
weights, and their construction does not need an existing dense candidate
pool.

For two hidden layers with at most \(q\) selected neurons each, the old
corrected optimizer would retain at most \(q^2+dq+q+m\) moving reals,
plus \(O(q^2+m(d+1))\) fixed metric/data/cache entries, after discarding
the source program and marks. Thus a source rank
\(R=O((\log n)^{3d/2+1})\), **if directly supplied with the necessary
error control**, preserves the previous \(O((\log n)^{3d+2})\)
retained-storage order. Mark dimensions and programs must be discarded or
counted separately; they are not hidden in this formula.

Equation (3) represents projected operator actions. It equals the full
forward or transpose action only on paired sources whose images are
included in the other source space. A new nonlinear feature can have a
fresh Gaussian component orthogonal to all previously retained operands.
The exact three-query calculation in
[DIRECT_GAUSSIAN_ATTEMPT.md](DIRECT_GAUSSIAN_ATTEMPT.md) shows that such a
component changes the next nonlinear prediction. A small or zero missing
linear contraction does not permit discarding that component.

Non-diagonal metrics also change gate adjoints. Therefore (3) cannot be
inserted into ordinary backpropagation without rederivation. The relevant
runtime is the explicitly corrected autonomous optimizer of the authorized
compression construction. Its old paired proof is not automatically a
proof for the synthetic sources.

## 5. Why the full theorem does not yet follow

Three obligations remain substantive.

1. **Growing source programs.** The book's Gaussian compiler treats each
   fixed finite program. The required number of jets, queried directions,
   and responses grows with accuracy. Quantitative joint-law and source-tail
   control must hold at that growing size, with computable error budgets.
2. **Own nonlinear feedback.** Source approximation must control the actual
   synthetic model's forward actions, reused adjoints, gates, and residuals
   throughout training. The envelope theorem helps transfer a proved
   source tail to selected neurons; it does not produce the neural tail
   or its dynamical stability.
3. **Dense-reference identification and endpoints.** A population route
   still needs a quantitative dense-to-population bound, including bias.
   Alternatively, a coupling to a canonical-law virtual dense run can use
   [VIRTUAL_REFERENCE.md](VIRTUAL_REFERENCE.md) and the dense-pair bound.
   Either route must preserve physical time, sphere supremum, and fitted
   endpoints. Independent fitting of the labels is insufficient.

The supplied single-origin continuation needs special care. The exact
[continuation audit](GAUSSIAN_JET_CONTINUATION.md) finds that its certified
jet cutoff grows, at fixed problem parameters, like a power of \(\log n\)
times \(\exp(C(\log n)^{3/2})\). This is a sufficient cost of that
certificate, not a lower bound on every algorithm or a change to retained
storage. A conditional staged-current-state Taylor method has much smaller
orders, and the note supplies its exact Gaussian-word recursions, but the
required growing-program stability is not yet proved.

Moreover, high-probability analytic bounds for realized networks do not
automatically justify analytic continuation of unconditional expected
jets. The audit gives an explicit counterexample:
\(g(t,G)=(1+t^2G^2)^{-1}\), with standard Gaussian \(G\), has bounded
holomorphic strips on increasingly likely Gaussian truncation events, but
the Taylor coefficients of \(\mathbb Eg(t,G)\) grow as
\((-1)^k(2k-1)!!\); its Taylor series at zero has radius zero.
This is a counterexample to that inference, not to the desired tanh
construction. Conditioning, Gaussian-tail control, or a different
continuation scheme must be justified quantitatively.

## 6. Result status and next bottleneck

Theoretical neuron selection is now proved under an effective source-law
contract, with the same quadratic metric/mixer storage order. A complete
direct, dataset-blind circular first-layer construction follows by the
harmonic-envelope synthesis in Section 2. General-dimensional explicit
quadrature and the three-Gaussian second-jet law provide additional concrete
modules. No computational experiment supports or is needed for these
statements.

The highest-leverage next theorem is a quantitative law-computable source
approximation retaining both orientations of the reused Gaussian operator,
with a common computable error envelope along the model's own evolution.
Proving that at the existing source rank would make synthetic selection
applicable to training. It is not equivalent to merely evaluating more
individual Gaussian moments.

The requested complete direct compact model, at the old storage order and
the specified dense-run trajectory accuracy, remains open. The present
results neither strengthen label restrictions for that target nor claim to
meet it under the full general activation/data scope. Dataset-blindness is
proved only for the initial first-layer modules; training jets and their
theoretical moments generally depend on inputs and labels.
