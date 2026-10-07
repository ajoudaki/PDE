# Uniform Gaussian response errors for training and unseen query sources

2026-10-06. A partial theorem for the existing deep nonlinear model. This
does not yet construct the compact decoder.

The scalar response estimate in `ROOT_RESPONSE_AND_COVARIANCE.md` can be
made simultaneous over the whole query sphere and a logarithmic training
horizon. No spatial coefficient table is retained: analytic patches are
used only to prove a supremum bound. The missing compact evaluation of the
response traces remains a separate issue.

## 1. Model, sources and statement

Keep the original fixed depth L>=2, training count m, dimension d, sphere
inputs, Gaussian initialization, zero readout, mean squared loss and
mobilities (n,1,...,1,n). Keep the full original intersection of the
source, dense-fitting and compact-fitting label allowances and the
positive initial training feature-Gram gap gamma. Activations may have
unbounded values and have bounded first derivatives on their analytic
strips. The query v=x/sqrt(d) lies on the unit sphere and is not used
for training.

Write Y=||y||_2/sqrt(m)>0 and set

\[
 T=32(m/\gamma)\log(en).
\]

Let G be the complete standard Gaussian initialization root, and let M
be any one standard-Gaussian hidden-matrix block, so its physical mixer
is M/sqrt(n). Choose c(s) to be one training feature, training backward
response or readout vector. Initialized-matrix images of these vectors
are also allowed. Let h(t,v) be one forward feature vector at the query,
or its initialized forward-matrix image. All these vectors have n entries.
The choices range over a fixed finite list of layers and training samples.
Passive-query backward vectors are not included.

Define the total-response defect

\[
 E_n(s,t,v)=\frac1{n^{3/2}}\sum_{i,j}
       \left[M_{ij}c_i(s)h_j(t,v)
                    -\partial_{M_{ij}}\{c_i(s)h_j(t,v)\}\right].
 \tag{1}
\]

All derivatives include the dependence of the actual trained parameters
on the initialization. There are constants C depending only on the fixed
problem such that, for every fixed 0<delta<1 and sufficiently large
individual n,

\[
 \sup_{0\le s,t\le T}\sup_{\|v\|_2=1}|E_n(s,t,v)|
 \le \frac{C}{\sqrt{n\delta}}
          e^{C\sqrt{\log(en)}}[\log(en)]^{2+d/4}
 \tag{2}
\]

with probability at least 1-delta-o(1). The o(1) is exactly the inherited
good-event failure, not a new quantitative source theorem. Equivalently,
replacing delta by delta/2 gives success probability at least 1-delta
at every sufficiently large width. The stochastic width threshold remains
unquantified, and the inherited explicit construction gates remain in force.
The bound can cover the fixed finite list of source choices by enlarging C.

The logarithmic power displayed in (2) is a proof-bound cost, not a retained
storage bound. It is not optimized. This theorem neither approximates the
derivative trace by a compact algorithm nor asserts smooth dependence of
fitted-limit derivative traces at infinite time.

## 2. Precisely what is inherited

Intersect the dense good-pair event with the analytic source event in the
authorized integrated proofs. Their probabilities tend to one under the
unchanged label conditions. On this intersection:

- Actual real parameter paths have the all-time physical bounds and the
  good-pair estimate (9) of `GENERAL_DENSE_COMPARISON.md`.
- `UNBOUNDED_COMPRESSOR_BRIDGE.md`, Sections 6--8, gives a complex
  rectangle around [0,T] with margins r_t=c_t/sqrt(log(en)), and the
  complex sphere tube of radius r_x=c_x/sqrt(log(en)). The positive
  coefficients c_t,c_x depend on the fixed problem only.
- All relevant preactivation imaginary parts on this product domain are
  at most one quarter of the activation strip width. Hidden operator
  norms and all feature/backward RMS norms are bounded by fixed constants.
  Training carrier coordinates, including the readout, are bounded by
  C sqrt(log(en)) on the complex time rectangle, by that source's (23).
  This is a complex-domain bound, not an inference from its real restriction.
- The complex training residual norm divided by sqrt(m) is at most 2Y
  along the short paths from a nearest real anchor, by source (31).

These source statements already have a common holomorphic neighborhood
of their closed domains. Shrinking either radius by a fixed factor is
allowed and does not change the probability event or the logarithmic scale.
All references here are to the integrated study explicitly authorized by
the user; their linked earlier studies are not separately imported.

## 3. Complex good-pair control from the real comparison

Use the parameter difference norm

\[
 D=\frac{\|\Delta A\|_F}{\sqrt n}
          +\sum_{\ell=2}^L\|\Delta W^{(\ell)}\|_F
          +\frac{\|\Delta w\|_2}{\sqrt n},
 \tag{3}
\]

with complex Euclidean norms when needed. For two good initialization
roots G,G', the real comparison implies, uniformly at real anchors,

\[
 D\le\frac{C}{\sqrt n}e^{C\sqrt{\log(en)}}\|G-G'\|_2.
 \tag{4}
\]

We extend (4) to the small complex neighborhoods without assuming that a
straight segment between the two parameter states is itself a good path.
The two actual complex paths separately satisfy the source bounds.

Forward subtraction at a training input gives feature and preactivation
RMS differences at most CD. To justify activation subtraction, the straight
segment between the two scalar preactivations stays in the convex safe
strip, so its derivative bound applies. Backward subtraction has one
changed-gate term, whose reference carrier is bounded coordinatewise by
C sqrt(log(en)). The changed matrix and propagated upper response use
their RMS and operator bounds. Downward induction therefore gives

\[
 \frac{\|\Delta\delta^{(\ell)}\|_2}{\sqrt n}
     \le C(1+\sqrt{\log(en)})D.
 \tag{5}
\]

There is a sum of changed-gate contributions, not a new logarithmic factor
at every layer. The prediction and normalized residual differences are
at most CD. Subtracting the actual rank-one gradient-flow equations,
using the residual bound 2Y and
||ab^T/n||_F=(||a||/sqrt(n))(||b||/sqrt(n)), gives

\[
 \|F(\theta)-F(\widetilde\theta)\|_{\rm par}
       \le C(1+\sqrt{\log(en)})D
 \tag{6}
\]

for these two states, where F is the actual complexified vector field.
The first and readout blocks use the normalizations in (3).

Follow both paths from the same nearest real anchor to the same complex
time, on one or two segments of total length at most 2r_t. The integral
form of (6) and Gronwall multiply (4) by at most
exp(2Cr_t(1+sqrt(log(en)))), which is bounded by a fixed constant.
Thus (4) holds throughout the required complex time domain as well.

For a complex query in the source tube, both preactivation sequences still
lie in the safe strip and its input norm is at most two. Forward subtraction
therefore gives

\[
 \|h(t,v;G)-h(t,v;G')\|_2
       \le Ce^{C\sqrt{\log(en)}}\|G-G'\|_2.
 \tag{7}
\]

For c(s), equations (4)--(5) give the same bound with an additional factor
1+sqrt(log(en)). In both cases the vector amplitude is at most C sqrt(n).
Initialized matrix images obey these bounds too: subtract the two products;
the initialized operator norm is bounded and
||Delta W_0||_F<=||G-G'||/sqrt(n). No passive-query backward maximum
is needed. This proves actual good-pair premises on the complex domain,
not merely a pointwise derivative estimate on a possibly nonconvex event.

## 4. Analytic charts and coefficientwise localization

At a real sphere point u choose an orthonormal basis V of its tangent
space. For a complex (d-1)-vector z define

\[
             v_u(z)=\frac{u+Vz}{\sqrt{1+z^Tz}},
 \tag{8}
\]

using the branch of the square root equal to one at zero. For sufficiently
small ||z||_2, this is holomorphic, v_u(z)^Tv_u(z)=1, and the norm
of its derivative is bounded by an absolute constant. In a polydisk of
radius c r_x/sqrt(d), with a sufficiently small numerical c, its input
norm is at most two and ||Im v_u(z)||_2<=sinh(r_x). To see the latter,
subtract v_u(Re z), integrate the bounded derivative along the imaginary
segment, and use ||Im z||_2<=sqrt(d-1) max_j|Im z_j|.

An ambient Euclidean sphere net of mesh a fixed fraction of this radius
has at most C_d r_x^(-d) points, by disjoint-ball volume comparison.
Their smaller real chart neighborhoods cover the sphere: the inverse
coordinate at a nearby real v is V^Tv/(u^Tv), whose denominator is
bounded below. For d=1 simply use the two points. Two temporal grids
cover [0,T]^2 with at most C(1+T/r_t)^2 smaller time polydisks. The
total number of product patches is therefore bounded by

\[
 C[\log(en)]^{3+d/2}.
 \tag{9}
\]

Use outer polydisks twice the smaller radius, shrinking the initial choices
by a fixed factor if necessary. On each product patch, expand c(s) and
h(t,v_u(z)) in all k=d+1 variables (two times and d-1 chart coordinates).
Variables on which a source does not depend simply have zero coefficients.
Multiply each Taylor coefficient by its multi-radius power. Vector-valued
Cauchy integration, (5)--(7), and the RMS bounds show that every such
weighted coefficient has amplitude at most B sqrt(n) and good-pair root
Lipschitz constant at most

\[
 B=C,\qquad
 A=C(1+\sqrt{\log(en)})e^{C\sqrt{\log(en)}}.
 \tag{10}
\]

Extend each complex vector coefficient from the common good set by the
Euclidean extension proved in `ROOT_RESPONSE_AND_COVARIANCE.md`, treating
C^n as R^(2n), and project it onto its radius-B sqrt(n) ball. The global
coefficient bounds remain (10). The Jacobian has rank at most 2n, so the
scalar divergence estimate (4) of that note gives, for every pair of
extended coefficients, an L2 defect bound at most

\[
                    \frac{C B(B+A)}{\sqrt n}.
 \tag{11}
\]

This is an auxiliary extension argument only. It neither stores the
coefficients nor asks the decoder to evaluate an extension.

Weak derivative locality identifies the extended coefficient derivatives
with the original ones on the good set, outside a common null set for
this countable collection. Coefficient extraction commutes with root
differentiation: the finite-dimensional analytic ODE and the forward maps
are locally smooth in real initial conditions on each safe compact complex
domain, and Cauchy differentiation under its finite contour integral is
valid there.

## 5. Sum first, then take the supremum

On a smaller polydisk the ratio of each variable to its outer radius is
at most one half. Bilinearity of (1) expands its defect into pairs of the
weighted coefficients. The triangle inequality followed by Minkowski and
(11) bounds its supremum in L2 by

\[
 \frac{C B(B+A)}{\sqrt n}
       \left(\sum_{\alpha\in\mathbb N^k}2^{-|\alpha|}\right)^2
     =\frac{C B(B+A)}{\sqrt n}\,2^{2k}.
 \tag{12}
\]

The same bound holds at every finite truncation order. The sum of the
L2 norms is finite, so the infinite auxiliary series converges uniformly
on the smaller closed polydisk almost surely and in the displayed L2
supremum norm. On the good set it is the original analytic defect, by
coefficient equality. Countably many coefficients and finitely many
patches require only one null-set removal.

Square (12), sum over patches using (9), and apply Markov's inequality.
The square root of the patch count contributes log(en)^(3/2+d/4),
and the factor B(B+A) in (10) contributes at most
C sqrt(log(en)) exp(C sqrt(log(en))). This proves (2).

The proof also covers a fixed finite list of layer/sample contractions,
and polynomial temporal truncation degrees growing with n. It is not a
union bound over n-dependent lists of fine real query points with only a
fixed-point second-moment estimate. The analytic geometric summation is
what avoids that loss.

## 6. Consequence and remaining gap

For these actual training/forward-query source pairs, good-event
localization and whole-sphere transfer no longer require additional
Gaussian moment or complex Lipschitz hypotheses. They follow from the
existing source event plus the established real good-pair comparison.
The probability and model scope have not been tightened.

What is still missing is identification of the total derivative trace in
(1) with a compact, computable family of nonlinear response coefficients
for the growing training chronology. This theorem does not supply that
identity, control arbitrary adaptive Stein-test fields, or prove stable
autonomous dynamics for those coefficients. Exponential fitting makes
the prediction after T negligible at the requested accuracy, but it does
not by itself identify endpoint derivative traces. The full unseen-input
decoder therefore remains open.

## Provenance and checking

The lead read the following complete authorized sources before this
derivation: `UNBOUNDED_COMPRESSOR_BRIDGE.md`, `COMPACT_VARIABLE_SOURCE.md`
and `ANALYTIC_TAIL_EXTENSION.md`; the current `GENERAL_DENSE_COMPARISON.md`
and current-study response notes had already been read. The source event
is inherited, not independently reproved here. The extension/divergence
algebra is in `ROOT_RESPONSE_AND_COVARIANCE.md`, Sections 1--3, separately
reconstructed in its check report. This new source-supremum transfer is a
candidate partial theorem pending its own reconstruction.

Source hashes:

- `UNBOUNDED_COMPRESSOR_BRIDGE.md`:
  `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.
- `GENERAL_DENSE_COMPARISON.md`:
  `ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9`.
- `ANALYTIC_TAIL_EXTENSION.md`:
  `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349`.

No numerical experiment, Git mutation, other-study search or promotion
was performed. The new proof uses the original finite horizon T; the
late-time analytic extension was read for scope but is not needed to
assert derivative-trace regularity at the fitted endpoint.
