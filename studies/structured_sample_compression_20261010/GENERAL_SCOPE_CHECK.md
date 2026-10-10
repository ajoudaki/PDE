# General scope check: low-dimensional data and all-time sample compression

This is a bounded, prompt-only adversarial route. Scientific inputs were the
supervisor's assignment and its two clarification messages; no book, code,
other study, external scientific source, experiment, or other route was read.
The required canonical-notation, mathematical-proof, conjecture-contract and
adversarial-audit instructions were read. This report is an authored theoretical
candidate, not an independent review or a promoted result.

## What is established here

Low-dimensional analytic inputs and analytic labels with fixed nonzero amplitude
do **not** imply uniform all-time continuity of the trained predictor with respect
to a small absolute error in the empirical measure. This failure already occurs
inside the specified all-trained, zero-readout, deep Gaussian architecture,
with the allowed linear activation and constant labels.

This is a proof-route obstruction, not an impossibility theorem for sample
compression. The same example admits exact compression into finitely many
sample moments. Thus neither this example nor the collapse of a full sample
Gram gap establishes an information lower bound against all admissible compact
surrogates.

The unresolved bridge is stronger than spatial approximation: one needs an
all-time stability estimate in a data metric adapted to the trainable dynamics,
or a reduction that preserves the sensitive coefficients with adequate relative
accuracy. An absolute quadrature error alone cannot supply that bridge.

## An actual deep-network all-time discontinuity

Take input dimension and width \(d=n=2\), any fixed number \(L\geq2\) of hidden
layers, and activation \(\phi(z)=z\). This activation is entire and its derivatives
of positive order are bounded; its values need not be bounded, as allowed in the
assignment. Put \(v=x/\sqrt d\), so \(\|v\|=1\). The original forward pass and
readout are

\[
 h^{(1)}=W^{(1)}v,\qquad
 h^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
 f(x)=\frac1n w^\top h^{(L)}.
\]

All blocks train by gradient flow for the empirical squared loss, with mobilities

\[
 (n,1,\ldots,1,n),\qquad w(0)=0.
\]

Define, only for this proof,

\[
 A_1=W^{(1)}/\sqrt n,\qquad
 A_\ell=W^{(\ell)}\ (2\leq\ell\leq L),\qquad
 a=w/\sqrt n,\qquad F=A_L\cdots A_1.
\]

Then \(f(x)=a^\top Fv\), and each transformed parameter has unit gradient-flow
mobility. For example, \(\nabla_{W^{(1)}}\mathcal L=n^{-1/2}
\nabla_{A_1}\mathcal L\), so \(\dot A_1=-\nabla_{A_1}\mathcal L\).
Write \(u=F^\top a\in\mathbb R^2\), so the predictor is \(u^\top v\).

The input parametrization

\[
 x(s)=\sqrt2(\cos s,\sin s),\qquad y(s)=Y>0
\]

is one dimensional and analytic, with fixed regularity bounds. Every training
label equals \(Y\); both the maximum and empirical root-mean-square label
amplitudes are exactly \(Y\), independently of \(m\).

For \(0<p<1\), let the training measure in the normalized input coordinate be

For the calculations below use one half of the original averaged squared
loss. This rescales time only: the original paper's trajectory at physical
time \(t\) is the following half-loss trajectory at time \(2t\). All
initializations, parameter curves, endpoints, and all-time suprema are
unchanged.

\[
 \mu_p=(1-p)\delta_{e_1}+p\delta_{e_2},\qquad
 \mathcal L_p=\frac12\bigl[(1-p)(u_1-Y)^2+p(u_2-Y)^2\bigr].
\]

Here \(e_1,e_2\) are the coordinate unit vectors in \(\mathbb R^2\). For \(p=1/m\),
this is an ordinary unweighted dataset with \(m-1\) copies of \(e_1\) and one copy
of \(e_2\). Repeated inputs will be removed below. The limiting dataset is

\[
 \mu_0=\delta_{e_1},\qquad \mathcal L_0=\tfrac12(u_1-Y)^2.
\]

### A positive-probability Gaussian event giving complete convergence

All Gaussian initialization laws in question have a strictly positive joint
density for the finite collection \(A_1(0),\ldots,A_L(0)\). The readout is zero.
The following balancedness matrices are constant along the exact flow:

\[
 C_\ell=A_\ell A_\ell^\top-A_{\ell+1}^\top A_{\ell+1}
 \quad(1\leq\ell<L),\qquad
 C_L=A_LA_L^\top-aa^\top.
\]

For completeness, let

\[
 F_0=I,\quad F_\ell=A_\ell\cdots A_1,\quad
 b_\ell=A_{\ell+1}^\top\cdots A_L^\top a,
 \quad b_L=a,
\]

and set \(q=\int (u^\top v-Y)v\,d\mu(v)\). Direct differentiation of the loss gives

\[
 \dot A_\ell=-b_\ell q^\top F_{\ell-1}^\top,
 \qquad \dot a=-F_Lq.
\]

Using \(b_\ell=A_{\ell+1}^\top b_{\ell+1}\) and
\(F_\ell=A_\ell F_{\ell-1}\), the derivatives of \(A_\ell A_\ell^\top\) and
\(A_{\ell+1}^\top A_{\ell+1}\) are both

\[
 -b_\ell q^\top F_\ell^\top-F_\ell q b_\ell^\top.
\]

The same calculation at the readout proves \(\dot C_L=0\).

Let \(E\) be the initialization event on which, for every \(1\leq\ell\leq L\),

\[
 \lambda_{\min}(C_L)+
 \sum_{j=\ell}^{L-1}\lambda_{\min}(C_j)>\tfrac12.
\]

An empty sum is zero. At \(A_\ell(0)=I\) for every layer, the left side is one.
Continuity of the least eigenvalue gives an open neighborhood of that
initialization contained in \(E\). Consequently \(\mathbb P(E)>0\).

On \(E\), all times for which the flow exists satisfy

\[
 A_\ell A_\ell^\top\succeq\tfrac12 I,
 \qquad FF^\top\succeq 2^{-L}I.
\]

Indeed, \(A_LA_L^\top=C_L+aa^\top\succeq C_L\). Inducting backwards in
\(A_\ell A_\ell^\top=C_\ell+A_{\ell+1}^\top A_{\ell+1}\), and using that the
square matrices \(A_{\ell+1}^\top A_{\ell+1}\) and
\(A_{\ell+1}A_{\ell+1}^\top\) have the same least eigenvalue, proves the
first assertion. Multiplying the least singular value bounds proves the second.

There is no finite-time blowup. To see this, put

\[
 R^2=\|a\|^2+\sum_{\ell=1}^L\|A_\ell\|_F^2.
\]

The predictor is homogeneous of degree \(L+1\) in all transformed parameter
blocks. Therefore, for the constant label \(Y\),

\[
 \frac{d}{dt}R^2
 =2(L+1)\int (Yf-f^2)\,d\mu
 \leq\frac{L+1}{2}Y^2.
\]

The finite-dimensional polynomial vector field is locally Lipschitz. The last
inequality bounds all coordinates on every finite time interval, so a local
solution extends to all \(t\geq0\).

For \(\mu_p\), \(q=\operatorname{diag}(1-p,p)(u-(Y,Y))\), and the readout gradient
alone gives

\[
 \dot{\mathcal L}_p
 =-\|\nabla\mathcal L_p\|^2
 \leq-\|Fq\|^2
 \leq-2^{-L}\|q\|^2
 \leq-2^{1-L}\min\{p,1-p\}\mathcal L_p.
\]

Thus \(f_p(\sqrt2 e_1,t)\to Y\) and \(f_p(\sqrt2 e_2,t)\to Y\) as
\(t\to\infty\), for every \(0<p<1\) and every initialization in \(E\).

For \(\mu_0\), \(q=(u_1-Y)e_1\), so the same argument gives

\[
 \dot{\mathcal L}_0\leq-2^{1-L}\mathcal L_0.
\]

The parameter norm has at most square-root growth in \(t\), while \(q\) decays
exponentially. The displayed parameter-velocity formulas are products of \(q\)
with at most \(L\) parameter factors. Their norms are bounded by a polynomial in
\(t\) times a decaying exponential, and hence are integrable. All parameters
therefore converge for \(\mu_0\) as well as for each \(\mu_p\). In particular,

\[
 Z=f_0(\sqrt2 e_2,\infty)
\]

exists and is finite on \(E\).

### The limiting single-point predictor does not recover the rare point

Let \(D=\operatorname{diag}(1,-1)\), and transform only the initial first matrix
by \(A_1(0)\mapsto A_1(0)D\). This leaves its Gaussian law unchanged. It also leaves
every \(C_\ell\), and hence \(E\), unchanged. For training on \(e_1\) only, it
leaves the training trajectory of all other blocks and the first column of
\(A_1\) unchanged. The second column is never updated and changes sign.
Consequently \(Z\mapsto-Z\).

The conditional law of \(Z\) on \(E\) is therefore symmetric, and

\[
 \mathbb P(E\cap\{Z\leq0\})\geq\tfrac12\mathbb P(E)>0.
\]

For every initialization in this event and every \(0<p<1\),

\[
 \sup_{t\geq0}\sup_{\|x\|=\sqrt2}
 |f_p(x,t)-f_0(x,t)|
 \geq |f_p(\sqrt2 e_2,\infty)-f_0(\sqrt2 e_2,\infty)|
 \geq Y.
\]

On the other hand the Wasserstein distance for the Euclidean metric on the
normalized inputs is \(W_1(\mu_p,\mu_0)=\sqrt2p\). Every bounded test-function
moment also changes by at most twice its supremum norm times \(p\).
Thus there is no modulus \(\omega(\delta)\to0\), deducible from input/label
regularity alone, controlling the all-time predictor difference by
\(\omega(W_1(\mu_p,\mu_0))\). The same failure holds for the finite test panel
containing \(\sqrt2e_2\).

This statement concerns a positive-probability event at fixed width two. It is
not a lower bound with probability tending to one as width grows, and it does
not refute a theorem that explicitly discards this event at its stated failure
probability. It does refute a deterministic universal stability implication
from low-dimensional analytic regularity alone. A probabilistic theorem must
state the failure probability and the order of its \(m,n\) limits.

### Distinct inputs do not repair this discontinuity

Use \(m-1\) distinct angles in symmetric pairs \(\pm\alpha_j\), with a single
zero angle when needed, all satisfying \(|\alpha_j|\leq\delta_m=m^{-2}\).
Add the angle \(\pi/2\). Keep every label equal to \(Y\). Put \(p=1/m\), and let
\(S_m\) be the average of \(\sin^2\alpha_j\) over the cluster. Symmetry makes
the off-diagonal empirical second moment zero and makes the cluster's mean
second coordinate zero. The unique linear least-squares predictor therefore
has second coefficient

\[
 u_{*,2}=\frac{pY}{p+(1-p)S_m}
 \geq\frac{Y}{1+m\delta_m^2}\longrightarrow Y.
\]

The full empirical covariance is positive definite. If its least eigenvalue
is \(\lambda_m>0\), the preceding readout-gradient argument applies to
\(\mathcal L-\min\mathcal L\), giving exponential decay at rate at least
\(2^{1-L}\lambda_m\). The same polynomial-times-exponential velocity argument
proves parameter convergence to this least-squares predictor. Meanwhile the
empirical measures converge to \(\delta_{e_1}\) in \(W_1\), at distance at most
\(\delta_m+\sqrt2/m\). On \(E\cap\{Z\leq0\}\), the limiting test discrepancy is
again at least \(Y\) in the limit \(m\to\infty\).

The feature Gram matrix for linear activation has rank at most two, so this
example is not claimed to satisfy the previous full \(m\times m\) positive-gap
theorem. It tests the proposed replacement of that hypothesis by low-dimensional
smooth data structure. No use was made of the old shrinking-label cap.

## Why this is not an impossibility theorem for sample storage

For a linear activation, every sample dependence of the exact gradient flow
is through

\[
 \Sigma=\frac1m\sum_{j=1}^m v_jv_j^\top,
 \qquad b=\frac1m\sum_{j=1}^m y_jv_j,
 \qquad q=\Sigma u-b.
\]

These require \(d(d+1)/2+d\) real coordinates. The additional scalar
\(m^{-1}\sum_jy_j^2\) is sufficient to reconstruct the loss if that is also
requested. They can be accumulated from the initial dataset and retained
without any future-state information or data oracle. The displayed exact
parameter ODE then uses only these fixed coefficients and its current state.

Hence this all-trained deep linear example admits exact \(O(1)\) sample storage
at fixed \(d\), despite its all-time discontinuity in absolute moment error.
The rare coefficient \(p\) must be preserved, rather than dropped as an
absolutely small quadrature error. The result isolates sensitivity and does
not establish a metric-entropy or information lower bound for the larger
nonlinear class. It also retains the dense width-dependent parameter state;
it does not solve simultaneous width compression.

## Assumptions that actually change the problem

Several distinct assumptions are easily conflated.

1. A fixed latent dimension and a uniform Lipschitz or analytic bound on the
   initial input and label maps bound their approximation complexity. They do
   not bound the relative importance of small empirical masses, the condition
   number of the training problem, or the reachable network's spatial
   regularity for all time. The example proves the first two limitations.

2. A density bounded above and below on a fixed latent domain, together with a
   quantitative empirical sampling condition, excludes the disappearing-mass
   geometry used above. It does not itself prove stability of feature learning
   or an invariant source condition. Smoothness may still coexist with very
   small spectral modes. No counterexample within that strengthened class is
   proved here.

3. A label source condition relative to an initial kernel can control label
   amplitude in initially weak modes. In the all-trained system, the feature
   map changes. To use that source condition for all time, one must derive its
   preservation or control the transfer of labels/residuals into newly weak
   modes. Initial spectral information alone is not an estimate for a rotating
   feature family. This is a missing proof obligation, not a constructed
   rotating-mode counterexample for this network.

4. A uniform all-time sensitivity or coercivity hypothesis would provide the
   missing bridge, but assuming the desired trajectory estimate as a
   hypothesis is not an unconditional derivation from data structure. A useful
   sufficient condition must be checkable at initialization and must imply the
   trajectory bound by a complete argument.

A fully nonvacuous exact initial-data class is finite support: if the dataset
has at most \(s\) distinct input-label pairs, where \(s\) is independent of \(m\),
retain those pairs and their multiplicities. The empirical loss and every
gradient block are exactly the same weighted sums over these \(s\) pairs.
This works for the entire nonlinear activation class, every width and depth,
and every time at which the reference flow exists. It removes the sample axis
exactly, without reducing width. It is much more restrictive than a genuinely
continuous low-dimensional sample manifold and should be identified as such.

For continuous low-dimensional data, a promising but unproved sufficient
package would combine quantitative coverage of the latent domain, a fixed
analytic complex-neighborhood bound for inputs/labels, an initialization-checkable
invariant bound on parameter motion, and a coercivity/source estimate on the
specific function class generated by the dynamics. The hard part is deriving
the latter two from the first two for fixed nonzero \(Y\). They cannot be counted
as consequences of low-dimensional analyticity without that derivation.

## Storage, precision, and limit-order audit

- Count retained sample coordinates and fixed coefficients, not only evolving
  variables. A function-valued empirical-measure object, an evaluator with
  access to all latent sample locations, or a table hidden behind an oracle
  still retains the samples.
- A finite real-coordinate count alone permits pathological encodings of an
  entire dataset in one real number. An admissible construction needs explicit,
  computable coefficient provenance and ordinary finite operations; precision
  must be reported separately as requested.
- Constants must be uniform in the stated structural bounds. Calling a family
  analytic without a common complex neighborhood and a common norm bound
  allows arbitrarily increasing effective complexity. Similarly, letting the
  latent domain's diameter or the number of chart pieces grow with \(m\)
  can hide sample dependence.
- For fixed width and input dimension, storing all network parameters is
  already independent of \(m\), but generally leaves \(O(Ln^2+nd)\) moving
  coordinates. A purported sample theorem should say whether this destroys
  the intended width compression as \(n,m\to\infty\).
- Spectral decay at each separate time does not bound the dimension of the
  union of the corresponding important subspaces. A feature family may
  change its important directions; whether this actual network does so enough
  to obstruct compression remains open here.
- Compact-time continuity follows from local ODE stability on bounded sets;
  it cannot be extended to \(t=\infty\) by silently exchanging limits. In the
  example, the trajectories converge as \(p\to0\) on each fixed compact time
  interval, while eventual predictions remain separated. The time needed to
  exhibit a fixed positive discrepancy must therefore diverge. This proof
  does not identify its exact rate.

## Current verdict

**Proved candidate:** fixed-amplitude analytic low-dimensional data do not
imply an all-time absolute-quadrature stability estimate for the actual
all-trained deep architecture. The proof includes the Gaussian event,
global existence, convergence, and a version with distinct sample points.

**Not proved:** an \(O(1)\)/polylogarithmic sample-storage impossibility theorem
for the full admissible approximation class, a high-probability large-width
obstruction, or an obstruction under quantitative nonconcentration and a
compatible invariant source condition.

**Useful exact subclass:** finite support permits exact sample aggregation
for all activations; linear activation permits exact covariance/label-moment
aggregation even for continuous low-dimensional datasets.

The decisive next bridge is a derived, initialization-checkable all-time
stability/source theorem for genuinely nonlinear feature learning. Spatial
regularity estimates or quadrature constructions cannot substitute for it.
