# Test-only domains and the placement of division

2026-10-11. Continuation after the user restricted Taylor's comparison to
test inputs distinct from training inputs. This removes the earlier
training-only-panel objection for the revised target. It does not establish
positive dense discrepancy on the revised domain.

The user wrote dense/dense discrepancy divided by compact/dense error and
asked for convergence to zero. The direction consistent with the compression
goal is the reciprocal. Define, for this note only,

\[
E_n(t,x)=|f_{\rm model}(t,x)-f_n(t,x)|,\qquad
D_n(t,x)=|f_n(t,x)-\widetilde f_n(t,x)|.
\]

Two different strengthened targets are

\[
\sup_{t\in(0,\infty]}
 \frac{\sup_{x\in\mathcal X}E_n(t,x)}
      {\sup_{x\in\mathcal X}D_n(t,x)}\longrightarrow0,
                                                               \tag{1}
\]

and

\[
\sup_{t\in(0,\infty],\ x\in\mathcal X}
 E_n(t,x)/D_n(t,x)\longrightarrow0.                            \tag{2}
\]

Equation (2) implies (1) wherever the quotients are defined, but not
conversely. A moving zero in the dense difference matters for (2) even when
the spatial supremum in (1) is positive. The user has been asked to confirm
the placement. Pending that answer, (1) remains the working research target.
Both arrows mean convergence in probability as width tends to infinity,
with the problem parameters fixed separately.

## 1. Positive time and spatial separation do not remove pointwise zeros

Here is an exact counterexample to the assertion that a dense discrepancy
cannot vanish away from training inputs at positive time. It uses actual
finite-width networks, not a kernel surrogate or a limiting model.

Take \(d=3,m=2\), any fixed hidden depth \(L\ge2\), training directions
\(v_1=e_1,v_2=e_2\), and \(\phi_j=\tanh\) at every layer. There
are no biases. Every parameter realization satisfies

\[
f_n(t,-x)=-f_n(t,x)
\]

at every time at which it is defined, since each hidden activation is odd
and every intervening map and readout is linear. The independently initialized
dense run has the same identity. Their difference is therefore a continuous
odd function of the input sphere.

Consider the fixed semicircle of unit query directions

\[
v(\theta)=\cos\theta\,e_3+
            \sin\theta\,(e_1+e_2)/\sqrt2,
\qquad 0\le\theta\le\pi.
\]

For each \(a=1,2\) and either sign,

\[
\|v(\theta)\mp v_a\|_2^2
 =2\mp\sqrt2\sin\theta\ge2-\sqrt2.                          \tag{3}
\]

Thus this whole semicircle is uniformly separated from both signs of every
training input. Its endpoints are antipodal. At any fixed positive time,
the dense differences at these endpoints are negatives of one another. If
either is zero, a separated zero is already present. Otherwise the
intermediate value theorem gives a zero in the interior of the semicircle.
Consequently

\[
\text{for every }t>0,\quad
\exists\theta\in[0,\pi]:
D_n(t,\sqrt3\,v(\theta))=0.                                  \tag{4}
\]

The same applies to the fitted limit when it exists. The query achieving
(4) may depend on the two realized networks and time; that is allowed by
the pointwise spatial supremum (2). No test label is used.

All theorem assumptions can be met. Tanh is nonaffine, analytic on a
sufficiently small strip with bounded derivative there. Its values are
bounded, which is allowed. The initialized population training Gram at every
layer is \(q_j I_2\), where
\(q_0=1\) and \(q_j=\mathbb E\tanh(\sqrt{q_{j-1}}G)^2>0\).
The two preactivations are independent centered Gaussians at each covariance
recursion, so oddness makes their cross moment zero. Hence \(\gamma=q_L>0\).
Choose fixed labels \(y=(\varepsilon,-\varepsilon)\) with
\(0<\varepsilon\le(\gamma/2)\beta^{-30L}\). This satisfies the
original small-label cap and is compatible with the architecture. The
training inputs are neither parallel nor antiparallel. The paper's fitting
event has probability tending to one, and (4) is an exact deterministic
identity on it.

Under the current convention that a zero denominator counts as failure,
(2) cannot hold even for this ordinary activation, even with strict
test/training angular separation, and even when time zero is excluded.
No claim that the numerator at the zero is positive is needed or made.
If zero/zero is instead assigned a special value, that is a different
statement; this argument alone does not disprove that revised convention.

This pointwise-zero argument does **not** disprove (1): a function can vanish
at one separated input while having a positive supremum over the query set.

## 2. Test-only finite panels still need an endpoint qualification

For (1), restrict to a declared finite panel as in Taylor. Mere distinctness
from training inputs is insufficient. Use \(d=m=2\), training directions
\(e_1,e_2\), cosine in every layer, and the test-only panel
\(\{-e_1,-e_2\}\). These test inputs are distinct from both training
inputs, and the training inputs span the whole input space.

First-layer evenness implies \(f_n(t,-x)=f_n(t,x)\) for all weights and
all times. At the fitted limit, both independent dense runs therefore equal
the prescribed training labels on this test-only panel. Its spatial
supremum discrepancy is exactly zero. The positive population Gram and
small-label verification are fully given in `UNIFORM_TIME_SCOPE.md`, Section
2: its diagonal/off-diagonal recursion preserves \(0<c_j<q_j\), so
the gap is strictly positive. No bad or incompatible training labels are
being imposed on two equivalent training inputs.

This is a zero-denominator obstruction at the fitted endpoint. Removing
\(t=0\) does not remove \(t=\infty\). It uses antipodal test points,
so it does not settle a stronger requirement that all tests be separated
from both signs of training inputs. Under that stronger geometry, the
whole-sphere pointwise obstruction in Section 1 still applies to (2), but
not to the separate-suprema finite-panel statement (1).

## 3. Geometry and time are separate proof obligations

The endpoint oracle route does extend from an orthogonal query to any fixed
query outside the training span; the new proof is in
`TEST_PANEL_DENSE_ROUTE.md`. Distinctness alone does not ensure that its
perpendicular component is nonzero. If the training span is all of
\(\mathbb R^d\), every query lacks that component, and the oracle proof
does not apply. This is a boundary of that argument, not a proof that all
full-span endpoint lower bounds are false.

Even an endpoint lower bound on a genuinely new test input does not establish
a lower bound at every earlier time. Fixed-time estimates must be made
simultaneous, or a noncrossing/quantitative minimum argument must be supplied.
Neither nonaffinity nor fitting at the training inputs proves such an
argument by itself.

Thus the proposed clarifications remove one old query-domain objection, but
they do not complete the same-time theorem. The distinctions above are exact
mathematical issues, not choices of constants or storage bookkeeping.
