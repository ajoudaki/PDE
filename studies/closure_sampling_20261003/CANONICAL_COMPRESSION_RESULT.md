# Sublinear coordinated neuron compression of an actual Gaussian dense run

2026-10-03. Internally derived and checked research result. The reference
is the original finite network, not a population predictor. The full proof
is [CANONICAL_NEURON_COMPRESSION.md](CANONICAL_NEURON_COMPRESSION.md);
its full reconstruction is
[CANONICAL_NEURON_COMPRESSION_CHECK.md](CANONICAL_NEURON_COMPRESSION_CHECK.md).
These are internal checks, not promotion reviews or manuscript theorems.

## Precise positive result

Take two tanh hidden layers, both of original width $n$, no biases, and

\[
 h(x)=\tanh(Ax/\sqrt2),\qquad
 g(x)=\tanh(Wh(x)),\qquad f_n(t,x)=w^\top g(x)/n.
\]

Initially the read-in entries are independent $N(0,1)$, the hidden-matrix
entries are independent $N(0,1/n)$, the arrays are independent, and the
readout is zero. All three blocks train with the manuscript's mobilities
$(n,1,n)$ and squared loss. The training set is the one circle input
$x_1=\sqrt2e_1$ with a sufficiently small fixed label $y>0$. The label
threshold is positive and independent of width. Queries range over the
**entire circle**, $x_\theta=\sqrt2(\cos\theta,\sin\theta)$.

For each fixed $0<\eta<1/2$ and confidence $1-\eta$, an initialization-only construction
selects and weights far fewer neurons in both layers and constructs their
small initial mixer. The resulting weighted network trains autonomously
using its own residual. For all sufficiently large $n$, with probability
at least $1-\eta$,

\[
 \boxed{\sup_{t\in[0,\infty]}\sup_{\theta\in\mathbb R}
       |f_C(t,x_\theta)-f_n(t,x_\theta)|\le\frac C{\sqrt n}.}
\]

Both models converge and interpolate the training label. The displayed
supremum explicitly includes their fitted limits. The constant $C$ is
independent of width and physical time. There is no omitted sampling bias
or finite-network-to-population term.

The **total moving state**, including the entire smaller learned hidden
matrix, is bounded by

\[
 \boxed{P_n\le C\exp\!\left(C\sqrt{\log(en/\eta)}\right)
                  [\log(en/\eta)]^{10}=n^{o(1)}.}
\]

For fixed confidence this is $o(n)$, and eventually smaller than $n^\alpha$
for every fixed $\alpha>0$. It is not a polylogarithmic bound. Fixed storage
after setup has the same order; no original-width array or trained-path
oracle is retained. The construction is proved in exact real arithmetic.
Its initialization work and numerical conditioning may be expensive; this
result does not establish a practical implementation cost.

The reference initialization remains exactly canonical Gaussian. The smaller
network uses coordinated weights and a projected mixer, as intended by the
sampling question. Its forward and backward passes use the same evolving
small matrix and the exact weighted adjoint. This is a direct dense-model
construction, not an unproved modification of the original order-$q$
closure.

## Why ordinary sampling was the wrong comparison

Independent sampling spends neurons estimating whichever response happens
to be queried. Here the construction first identifies a finite collection
of response directions sufficient for the whole nonlinear trajectory and
all circle queries. It selects positive neuron weights that preserve their
pairwise products. It also preserves how the original mixer transports
those directions **in both orientations**.

Preserving only initial outputs would not suffice: a small initial forward
error could alter the reverse response and all subsequent feature motion.
The proof controls paired forward and reverse sources together. The same
weighted neurons therefore approximate the feedback driving their own
future movement. This is coordinated empirical cubature for an actual
realized network, with its approximation error bounded directly.

## The mechanism that makes a finite response collection sufficient

For one training input, let $a=Ae_1$ and change the independent variable to
activity $s$, where $ds/dt=2(y-f_n(t,x_1))$. The exact activity equations
are independent of the label; a small label chooses an endpoint on a
fixed short activity interval.

The useful coordinate change is

\[
 u=\Psi(a),\qquad \Psi(a)=a/2+\sinh(2a)/4.
\]

Since $\Psi'(a)=\cosh^2a$, it cancels the first-layer gate in the
backward equation:

\[
 a'=\operatorname{sech}^2a\odot W^\top\delta
 \quad\Longrightarrow\quad u'=W^\top\delta,
 \qquad\delta=w\odot\operatorname{sech}^2(Wh).
\]

This is an exact change of coordinates. It removes the large backward
carrier from the local stability constant, while the nonlinear forward
features and learned matrix remain fully active.

A finite Gaussian deletion-and-reinsertion argument then proves that the
actual response functions are holomorphic in a complex neighborhood of
the activity interval and circle angle, with radii proportional to
$1/\sqrt{\log(en/\eta)}$. This estimate is proved for the finite adaptive
network itself. Analytic continuation of initial derivatives and finite
trigonometric interpolation supply a sufficiently accurate response space
of dimension $n^{o(1)}$, using initialization only.

Positive cubature selects $O(R^2)$ neurons per layer from response spaces
of dimension $R$. The smaller dense matrix therefore costs $O(R^4)$
coordinates. The proved response dimension is small enough that this
entire count remains $n^{o(1)}$.

Finally, a weighted stability estimate controls the smaller network's own
nonlinear evolution. The training prediction is strictly increasing in
activity on the relevant interval. Consequently the two scalar physical
clocks contract their discrepancy, converting equal-activity accuracy into
accuracy at the **same physical time**, uniformly up to infinity.

## Feature learning and exact limits of scope

[CANONICAL_FEATURE_LEARNING.md](CANONICAL_FEATURE_LEARNING.md) proves that
both hidden training-feature vectors move by at least $c s^2$ in empirical
RMS on a fixed activity interval. At the fitted endpoint both displacements
are at least $c y^2$, independent of width for fixed nonzero $y$. The same
conclusion transfers to the compressed network at sufficiently large width.
This verifies actual movement of both nonlinear representations; it makes
no additional claim about an unknown test-label rule.

The positive result settles the requested existence question for one
nontrivial canonical deep feature-learning configuration. Two distinct,
non-antipodal canonical training inputs, general datasets, arbitrary depth,
large labels, and a polylogarithmic state bound are not established by it.
The separate two-input assessment records a concrete obstruction to simply
repeating the one-input proof, not an impossibility theorem for compression.

No numerical training experiment, manuscript edit, promotion, commit, or
push was performed in this continuation.
