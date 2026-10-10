# Compression preserves a nonvanishing feature-learning effect

Date: 2026-10-10. Author-derived consequence of the repaired
[compatible-data theorem](COMPATIBLE_RESULT.md) and the current paper's
compression theorem. This is a proposed paper addition, not a change to the
paper or a promotion to the maintained book.

The later companion `INPUT_NONLINEARITY_RESULT.md` strengthens this proposed
addition by also excluding every affine-in-input predictor, including deep
linear feature learning with a moving kernel. `NONLINEAR_FEATURE_INCREMENT.md`
further certifies change of the nonlinear part of the dense first-layer
features. The fixed-kernel separation in this file alone is not a proof of
either stronger property; the companion arguments supply those certificates.

## Main message and scope

The compressed trajectories preserve nonlinear feature learning, rather than
merely approximating a regime in which feature learning disappears with width.
The distinction is observable: the approximation error vanishes, whereas the
departure from the dense network's frozen initial tangent kernel stays positive.
All hidden layers of the reference network contribute to this departure.

Use the paper's network, zero-readout Gaussian initialization, squared loss,
mobilities, fixed nonzero labels, and compression hypotheses. For this
additional conclusion only, assume every activation is nonaffine and
\(|x_a^\top x_b|<d\) for distinct training inputs. These are sufficient
nondegeneracy conditions, not replacements for the broader compression
theorem. Unbounded activation values remain allowed. Unit Gaussian second
moments are optional normalization, not a further restriction.

Throughout, the complete-trajectory norm \(\|\cdot\|_{\mathcal X}\) and
query domain are exactly those of the compression theorem: the sphere for
Legendre and Harmonic, and the declared finite panel for Taylor. Let
\(f_{{\rm NTK},n}\) be training with the same dense initialization but its
initial tangent kernel held fixed. At zero readout this is precisely training
only the readout with all hidden features frozen. Its training predictions are

\[
 f_{{\rm NTK},n}(t)=(I-e^{-2tQ_n^{(L)}(0)/m})y,
 \qquad (Q_n^{(L)}(0))_{ab}
       =\frac1n h_a^{(L)}(0)^\top h_b^{(L)}(0).
\]

At other queries use the corresponding initialized feature cross-kernel.
No comparison to a compressed model's own tangent kernel is intended.

## Proposed main-text corollary

**Compression beyond the frozen-kernel regime.** Under the compression
theorem's hypotheses, additionally suppose that the training inputs are
pairwise nonparallel and every activation is nonaffine. With exactly the
same storage bounds and query domains, each of Legendre, Harmonic and Taylor
satisfies

\[
 \|f_{\rm model}-f_n\|_{\mathcal X}\xrightarrow{\mathbb P}0,
 \qquad
 \Pr\{\|f_{\rm model}-f_{{\rm NTK},n}\|_{\mathcal X}\ge c\}
 \longrightarrow1
\]

for a fixed \(c>0\) depending on the admissible problem, not on width.
Every hidden layer of the dense reference has nonvanishing normalized
feature displacement at each fixed sufficiently small positive time.

The stronger exact comparison is

\[
 \frac{\|f_{\rm model}-f_{{\rm NTK},n}\|_{\mathcal X}}
      {\|f_n-f_{{\rm NTK},n}\|_{\mathcal X}}
 \xrightarrow{\mathbb P}1.
 \tag{1}
\]

This last ratio is useful in the proof and discussion, but need not be a
second main-text display. It says that compression preserves the magnitude
of the observable departure from frozen features, not just its nonzeroness.

### Proof

The repaired compatible-data theorem gives a deterministic positive time
\(t_0\), independent of width, and \(c_0>0\) such that

\[
 \Pr\{y^\top(f_n(t_0)-f_{{\rm NTK},n}(t_0))\ge c_0\}
 \longrightarrow1.
\]

Because \(y\ne0\), duality with \(\|y\|_1\) implies
\(\max_a|f_n(t_0,x_a)-f_{{\rm NTK},n}(t_0,x_a)|
\ge c_0/\|y\|_1\) on this event. Each query domain contains all training
inputs. Hence the same lower bound holds for its complete-trajectory norm.
The constants may depend on data, labels and activations; no quantitative
lower bound uniform over near-affine activations or nearly parallel inputs
is being asserted.

Each existing compression error tends to zero in probability. For Harmonic
and Taylor this follows from their \(Y/n\) accuracy at every fixed confidence
and eventual width. For Legendre the optimized construction gives
\(CY/[\sqrt n\log(en)^3]\) under the same convention. For any tolerance and
failure budget, first fix that budget and then take width sufficiently large;
this is convergence in probability and needs no common event across widths.

The reverse triangle inequality now gives, deterministically,

\[
 \left|\|f_{\rm model}-f_{{\rm NTK},n}\|_{\mathcal X}
       -\|f_n-f_{{\rm NTK},n}\|_{\mathcal X}\right|
 \le\|f_{\rm model}-f_n\|_{\mathcal X}.
\]

Take \(c=c_0/(2\|y\|_1)\) to obtain the stated event, and divide by the
positive dense-to-frozen lower bound to obtain (1). A finite union bound
makes this simultaneous over all three schemes. The layerwise feature claim
is exactly the repaired compatible-data theorem. No new stored coordinates,
initialization inputs or trajectory modifications are introduced.

## Why the feature-learning contribution cannot cancel

This is the central proof insight worth explaining in the main paper.
Initially the readout vanishes, so hidden velocities vanish. The readout
first grows at order \(t\), hidden weights and features then change at order
\(t^2\), and predictions first depart from frozen-feature training at order
\(t^3\). In the mobility coordinates
\(\theta_{\rm hid}=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)})\), the exact
finite-width onset identity is

\[
 y^\top\{f_n(t)-f_{{\rm NTK},n}(t)\}
 =\frac m3\|\ddot\theta_{\rm hid}(0)\|_2^2t^3+o(t^3).
 \tag{2}
\]

The remainder in (2) is initially a finite-width statement. The repaired
population proof derives its own strong small-time expansion before choosing
a fixed time and transferring back to finite width. It does not interchange
a width-dependent remainder with the width limit.

Every layer contributes a strictly positive squared norm to the coefficient
in the population limit.
The adjoint identity couples the propagated lower-layer response to the new
learned-link response with the same sign. In the output tangent Gram, the
emerging hidden tangent directions and the changing readout features each
contribute exactly half the leading positive coefficient. Thus the effect is
neither an arbitrary parameter reparametrization nor cancellation-prone motion
that leaves the predictor unchanged.

The existing stability proof serves a different purpose: integrated residual
activity controls total feedback, and the selected constructions' correction
cancels the unstable readout--residual term. Stability bounds the error made
by compression; it does not require the underlying hidden movement to vanish.
This is why small approximation error and persistent feature learning coexist.

## A stronger observable: early training improves on the frozen kernel

For this subsection only, let
\(A(y)=\lim_{n\to\infty}\|\ddot\theta_{{\rm hid},n}(0;y)\|_2^2>0\),
the deterministic population coefficient proved in the compatible-data
theorem, and write \(f(t)\) for population training predictions. The kernel
variation-of-constants argument gives the vector difference
\(f(t)-f_{\rm NTK}(t)=O(t^3)\), not just its pairing with \(y\).
For \(\mathcal L(t)=m^{-1}\|f(t)-y\|_2^2\), elementary expansion gives

\[
 \begin{aligned}
 \mathcal L_{\rm NTK}(t)-\mathcal L(t)
 &=\frac2m y^\top(f-f_{\rm NTK})
    -\frac1m(f+f_{\rm NTK})^\top(f-f_{\rm NTK})\\
 &=\frac23 A(y)t^3+o(t^3)>0
 \end{aligned}
 \tag{3}
\]

at every sufficiently small positive time. The second term is \(O(t^4)\)
because both predictions are \(O(t)\). Thus hidden learning initially
improves training MSE over the same initialized frozen-feature model.

At each such fixed time, prediction convergence transfers (3) to finite width
and to all three compressions. Indeed
\(|\mathcal L(g)-\mathcal L(f)|
\le m^{-1}\|g-f\|_2(\|g-y\|_2+\|f-y\|_2)\), and the second factor is
bounded in probability. The limiting positive training-loss improvement is
therefore identical for the dense and compressed predictions. This is an
early-time training comparison, not an endpoint or generalization claim.

## Beyond the particular initialization kernel

The trajectories cannot be explained by any single rule linear in the labels.
Use the same initialized dense weights for labels \(y\) and \(y/2\); both
satisfy the original label condition. Hidden acceleration is quadratic in
the labels by its exact initialization formula, so its squared norm scales
as \(A(y/2)=A(y)/16\). The frozen-kernel predictions are linear in labels.
Subtracting the two population versions of (2) therefore yields

\[
 y^\top\{f(t;y)-2f(t;y/2)\}
 =\frac m4 A(y)t^3+o(t^3)>0.
 \tag{4}
\]

For any common matrix \(B\) mapping training labels to training predictions,

\[
 \max_{z\in\{y,y/2\}}\|f(t;z)-Bz\|_\infty
 \ge\frac13\|f(t;y)-2f(t;y/2)\|_\infty.
 \tag{5}
\]

This follows by writing the superposition defect as the first error minus
twice the second. In fact the factor \(1/3\) is optimal, as the complete
[label-superposition calculation](LABEL_SUPERPOSITION.md) shows. Combining
(4)--(5), for every fixed sufficiently small \(t>0\), the large-width
compressed predictions obey, with probability tending to one,

\[
 \inf_{B\in\mathbb R^{m\times m}}
 \max_{z\in\{y,y/2\}}\|f_{\rm model}(t;z)-Bz\|_\infty
 \ge\frac{mA(y)}{24\|y\|_1}t^3.
 \tag{6}
\]

The factor \(1/24\) leaves a fixed margin below the limiting coefficient
\(1/12\). Convergence is joint for the two label runs and three compression
schemes by a finite union bound. The elementary transfer estimate is that
the error of the compressed superposition defect is at most the compression
error for \(y\) plus twice that for \(y/2\).

Every zero-initialized fixed-kernel square-loss flow with label-independent
kernel has the form \(B(t)z\), so (6) rules out a common fixed-kernel
explanation across these two admissible problems. It does not rule out
label-dependent kernel selection or fitting a special kernel to a single
observed trajectory. The conceptual comparison uses two runs; it adds no
per-run storage to the construction.

## Recommended paper integration

Keep the main compression theorem unchanged. Immediately after it add the
short corollary above, with the nondegeneracy hypotheses attached only there.
Follow it with the readout \(t\), hidden \(t^2\), output \(t^3\) mechanism,
and explain the sum-of-squares identity rather than adding more order bounds.
A sentence may note the strict early training-MSE gain and the nonlinear
label response; (3)--(6) belong in the appendix.

The compression contribution can then be stated as three separated scales:

\[
 \text{compression error}
 \ \ll\ \text{independent dense-run variability}
 \ \ll\ \text{departure from frozen-feature training}.
\]

Here the first comparison is the paper's error ratio converging to zero in
probability. The second follows from its dense upper bound tending to zero
at fixed problem parameters and the new positive lower bound. It concerns
the same full-trajectory/query-domain norm throughout. It is not a claim
that the feature-learning effect is numerically large uniformly over the
allowed small labels; its key property is that it does not vanish with width.

Keep the activation best-affine-fit lemma in the appendix as an auxiliary
nondegeneracy check. The observable separation, loss gain and label-scaling
failure carry more of the paper's message than another abstract assertion
that the activation is nonlinear. Do not claim that prediction accuracy
identifies the compressed model's internal representations layer by layer.

For a self-contained paper proof, the fixed-time transfer must be supplied as
a local population lemma with its proof, or replaced by a width-uniform real
remainder argument. The present research proof uses the established maintained
book's local population theorem (`docs/03-local-population.qmd`, C.1), not the
paper's shrinking complex-time radius. Simply copying this corollary into the
paper without that dependency would not meet its self-contained-proof contract.
The short algebraic additions (1)--(6) are complete; importing that local
population module is a separate integration task, not a hidden new compression
hypothesis or a change in the storage theorem.
