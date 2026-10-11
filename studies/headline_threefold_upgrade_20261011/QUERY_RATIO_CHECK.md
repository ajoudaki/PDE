# Check of querywise zeros and the test-only endpoint example

2026-10-11. Bounded internal mathematical check, not a promotion review.
Inputs: `QUERY_RATIO_SCOPE.md`, Section 2 of `UNIFORM_TIME_SCOPE.md`, and
the current compact setup/fitting statements. Other proposed upgrades and
the endpoint theorem referenced in Section 3 were not audited here. The
rigorous-math and canonical-notation instructions were applied. No proof or
paper was edited.

**Finding:** both assigned counterexamples are valid under the stated
zero-denominator-as-failure convention. The tanh example produces a zero
somewhere on one fixed separated semicircle at every positive time. The
cosine example gives zero endpoint discrepancy on a fixed test-only panel.
Their distinct conclusions are correctly separated in the proof note.

## 1. Division inside versus outside the spatial supremum

For nonnegative errors \(E(t,x)\) and dense differences \(D(t,x)\), if
\(D(t,x)>0\) and \(E(t,x)/D(t,x)\le a\) for every query, then
\[
\sup_x E(t,x)\le a\sup_xD(t,x).
\]
Hence the pointwise-quotient target implies the ratio of separate spatial
suprema whenever its quotients are defined. The converse does not follow:
a spatial zero of \(D\) can coexist with a positive spatial maximum.
Under the stated failure convention, a single zero denominator at a query
and time is sufficient to invalidate the pointwise-quotient target, regardless
of the numerator at that point.

The argument must keep the order of quantifiers: the tanh construction shows
\(\forall t\,\exists x\), with the query permitted to depend on time
and the two network realizations. This is sufficient for a supremum over
queries at every time. It does not supply a fixed query with zero discrepancy
at every time, or a zero lying in an arbitrary fixed finite passive panel.

## 2. The tanh architecture and its training assumptions

Take \(d=3,m=2\), unit training directions \(v_1=e_1,v_2=e_2\),
physical inputs \(x_a=\sqrt3v_a\), and tanh at every hidden layer.
There are no biases. Each linear map is odd and tanh is odd, so induction
through the layers gives
\[
h^{(j)}(-v)=-h^{(j)}(v),\qquad f_n(t,-x)=-f_n(t,x)
\]
for every parameter realization at every time where the flow is defined.
This identity does not depend on the labels or on any symmetry of the
learned weights. Both independent dense runs satisfy it.

Tanh satisfies the activation assumptions. For any fixed
\(0<a<\pi/2\), it is holomorphic on \(|\operatorname{Im}z|<a\), and
\[
|\cosh(x+iy)|^2=\sinh^2x+\cos^2y\ge\cos^2a
\]
gives \(|\tanh'(x+iy)|\le\sec^2a\) on that strip. It is real
on the real axis and nonaffine. Its second derivative is bounded on the
required smaller strip, so its prescribed envelope \(\beta\) is finite.

The population training covariance starts at \(Q^{(0)}=I_2\). If
\(Q^{(j-1)}=q_{j-1}I_2\), its centered Gaussian coordinates are
independent. Oddness gives zero mean for each activated coordinate, so the
next off-diagonal moment is zero, while
\[
q_j=\mathbb E\tanh(\sqrt{q_{j-1}}G)^2,\qquad G\sim N(0,1).
\]
Starting from \(q_0=1\), every \(q_j\) lies strictly between zero and
one. Thus \(\gamma=q_L>0\), and \(m/\gamma\ge1\). The chosen
labels \(y=(\varepsilon,-\varepsilon)\) have RMS \(Y=\varepsilon\).
The inequality
\(0<\varepsilon\le(\gamma/2)\beta^{-30L}\) is exactly the current
small-label condition because \(m=2\). The training inputs are distinct,
nonparallel and nonantipodal. No assumption in the compression setup excludes
their proper two-dimensional span inside \(\mathbb R^3\).

The current fitting lemma therefore supplies a global parameter-convergent
flow with probability tending to one for each dense run. Their joint fitting
event also has probability tending to one by a union bound.

## 3. A zero on the separated semicircle at every time

Let
\[
v(\theta)=\cos\theta\,e_3+
\sin\theta\,(e_1+e_2)/\sqrt2,\qquad 0\le\theta\le\pi.
\]
The two displayed spanning vectors are orthonormal, so every query is a unit
vector. For \(a=1,2\),
\[
\|v(\theta)\mp e_a\|_2^2
=2\mp\sqrt2\sin\theta\ge2-\sqrt2>0.
\]
Thus the full fixed semicircle is separated from both signs of every training
direction. Equivalently its angular distance from each signed training
direction is at least \(\pi/4\). Physical Euclidean distances acquire
the common factor \(\sqrt3\).

For any fixed time at which both flows exist, define the continuous scalar
function
\[
g_t(\theta)=f_n(t,\sqrt3v(\theta))
            -\widetilde f_n(t,\sqrt3v(\theta)).
\]
Its endpoint queries are \(e_3\) and \(-e_3\). Oddness gives
\(g_t(\pi)=-g_t(0)\). If \(g_t(0)=0\), an endpoint is a zero.
Otherwise the endpoints have opposite signs, and the intermediate value
theorem gives an interior zero. This proves
\[
\text{for every }t>0,\quad
\text{there exists }\theta\in[0,\pi]
\text{ with }D_n(t,\sqrt3v(\theta))=0.
\]
No probabilistic union over times is needed: the deterministic symmetry
and continuity hold for all parameter states, so on the joint global-flow
event the argument applies to every time. At the fitted endpoint, parameter
convergence supplies a continuous limiting network with the same oddness;
alternatively the fitting lemma's uniform sphere convergence preserves both
continuity and oddness.

This excludes the pointwise spatial quotient under the failure convention
on any promised query domain containing the semicircle, including the whole
sphere or the indicated separated test domain. It does not exclude a ratio
of separate spatial suprema, since this argument does not make the dense
difference vanish on every query. The note makes this distinction correctly.

## 4. The cosine test-only endpoint panel

For the second example, take \(d=m=2\), training directions \(e_1,e_2\),
and cosine in every layer. The test-only directions \(-e_1,-e_2\) are
distinct from both training directions. Cosine is entire and nonaffine;
its first and second derivatives are bounded on every fixed horizontal
strip. Thus the current activation hypotheses hold.

For a centered Gaussian pair with common variance \(q\) and covariance
\(c\), the cosine product identity gives the recurrence stated in
`UNIFORM_TIME_SCOPE.md`:
\[
q_j=e^{-q_{j-1}}\cosh(q_{j-1}),\qquad
c_j=e^{-q_{j-1}}\cosh(c_{j-1}),\quad(q_0,c_0)=(1,0).
\]
Strict increase of cosh on nonnegative arguments proves inductively
\(0<c_j<q_j\) for every positive layer. Hence the final Gram gap is
\(\gamma=q_L-c_L>0\). Also \(q_j\le1\), so \(m/\gamma\ge1\).
The supplied choice
\[
y=(\varepsilon,2\varepsilon),\qquad
0<\varepsilon\le(\gamma/2)\beta^{-30L}\sqrt{2/5}
\]
has RMS \(Y=\varepsilon\sqrt{5/2}\) and satisfies the original cap.
The two training directions are not identified by input-sign symmetry, so
different labels on them cause no incompatibility.

First-layer evenness gives \(h^{(1)}(-v)=h^{(1)}(v)\) at every parameter
state. All later features and outputs therefore agree at \(v\) and
\(-v\), regardless of training dynamics. On the joint dense fitting event,
both runs consequently have endpoint predictions \(y_1,y_2\) at the
test-only inputs \(-x_1,-x_2\). Thus
\[
\sup_{x\in\{-x_1,-x_2\}}
|f_n(\infty,x)-\widetilde f_n(\infty,x)|=0.
\]
This refutes the separate-spatial-suprema target on that panel under the
endpoint failure convention. It does not refute a version requiring test
queries to be separated from both signs of every training input, which
would exclude this panel. Removing time zero leaves this endpoint intact.

## 5. Small corrections and the check boundary

Coordinator follow-up: the argument-separator typo identified below has been
corrected in `QUERY_RATIO_SCOPE.md`; its two arrows are explicitly specified
there to mean convergence in probability. Neither change alters the checked
arguments. The comments below record the version inspected by the reviewer.

Equation (4) of `QUERY_RATIO_SCOPE.md` currently writes
`D_n(t,\sqrt3,v(\theta))`, with an extra argument separator. Its intended
and mathematically verified expression is
`D_n(t,\sqrt3\,v(\theta))`.

If equations (1)--(2) are intended as the paper's probabilistic targets,
writing \(\xrightarrow{\mathbb P}0\) would make their probability mode
explicit. The counterexamples above have failure probability tending to one,
so this notational clarification does not affect them.

The extension of an endpoint oracle theorem to a nonorthogonal query outside
the training span, asserted in Section 3, was not assigned for verification
and is not certified by this check. The last observation there is sound
independently: an endpoint lower bound alone says nothing about a possible
zero or small minimum at an earlier positive time.
