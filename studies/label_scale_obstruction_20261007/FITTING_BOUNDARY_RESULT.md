# Fitting and non-fitting coexist for the same inputs and labels

2026-10-10. Current synthesis of the two-sided theoretical search in this
study. These are internally checked research results, not promoted book
theorems. The original high-probability, sufficiently-large-width
arbitrary-label fitting problem remains open.

## 1. Headline and exact quantifiers

There is no deterministic input-and-label-only boundary separating fitting
from stable non-fitting in the present model: the same fixed inputs and
labels can support open initialization basins of both kinds. This statement
does not rule out a high-probability boundary under a specified random
initialization law.

Throughout, use the bias-free, fully trained, two-hidden-layer tanh network.
The matrix \(X\in\mathbb R^{d\times m}\) has unit input columns; for the
radius-\(\sqrt d\) convention these columns are the original inputs divided
by \(\sqrt d\). At width \(n\ge m\), define

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad
\mathcal L=\|r\|_2^2/m,
\]

where \(A\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). The flow is

\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L,\qquad w(0)=0.
\tag{1}
\]

No layer is frozen and no learning rate is changed. All inputs and labels
are fixed independently of width. An open initialization set below is open
in \((A(0),W(0))\), on the exact slice \(w(0)=0\).

### Positive theorem: every admissible dataset and every bounded label set

For every finite set of distinct, nonantipodal sphere inputs, every
\(n\ge m\), and every finite label radius, there is a nonempty open set
of hidden initializations such that **every label vector in that radius**
is fitted exponentially:

\[
\mathcal L(t)\le\mathcal L(0)e^{-ct},\qquad c>0.
\tag{2}
\]

The same initialization set works for the whole specified label ball,
including arbitrary mixed signs. It may depend on the radius, dataset,
and width. All parameters converge to finite interpolating limits. This
is a proved initialization condition, not an assumption that a feature
gap persists along an unknown future trajectory.

### Negative theorem: generic inputs, all amplitudes, arbitrarily little learning

Let \(d\ge2\) and \(m\ge d^2+3d+4\). There is an open dense class of
distinct nonantipodal sphere datasets with the following property. For
each such dataset and each \(0<\eta<1\), one can fix a mixed-sign vector
\(y^\circ\) with \(\|y^\circ\|_\infty=1\) such that, for **every**
\(a>0\), labels \(y=a y^\circ\) admit a nonempty open bad initialization
basin at every width \(n\ge m\). Throughout that basin,

\[
0<(1-\eta)\mathcal L(0)<\mathcal L(\infty)<\mathcal L(0).
\tag{3}
\]

Both initial feature matrices have full column rank; both converge to
rank-one matrices. Parameters converge finitely to a stable positive-loss
critical manifold. Thus learning starts strictly, and then stops without
fitting. The architecture can interpolate these same labels elsewhere.

The direction \(y^\circ\) and the retained loss fraction are independent
of width and amplitude. The open basin itself may depend on \(a,n\).
Taking \(a=1\) gives genuinely fixed order-one maximum label magnitude;
taking any other fixed \(a\) requires no new restriction. Increasing
\(M\) in the construction below makes the retained fraction arbitrarily
close to one.

The sample threshold is sufficient, not necessary. On the circle the
generic all-amplitude theorem applies for \(m\ge14\). Genericity is also
relative to any nonempty open input region: in particular the theorem
includes open classes with all pairwise input correlations positive.
It does not require paired, orthogonal, or exactly symmetric data.

### Coexistence and probability

Apply the positive theorem to the very dataset and labels in the negative
theorem. For each fixed width there are therefore two nonempty open
initialization sets: one fits exponentially, the other has (3). This is
the promised coexistence result. Each set can be required to have both
initial feature matrices of full column rank.

Under the canonical independent law
\(A_{jk}(0)\sim N(0,1)\), \(W_{ij}(0)\sim N(0,1/n)\), both sets have
strictly positive probability at each fixed width. Neither probability
has been bounded below uniformly in width. In particular this theorem
does not refute success probability tending to one as \(n\to\infty\).

## 2. Positive mechanism and its precise qualifications

The complete derivation is in
[POSITIVE_ARBITRARY_LABELS.md](POSITIVE_ARBITRARY_LABELS.md), checked in
[POSITIVE_ARBITRARY_LABELS_CHECK.md](POSITIVE_ARBITRARY_LABELS_CHECK.md).
Its symbol \(Y\) denotes the Euclidean label radius, not the RMS label
size used in the compression study. The following restatement avoids that
collision and shows all initialization conditions explicitly.

Locally in this section, let \(B\) be the prescribed Euclidean label
radius. At initialization put
\(S=\operatorname{sign}(W(0)U(0))\) and
\(\lambda=\lambda_{\min}(S^\top S/n)>0\). Suppose all entries of
\(W(0)U(0)\) have absolute value at least \(R>0\), and

\[
\begin{aligned}
2\sqrt m\,e^{-R}&\le\frac{\sqrt\lambda}{2},\\
\frac{16m\operatorname{sech}^2(R/2) B^2}{\lambda^2}&<1,\\
\frac{16\sqrt{nm}\operatorname{sech}^2(R/2)B^2}{\lambda^2}
\left[m+(\|W(0)\|_{\rm op}+1)^2\|X\|_{\rm op}^2\right]&<R/2.
\end{aligned}
\tag{4}
\]

Then (2) holds for all \(\|y\|_2\le B\), with \(c=\lambda/m\).
The bootstrap proves that the top preactivations retain magnitude at
least \(R/2\). Their derivatives are at most
\(\operatorname{sech}^2(R/2)\), and
\(H^\top H/n\succeq(\lambda/4)I_m\). Integration of the residual's
exponential bound controls the total motion of every parameter block;
the last two inequalities in (4) close the bootstrap.

These conditions are nonempty for every stated dataset. Tanh ridge
features span all sample vectors for distinct nonantipodal inputs, so
choose a full-column-rank first feature matrix \(U_*\). Choose a
full-column-rank sign matrix \(S\), and set
\(W_*=2RS(U_*^\top U_*)^{-1}U_*^\top\). Its top preactivations are
\(2RS\). Its norm grows linearly in \(R\), while
\(\operatorname{sech}^2(R/2)\le4e^{-R}\). Hence a sufficiently large
finite \(R\) makes (4) strict for any fixed \(B\). Continuity gives
the open initialization event.

This proves arbitrary-label fitting through saturation-stabilized
features. It does not prove that typical Gaussian features enter this
regime, nor does it establish substantial feature learning on the good
basin. The required saturation can grow with the label radius and width.

## 3. Negative mechanism: generic moments and capture at every amplitude

The full generic construction is in
[NEGATIVE_LABEL_BOUNDARY.md](NEGATIVE_LABEL_BOUNDARY.md). The explicit
scale-independent capture bounds are in
[TANH_LARGE_RESIDUAL_CAPTURE.md](TANH_LARGE_RESIDUAL_CAPTURE.md).

Here is the proof architecture, with the central equalities exposed.
Consider the single profile

\[
h(p,q)_a=\tanh(q\tanh(p^\top X_a)).
\]

Fix a nonzero \(p\) along a coordinate axis and \(q>0\). A linear
moment system in a residual vector \(r_0\) prescribes

\[
r_0^\top h=0,\qquad Dh^\top r_0=0,\qquad
\nabla^2_{(p,q)}(r_0^\top h)=I_{d+1}.
\tag{5}
\]

It also makes the two neuron-splitting quadratic forms strictly positive.
The moment system involves \(d^2+3d+3\) independent analytic functions
on the sphere. Independence follows by decomposing into transverse
constant, linear, and trace-free quadratic parts and separating powers
of \(t\) from functions analytic in \(e^{-2t}\). Thus its evaluation
matrix is onto for an open dense class of datasets with at least that
many samples. Adding the constant function is independent by parity,
and supplies the extra moment \(\sum_a r_{0,a}=0\). Since \(r_0\ne0\),
it then has both signs. This is the origin of the sufficient threshold
\(m\ge d^2+3d+4\), not an assumption of generic labels.

Let \(h_*\) denote the profile at this fixed hidden parameter pair.
For one sufficiently large finite \(M\), choose the label direction
\(h_*-M r_0\). It is mixed-sign because \(r_0\) is mixed-sign. For a
positive physical amplitude \(s\), write the readout as \(s b\) and
use labels \(s(h_*-M r_0)\). The reduced loss divided by \(s^2\) is

\[
\frac1m\|b h(p,q)-h_*+M r_0\|_2^2.
\tag{6}
\]

Its hidden mobility is \(s^2\) and its \(b\)-mobility is one: this is
the original flow after changing coordinates, not a changed optimizer.
The function \(r_0^\top h\) has a strict local minimum zero by (5).
For all \(s>0\), the reduced trajectory from the fixed hidden profile
and \(b=0\) remains within a hidden ball of radius \(K/M\) and
\(0\le b\le2\), where \(K\) is independent of \(s,M\). At the
hidden boundary the restoring term \(M\nabla(r_0^\top h)\) dominates
the other hidden force. Changing \(s\) multiplies this velocity by a
positive factor and does not change its inward direction.

The readout reaches \(b=1/2\) in bounded time independent of \(s\).
Thereafter the full hidden/readout Hessian of (6) is positive definite:
its hidden block is order \(M\), its mixed block is bounded, and its
readout block stays bounded below. A Schur-complement estimate proves
strong convexity and convergence to \((p,q,b)=(p_*,q_*,1)\).
The convergence rate may depend on \(s\), but the sufficient \(M\)
does not. All numerical sufficient constants are given in the capture
note, equation (8).

Replicate this profile by taking every first-layer row equal to \(p^\top\),
every middle weight equal to \(q/n\), and every readout equal to \(sb\).
This is an exact invariant subsystem of (1), at every width. The strict
splitting forms make its bad limit transversely attracting in the full
network, with only the tangent directions of an affine critical manifold
in the Hessian kernel. Finite-time entrance into that attracting
neighborhood, and continuous dependence on the initial hidden parameters,
give an open basin on \(w(0)=0\). This is why the construction is not
merely an exceptional symmetric trajectory.

Full-rank first and top feature matrices form an open dense subset of
hidden parameter space for these inputs. Intersecting this set with the
bad basin gives full-rank starts, while the common endpoint prediction
is \(s h_*\). Both endpoint feature matrices have rank one.

Since \(r_0^\top h_*=0\), every zero-readout trajectory in this basin has

\[
\frac{\mathcal L(\infty)}{\mathcal L(0)}
=\frac{M^2\|r_0\|_2^2}
       {\|h_*\|_2^2+M^2\|r_0\|_2^2}.
\tag{7}
\]

This fraction is independent of amplitude and width, strictly below one,
and tends to one as \(M\to\infty\). Choose \(M\) also to make it
greater than \(1-\eta\), then normalize
\(y^\circ=(h_*-M r_0)/\|h_*-M r_0\|_\infty\). Applying the capture
lemma with \(s=a/\|h_*-M r_0\|_\infty\) proves (3) for every
\(a>0\). This normalization is not a width-dependent small-label
restriction. The amplitude is arbitrary and fixed independently of width.

## 4. What boundary has and has not been identified

The exact residual evolution provides a useful diagnostic, but not a
substitute for a data-dependent theorem. Assume here that
\(\mathcal L(0)>0\); the zero-initial-loss case is stationary. A
nonstationary trajectory cannot first reach zero loss at a finite time:
the zero-loss state is an equilibrium, and local uniqueness backwards
from that finite state would force the preceding trajectory to be
constant. If \(J_f\) is the Jacobian of
the prediction vector with respect to all parameters and \(D\) is the
constant block mobility matrix from (1), set
\(\mathcal K=J_f D J_f^\top\). While \(r\ne0\), define locally
\(c(t)=r^\top\mathcal K r/\|r\|_2^2\). Direct differentiation gives

\[
\mathcal L(t)=\mathcal L(0)
\exp\!\left[-\frac4m\int_0^t c(s)\,ds\right].
\tag{8}
\]

Thus zero limiting loss is equivalent to divergence of this integral;
positive limiting loss is equivalent to its finiteness. An exponential
upper bound \(\mathcal L(t)\le C\mathcal L(0)e^{-\alpha t}\) is
equivalent to
\(\int_0^t c(s)ds\ge(m\alpha/4)t-(m/4)\log C\).
These are exact trajectory criteria. They do not classify inputs and
labels before solving the dynamics.

The positive theorem proves a uniform lower bound for \(c(t)\) from
initial conditions. The negative theorem proves that its integral is
finite along open bad basins, even though it is positive initially.
The initial residual is not merely placed in a permanently inactive
direction: full initial feature rank makes the initial loss derivative
strictly negative, and feature collapse occurs later.

Existing complementary results in
[TANH_CLASSIFICATION_RESULT.md](TANH_CLASSIFICATION_RESULT.md) remain
important. If \(X\) has full column rank and \(n\ge m\), every finite
local minimum fits; positive-loss stationary points can nevertheless
be saddles or higher-order degenerate points. That fact alone proves
neither boundedness nor avoidance of their stable sets on the zero-readout
slice. The study also has explicit positive-loss trajectories escaping
to infinite parameter norm, but no open or typical Gaussian escape basin.
The new generic finite-minimum construction does not cover every input
configuration or the intermediate sample-count regimes.

In particular, the present results do **not** prove any of the following:

- that large labels, rather than initialization, create a new sharp failure
  threshold; bad basins above exist at arbitrarily small amplitudes too;
- that a small-label restriction is necessary for high-probability fitting;
- that every fixed dataset admits a stable bad basin after choosing labels;
- that arbitrary fixed labels fit with high probability at large width;
- that non-fitting trajectories are incompressible;
- a broad multi-input theorem distinguishing exponential fitting from
  slower, nonexponential fitting under typical Gaussian initialization.

The strongest newly proved boundary is instead **coexistence of stable
outcomes for the same fixed data and labels**. Any complete probabilistic
classification must additionally control the measures of these basins
as width grows, or prove a trajectory property for the Gaussian bulk.

## 5. Search record and verification boundary

Three scoped routes were run: arbitrary-label positive fitting, correlated
input geometry, and generic negative moment construction. Independent first
rounds were compared before sharing mature lemmas. The generic moment route
and the lead's large-residual capture idea combined to remove the previous
capture amplitude restriction. Internal cross-checks reconstructed the
positive bootstrap, moment independence, capture tube, and replication
normalization. These reused-context checks are not isolated promotion reviews.

The geometry route also ruled out one simple extension of the orthogonal
tanh balance law: the proposed conserved potential has a nonzero curl for
non-diagonal input Gram matrices. That obstruction applies to that proposed
proof mechanism, not to fitting itself. Details and the applicability audit
of maintained-book comparisons are in
[POSITIVE_GEOMETRY_ROUTE.md](POSITIVE_GEOMETRY_ROUTE.md).

No experiment, shared-book modification, change to the integrated
compression theorem, staging, or Git commit was performed in this search.
