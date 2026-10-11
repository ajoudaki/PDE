# Canonical Gaussian initialization: fitting theorems and the remaining boundary

2026-10-10. This note supersedes the earlier engineered-basin discussion **as
an answer to the canonical-Gaussian question**. It does not retract those
deterministic basin constructions. Their Gaussian probabilities were not
controlled as width increases, so they did not establish the requested
probabilistic boundary.

## Outcome and scope

A complete, internally audited proof covers **tanh at both hidden layers**
on an open neighborhood of orthogonal input geometries and signed
common-magnitude label vectors. The common magnitude can be any fixed
positive number; signs are unrestricted, and nearby unequal magnitudes and
nonorthogonal inputs are included. It gives actual finite-width all-time
exponential fitting with probability tending to one. The neighborhood does
not shrink with width. Both exact zero readout and the book's tiny-Gaussian
readout are covered by separately checked arguments; see Section 3.

A separate arbitrary-label theorem covers a nonlinear activation subclass.
It includes any linearly independent inputs, not necessarily near orthogonal,
every finite mixed-sign label vector, finite parameter convergence, and an
eventual exponential rate independent of width on events whose probability
tends to one. Its first activation is linear; it is not a tanh/tanh theorem.

**The unrestricted two-hidden-tanh-layer target is not resolved.** The
arbitrary-label, nonorthogonal theorem has a linear first activation and a
nonlinear, nonsaturating second activation. The tanh/tanh theorem instead
restricts the inputs and label class. Neither may be presented as arbitrary
mixed labels on general nonorthogonal tanh data, or as a theorem for the entire
analytic activation class. No fixed-data, fixed-label Gaussian failure event
of probability bounded away from zero has been proved here. No compression
theorem is claimed from fitting alone.

## 1. Exact setup and probability question

Let the columns of \(X\in\mathbb R^{d\times m}\) be unit vectors; these are
the original sphere inputs divided by \(\sqrt d\). There are two trained
hidden matrices and a trained readout:

\[
 U=\phi_1(AX),\qquad H=\phi_2(WU),\qquad
 f=H^\top w/n,\qquad r=f-y,\qquad
 \mathcal L=\|r\|_2^2/m.
\]

The shapes of \(A,W,w\) are \(n\times d,n\times n,n\). The actual
gradient flow has mobilities \((n,1,n)\):

\[
 \dot A=-n\nabla_A\mathcal L,\qquad
 \dot W=-\nabla_W\mathcal L,\qquad
 \dot w=-n\nabla_w\mathcal L.
\]

Initially the entries of \(A\) are independent \(N(0,1)\), those of \(W\)
are independent \(N(0,1/n)\), the two matrices are independent, and
\(w=0\) exactly. This is the zero-readout setup used throughout this
investigation, not a perturbation around designed hidden weights. The
maintained book's distinct tiny-Gaussian-readout convention is not silently
identified with zero.

The dataset and labels are fixed independently of width and of every random
draw. A positive theorem here means

\[
 \Pr\!\left\{\lim_{t\to\infty}\mathcal L_n(t)=0\right\}
 \longrightarrow1\qquad(n\to\infty).
\]

A strong negative theorem would instead give fixed admissible data and labels
and fixed \(c,p>0\) for which

\[
 \liminf_{n\to\infty}
 \Pr\!\left\{\lim_{t\to\infty}\mathcal L_n(t)\ge c\right\}
 \ge p.
\]

In both statements training time tends to infinity at each finite width
first. Neither a population plateau nor rare finite-width bad basins are a
substitute. For the tanh question, incompatible duplicate/antipodal samples
and a singular initial population feature Gram are excluded.

## 2. The completed positive subclass

Assume \(m\ge2\), \(X\) has column rank \(m\), and

\[
 \phi_1(z)=z,\qquad
 0<c_\phi\le\phi_2'(z)\le L_\phi<\infty,\qquad
 |\phi_2(z)-z\phi_2'(z)|\le M_\phi<\infty
 \quad(z\in\mathbb R).
\]

The three activation constants in this display are fixed. Nonlinear analytic
examples are

\[
 \phi_2(z)=z+\varepsilon\tanh z
 \quad\text{or}\quad
 \phi_2(z)=z+\varepsilon\arctan z,
 \qquad\varepsilon>0.
\]

These examples have bounded derivatives on an appropriate complex strip,
but unbounded values, so they belong to the allowed activation class. The
first example has \(c_\phi=1\), \(L_\phi=1+\varepsilon\), and
\(M_\phi=\varepsilon\).

For \(n\ge d+1\), there is an initialization event of probability at least

\[
 1-\frac{524304(d^2+d)}n
 -2\exp\!\bigl((2n-d)\log9-8n\bigr)
\]

on which **every finite label vector** is fitted, with finite parameter
limits and eventual exponential loss decay. The event includes the
probability-one condition \(\operatorname{rank}H(0)=m\). The probability
bound is useful only when positive, and tends to one for fixed \(d\).
There is no small-label condition and no restriction on label signs.

More strongly, for each fixed dataset, activation, and nonzero label vector,
there are deterministic \(t_*<\infty\) and \(c>0\), independent of width,
such that, with probability tending to one,

\[
 \mathcal L_n(t)\le \frac{\|y\|^2}{m}
                         e^{-c(t-t_*)}\qquad(t\ge t_*).
\]

For zero labels the zero-readout network is already fitted. The rate
certificate for nonzero labels can be very small; no practical-rate or
polynomial-in-label-size claim is made. The full-column-rank condition means
\(m\le d\), but does not mean orthogonality: any fixed linearly independent
sphere dataset is covered, including correlated inputs.

The complete theorem, explicit constants, Gaussian probability calculation,
and all-time proof are in
[GAUSSIAN_NONLINEAR_TOP_POSITIVE.md](GAUSSIAN_NONLINEAR_TOP_POSITIVE.md).
The two trained hidden matrices should not obscure its limitation: only the
second activation is nonlinear.

The [complete internal audit](GAUSSIAN_NONLINEAR_TOP_CHECK.md) passed on the
frozen proof. The event statement above incorporates its minor precision
recommendation to name the probability-one initial-rank condition.

The same subclass also admits independent Gaussian initial readouts with any
uniformly bounded stored variance. This includes zero, the maintained book's
variance \(1/n^2\), and order-one stored variance, always with the same
outer \(1/n\) in the predictor. The extension proves the fitting, rate,
and finite-parameter conclusions for each fixed label vector with probability
tending to one; it does not claim the zero-readout theorem's simultaneous
all-label event. See the [complete extension](GAUSSIAN_READOUT_EXTENSION.md)
and its [internal audit](GAUSSIAN_READOUT_CHECK.md), which also passed.

### Why this proof avoids small labels

The argument permits large hidden motion; it does not try to keep the feature
matrix close to initialization. The exact identity

\[
 W(t)^\top W(t)-A(t)A(t)^\top/n
 =W(0)^\top W(0)-A(0)A(0)^\top/n
\]

protects the first-layer geometry. With the displayed Gaussian probability,

\[
 A(t)^\top A(t)/n\succeq I_d/512
 \qquad\text{for every }t\ge0,
\]

simultaneously in the labels. Full input column rank and the top derivative
floor therefore give a lower bound for the moving tangent Gram proportional
to \(\|w(t)\|^2/n\).

It remains to prevent this readout factor from collapsing. For this proof
only, put \(q=\|w\|/\sqrt n\), \(a=\|A\|_F/\sqrt n\),
\(\rho=\sqrt{\mathcal L}\), and \(S(t)=\int_0^tq(s)\rho(s)\,ds\).
The scalar balance identity gives

\[
 \left|\frac{d}{dt}(a^2-q^2)\right|
 \le4M_\phi q\rho.
\]

Combined with the matrix invariant, it bounds the feature size by a
constant times \(q^2+1+S\). Strict initial loss decrease makes the prediction
norm bounded away from zero after a finite time. Consequently
\(q\ge c_0/(1+S)\), for a positive, fixed trajectory constant \(c_0\).
Loss dissipation and the tangent lower bound now imply

\[
 \frac{d\rho}{dS}\le-\frac{c_1}{1+S}
\]

for another positive constant \(c_1\). The integral on the right diverges
as \(S\to\infty\), whereas \(\rho\ge0\). Hence \(S\) is bounded,
\(q\) stays bounded below, and loss decays exponentially. The detailed
proof gives all these constants and proves finite parameter convergence.

An attempted stronger matrix balance for \(WW^\top-ww^\top/n\) is false:
off-diagonal entries mix different neurons' derivatives. Only the scalar
trace balance just used is asserted. This correction is essential to the
proof.

## 3. Both hidden activations tanh: a Gaussian arbitrary-amplitude theorem

Keep the exact model, initialization and optimizer in Section 1, now with
\(\phi_1=\phi_2=\tanh\). Suppose

\[
 m\ge2,\qquad d\ge m,\qquad X^\top X=I_m,\qquad
 y_i=a\sigma_i,\quad \sigma_i\in\{-1,1\},\quad a>0.
\]

Every label has the same arbitrary fixed absolute value, with unrestricted
signs. There is **no upper bound on this fixed amplitude** and no dependence
of it on width.

There exists a deterministic \(c>0\), independent of \(n\), such that

\[
 \Pr\!\left\{
  \mathcal L_n(t)\le\mathcal L_n(0)e^{-ct}
  \text{ for every }t\ge0
 \right\}\longrightarrow1.
\]

In particular the actual finite-width terminal loss is exactly zero on
these events. For every prescribed failure probability there is a sufficiently
large width; the present proof does not quantify that width threshold or give
a useful explicit lower bound for \(c\). Both may depend on the fixed
problem. No neurons are paired or reinitialized.

There is also an open neighborhood of each such label vector in which every
fixed label vector is fitted with probability tending to one. Thus exact
equality of the label magnitudes is not necessary. The neighborhood radius is
not quantified, and these neighborhoods are not proved to cover all label
ratios. This first proof concerns label perturbations only; the additional
input-perturbation proof is stated separately below.

### The construction that closes this proof

For an individual first preactivation \(z\), introduce only as a proof
coordinate

\[
 \xi=\frac z2+\frac{\sinh(2z)}4.
\]

Its derivative is \(1/\tanh'(z)\). On orthogonal training inputs this
exactly cancels the first-layer derivative multiplying the backward field in
the original gradient-flow equation. The first activation as a function of
\(\xi\) is globally Lipschitz, with derivative \(\tanh'(z)^2\le1\).
The dynamics have not been changed: recovering \(z\) gives the original
muP gradient flow, and the initial raw weights are still iid Gaussian.

This yields a well-posed strong population evolution and a dimension-uniform
Euler comparison. The initialized transformed roots have finite second
moments; the maintained fixed-Gaussian-program theorem admits precisely such
roots, reused Gaussian matrices and their true adjoints, and causal scalar
contractions. All its hypotheses are checked in the proof. A fixed Euler
transcript is sent to large width before its time mesh is refined.

Oddness absorbs the label signs into the orthogonal inputs. Population sample
permutation symmetry then reduces training to a single scalar prediction,
without imposing symmetry on any finite Gaussian draw. Readout linearity
forces this scalar prediction to reach any fixed target in finite feature
time. Differences between transformed first-layer sample coordinates cannot
vanish at finite feature time; consequently the readout and middle-weight
tangent blocks together remain positive in every sample direction through
the fitted endpoint. The endpoint-capture lemma transfers this conclusion
from one fixed physical-time snapshot to every subsequent time of the actual
finite-width flow. A compact-path kernel margin also controls the preceding
interval, producing the all-time exponential estimate.

The complete derivation is in
[GAUSSIAN_POSITIVE_GEOMETRY.md, Sections 11 and 13](GAUSSIAN_POSITIVE_GEOMETRY.md#11-candidate-complete-theorem-for-the-orthogonal-pair).
It relies only on the explicitly inspected generic construction in the
maintained `docs/12-three-sample-learning.qmd`, III.F.1--11, not on the
activation-specific short-horizon tail bounds elsewhere in the book.

The [complete internal audit](GAUSSIAN_TANH_ORTHOGONAL_CHECK.md) passed on
the frozen proof. It verifies the exact initialization, all finite-program
hypotheses, the order of limits, and the actual finite-width capture. It is
not an independent promotion review.

### Extension to an open nonorthogonal input and label class

The complete, internally checked extension in
[GAUSSIAN_NONORTHOGONAL_EXTENSION.md](GAUSSIAN_NONORTHOGONAL_EXTENSION.md)
has passed its [separate audit](GAUSSIAN_NONORTHOGONAL_CHECK.md). Its precise
statement is as follows. For every fixed sample count \(m\ge2\), amplitude \(a>0\),
and sign vector \(\sigma\in\{-1,1\}^m\), there is a fixed
\(\eta>0\) such that

\[
 \|X^\top X-I_m\|_{\rm op}<\eta,\qquad
 \|y-a\sigma\|_2<\eta
\]

imply, for some deterministic \(c>0\) independent of width,

\[
 \Pr\!\left\{
  \mathcal L_n(t)\le\mathcal L_n(0)e^{-ct}
  \text{ for every }t\ge0
 \right\}\longrightarrow1.
\]

Here the model, Gaussian law, exact zero readout, and mobilities are unchanged.
The input columns are unit vectors; the Gram condition with \(\eta<1\)
implies \(m\le d\). All data, labels, and \(a\) are fixed before the
Gaussian draw and independently of width. Taking \(\eta<a/2\) if desired
preserves the chosen signs while allowing unequal magnitudes. The statement
is for each fixed dataset and label vector, not one random event asserted
simultaneously for all datasets and labels.

There is no smallness condition on the fixed amplitude \(a\). There is a
near-orthogonality condition and a near-common-magnitude condition. The
radius \(\eta\), rate \(c\), and sufficient width are not usefully
quantified and may deteriorate badly with amplitude or sample count. In
particular these open neighborhoods are not proved to cover every label
ratio or every positive-definite input Gram.

The extension does not assume a nonorthogonal population flow. It proves
Gaussian tail bounds for the backward fields of the orthogonal reference,
using dimension-scaled sensitivity to the initialized Gaussian matrix.
Gaussian integration by parts controls the initialized transpose action;
the learned middle-weight contribution is bounded separately by its exact
rank-one history. Gaussian concentration and the orthogonal empirical-law
limit turn these bounds into a high-probability tail estimate uniform on a
fixed time interval.

The actual finite-width perturbed dynamics are then compared in the bounded
first activations \(U\). Splitting the reference backward field at a fixed
tail threshold gives a width-independent stability estimate. First the
threshold is chosen, then the allowed input and label perturbation, and only
then width tends to infinity. The same strict finite-time capture test
controls the whole remaining trajectory. This is why the neighborhood is
fixed in width rather than merely a consequence of finite-dimensional
continuity at each width.

### Tiny Gaussian readout: a separate extension of the stated initialization

The frozen tanh proofs use exact zero readout. The following short addendum
checks the maintained book's distinct stored initialization
\(w_i(0)\sim N(0,1/n^2)\), independent of the hidden matrices, for the
same input and label class, shrinking the unquantified neighborhood if
needed. It is not an extension to order-one stored readout variance. The
[separate addendum check](GAUSSIAN_NONORTHOGONAL_CHECK.md#separate-addendum-vanishing-pointwise-initial-readout)
passed.

In fact the same argument works whenever
\(\|w(0)\|_\infty\to0\) in probability. Couple the new trajectory
with the exact-zero reference using the same hidden matrices. Since
\(|H_{ij}(0)|\le1\),

\[
 \|f(0)\|_2\le\sqrt m\,\|w(0)\|_2/\sqrt n
 \le\sqrt m\,\|w(0)\|_\infty\longrightarrow0.
\]

The initial loss is therefore bounded in probability. Put, only for this
calculation, \(p_0=\|w(0)\|_\infty\) and
\(S(t)=2\int_0^t\sqrt{\mathcal L_n(v)}\,dv\). The exact gradient
equations give

\[
 \|w(t)\|_\infty\le p_0+S(t),\qquad
 \|W(t)-W(0)\|_F\le p_0S(t)+S(t)^2/2.
\]

On a fixed time interval these replace the zero-initial-readout bounds by
the same width-independent bounded quantities. The first-feature stability
proof in Section 5 of the extension uses only those bounds and the reference
backward tails; it does not use zero readout for the perturbed trajectory.
Its initial squared state difference simply gains
\(\|w(0)\|_2^2/n=o_{\Pr}(1)\). Gronwall thus gives the same
finite-time closeness, with a term tending to zero in probability added to
the right-hand side. All tail thresholds and input/label tolerances are
chosen before taking width large, exactly as before.

The accumulated residual remains close to that of the reference. At the
capture snapshot, \(p_0+S(T)\le s_*+1\) with probability tending to one,
and

\[
 p_0S(T)+S(T)^2/2
 =\bigl((p_0+S(T))^2-p_0^2\bigr)/2
 \le(s_*+1)^2/2.
\]

Thus both strict capture and the preceding finite-time kernel margin persist.
The exponential bound has the same form, with the **actual** random initial
loss \(\mathcal L_n(0)\) as prefactor. For the book's tiny Gaussian
readout, the needed hypothesis follows directly from

\[
 \Pr\{\|w(0)\|_\infty>u\}
 \le2n e^{-n^2u^2/2}\longrightarrow0
 \qquad\text{for every fixed }u>0.
\]

This extension retains the initialized Gaussian law; it is not a Gaussian
perturbation around designed hidden weights.

## 4. What remains unresolved for general tanh data

For the actual two-nonlinear-layer tanh network, the renewed search supplies
the following exact facts and conditional bridges.

1. For distinct nonantipodal inputs and \(n\ge m\), both initialized feature
   matrices have full column rank almost surely. Every fixed nonzero label
   vector produces strict initial loss decrease. Gaussian sign symmetry does
   not cancel learning: the readout and hidden features become correlated.
2. If the input columns are independent, every finite positive-loss critical
   point with nonzero readout is a strict saddle. A trajectory that has
   decreased the loss cannot converge to a zero-readout state, whose loss
   equals the initial loss. This does **not** establish boundedness or saddle
   avoidance from the zero-readout slice.
3. A globally constructed one-direction residual reduction with positive
   initial readout-feature norm fits arbitrary fixed amplitudes exponentially.
   For orthogonal inputs, Section 3 now constructs and
   identifies the needed population path and supplies the finite-width
   bridge. For a general nonorthogonal opposite-label pair, the corresponding
   strong path and identification are still missing. The new near-orthogonal
   extension bypasses that construction by direct finite-width stability.
   Symmetry in law is not an identity for a finite Gaussian draw.
4. A proved endpoint-capture lemma can transfer an appropriate population
   theorem to exact finite-width fitting. It needs only a sufficiently late
   finite snapshot with small residual, positive full tangent Gram, and
   controlled backward moments. The continuity estimate is width-independent
   and does not require the largest backward coordinate to be bounded.
   Population fitting alone, or convergence on fixed finite intervals alone,
   is insufficient.

Complete calculations and the precise unproved population hypotheses are in
[GAUSSIAN_POSITIVE_GEOMETRY.md](GAUSSIAN_POSITIVE_GEOMETRY.md) and
[GAUSSIAN_POPULATION_POSITIVE.md](GAUSSIAN_POPULATION_POSITIVE.md). These
unresolved conditional lemmas are not counted as additional theorems. The
separate near-orthogonal extension above does not require their unproved
population hypotheses.

The positive subclass in Section 2 avoids both unresolved tanh mechanisms:
the exact matrix invariant protects lower features, and the derivative floor
prevents top-layer saturation from eliminating the useful tangent direction.
Tanh/tanh has neither guarantee from this proof. That is a proof boundary,
not a proof of failure of tanh.

### The obstruction to extending the scalar proof to arbitrary label ratios

A further bounded attempt tested both residual-direction control and
continuation in the labels. Neither closes the general case. The exact
identity explains the missing step. On an interval of nonzero residual,
write, locally in this calculation,

\[
 v=\frac{y-f}{\|y-f\|_2},\qquad
 \frac{ds}{dt}=\frac{2\|y-f\|_2}{m},\qquad
 R=\frac{\|w\|_2^2}{n},
\]

and let \(K\) be the full moving tangent Gram in the actual mobility metric.
A prime in the next display means differentiation with respect to \(s\).
The exact gradient equations give

\[
 f'=Kv,\qquad
 v'=-\frac{(I-vv^\top)Kv}{\|y-f\|_2},\qquad R'=2f^\top v,
\]

and hence

\[
 R''=2v^\top Kv
       -\frac{2f^\top(I-vv^\top)Kv}{\|y-f\|_2}.
\]

The second term vanishes on the scalar symmetric path used above. For
general labels, positive semidefiniteness of \(K\) gives it no definite
sign. Thus the protected scalar readout-feature estimate cannot simply be
reused when the residual rotates. This is a precise proof obstruction, not
a constructed failing Gaussian trajectory.

Continuation in labels proves that the certified fitting class is open. It
does not prove that this class is closed or covers all label vectors: capture
times could diverge or tangent margins could vanish at its boundary. The
current estimates do not rule out those alternatives. In particular, a union
of the neighborhoods in Section 3 must not be advertised as an arbitrary-label
theorem for tanh/tanh.

## 5. Negative search and the remaining boundary

The negative route tried symmetry cancellation, large-label alignment,
feature-rank collapse, and an admissible positive-floor periodic activation.
The first two mechanisms do not supply the desired counterexample: initial
Gaussian response is nonzero, and the exact one-direction alignment flow
cannot stall. The positive-floor example gives a candidate bad collapsed
state, but not an invariant Gaussian basin. Neurons with nearconstant
features can reverse their readout sign and correct the residual; omitting
a small but fixed Gaussian population is invalid at large width and infinite
training time.

[GAUSSIAN_NEGATIVE_MASS.md](GAUSSIAN_NEGATIVE_MASS.md) records these exact
calculations and the missing pathwise probability estimate. It contains no
claimed nonvanishing-probability failure theorem.

The justified conclusion is therefore narrower than a complete boundary:

- Small labels are **not necessary** for canonical Gaussian fitting in the
  nonlinear subclass of Section 2.
- They are also **not necessary** for the audited tanh/tanh class of Section 3,
  including mixed signs and an open neighborhood of both input geometries
  and label vectors. Its nonorthogonal and tiny-readout extensions passed
  separate internal checks.
- Their necessity for the two-tanh-layer Gaussian setting is **not proved**.
- Arbitrary-label high-probability fitting for that full tanh setting is
  also **not proved**.
- Earlier engineered bad basins do not establish a large-label Gaussian
  transition; some of those basins already exist at small label scales.
- Non-fitting, even if proved, would not by itself prove incompressibility
  of the resulting trajectory.

These are internal research results, not promoted book material. No numerical
experiment, modification of the integrated compression theorem, or Git commit
was performed for this continuation.
