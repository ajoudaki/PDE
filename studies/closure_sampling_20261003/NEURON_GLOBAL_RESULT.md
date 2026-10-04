# Neuron reduction: a fitted-function obstruction and an exact response sampler

2026-10-03. Continuation of the same neuron-sampling investigation. These
are internal research results, not promoted manuscript theorems. The general
source-dependent, weighted, all-time neuron-reduction problem remains open.
The new negative result has a substantive but explicit restriction on the
smaller initialization law; the positive result concerns finite initial
derivatives, not the requested full trajectory.

## 1. The unchanged target

The reference is the realized width-$n$, order-$q$ autonomous response-memory
closure with two tanh hidden layers, canonical Gaussian initialization, zero
initial readout, fixed compatible sphere data, and sufficiently small fixed
labels. It uses the original residual-RMS clock. The goal is an autonomous
representation with fewer neurons, retaining both forward and reverse mixer
actions, its own residual, and its own coupled memories, such that

\[
 \left(\int\sup_{t\ge0}
 |\widetilde f(t,x)-\widehat f_{n,q}(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_{\delta,\mu}/\sqrt n
\]

with probability at least $1-\delta$. The constant must be independent of
width and time; the guarantee includes the fitted limit. A total moving
count below $n$ is the strongest target. Setup may use the initialized
arrays and fixed data, but not a trained reference trajectory. No dense
trained matrix or population-limit comparison replaces the reference.

## 2. A negative theorem at the fitted endpoint

Consider one training input $x_1=\sqrt d\,e_1$, one sufficiently small
fixed label $y>0$, and the unseen input $x_*=\sqrt d\,e_2$.
Let both the width-$n$ and width-$N$ systems have canonical Gaussian
initialization at their own widths. Their initializations may be coupled
in **any** way, and their two memory orders may be arbitrary deterministic
functions of the widths. Both systems run their actual autonomous closures.

There are fixed $c_y,p_*>0$ such that, for $N\to\infty$ and $N=o(n)$,

\[
 \mathbb P\left\{
 \text{both systems fit, and }\quad
 |\widehat f_{N,q_N}(\infty,x_*)-
   \widehat f_{n,q_n}(\infty,x_*)|
 \ge c_y N^{-1/2}\right\}\ge p_*.
 \tag{1}
\]

There is also a fixed-positive-physical-time version. The complete
[proof](NEURON_GLOBAL_NEGATIVE.md) includes the nonlinear dynamics and the
probability bound. It does not infer a trained prediction discrepancy merely
from an initial derivative discrepancy.

The point query can also be replaced by any fixed probability law on
$\{\sqrt d\,v:\|v\|_2=1,\ v\perp e_1\}$. Then (1) holds with
the fitted $L^2(\mu)$ discrepancy in place of its pointwise discrepancy.
For example, in $d=3$ this is the uniform law on the entire unseen circle
$\sqrt3(0,\cos\theta,\sin\theta)$. This is a continuum-query theorem;
it is not a theorem for uniform measure on the full input sphere. The
full-time norm in Section 1 dominates the fitted norm, so it has the same
lower bound.

Consequently, within this class, $N=o(n)$ cannot attain root-$n$ accuracy
at every fixed prescribed confidence. More memory orders do not remove the
obstruction. Ordinary initialization-independent selection of $N$ rows and
columns, followed by variance-preserving mixer rescaling, belongs to this
class. Independence of the two trained networks is not required.

### Why the fluctuation survives learning

At a generic width $k$, let $A_0,W_0$ be the initialized read-in and mixer,
and define the initial upper features and their two scalar pairings by

\[
 g_0(x)=\tanh\!\left(W_0\tanh(A_0x/\sqrt d)\right),\qquad
 G_k=\frac{\|g_0(x_1)\|_2^2}{k},\qquad
 K_k(x_*,x_1)=\frac{g_0(x_*)^\top g_0(x_1)}{k}.
\]

Training changes only the first column of $A$. The independent Gaussian
query column $A_0e_2$ stays unchanged. The small-label fitting theorem,
the readout equation, and interpolation imply

\[
 f_k(\infty,x_*)=\frac{y}{G_k}K_k(x_*,x_1)+R_k(x_*).
 \tag{2}
\]

On a training-only event with exponentially small failure probability,
$G_k$ has a fixed positive lower bound and, conditionally on the training
initialization,

\[
 \|R_k(x_*)\|_{L^2(A_0e_2)}\le C y^3/\sqrt k.
 \tag{3}
\]

The leading kernel fluctuation has second moment at least $c/k$, and
the fitted prediction has fourth moment at most $C y^4/k^2$ on that
event. A sufficiently small fixed $y$ makes (3) smaller than the leading
$y/\sqrt k$ fluctuation. Moment inequalities then prove (1), under any
coupling of widths.

The width factor in (3) is essential. It comes from differentiating the
**whole nonlinear remainder** with respect to the untouched Gaussian query
coordinates: its gradient norm is at most $Cy^3/\sqrt k$. Oddness makes
its conditional mean zero, and the Gaussian variance inequality supplies
(3). A width-independent $Cy^3$ estimate would not prove this result.

### The exact restriction

The smaller model must retain the canonical Gaussian marginal law. A
source-dependent weighted cubature may deliberately change that law and
cancel these fluctuations. Our earlier joint cubature does exactly this at
initialization. Thus (1) is not a proof that the learned function, or its
entire trajectory, is incompressible under the user's proposed structured
sampling. A large unrecovered internal vector is also insufficient to
extend (1) to that class without a prediction lower bound.

## 3. A positive construction preserving arbitrary finite initial responses

For every fixed initialized original closure, every order $q$, and every
integer $p\ge0$, a positive weighted neuron selection can preserve all
training prediction derivatives through order $p$ exactly. It also
preserves the corresponding retained-neuron state derivatives, the clock,
and the forward and backward moments. It is a defined autonomous weighted
closure after setup, with its own residual and the same memory order.

For fixed input dimension and training sample count, it uses $O(p^2)$
neurons in each layer. Its fixed mixer has the exact weighted adjoint and
operator norm at most that of the original initialized mixer. The
construction uses derivatives computed by differentiating the original
finite equations at initialization; it does not query a trained path.
Any fixed finite set of passive query inputs can be included with the same
quadratic dependence on $p$.

The [construction and proof](NEURON_GLOBAL_POSITIVE.md) preserve empirical
inner products on two source spaces. The lower space includes forward
response derivatives and reverse mixer responses; the upper space includes
upper feature derivatives, backward derivatives, and forward mixer images.
Positive cubature of all pairwise basis products uses quadratically many
nodes. The resulting two-sided projected mixer reproduces both required
actions. An induction through the actual moment equations then reproduces
the specified derivatives.

This resolves a local obstruction: a fixed number of newly generated
response directions does not itself force a large neuron count. The sampler
can include those directions before training starts. It also shows why
testing only a second or third derivative cannot rule out the intended
response-aware sampler.

It does **not** establish all-time accuracy. A bound on the Taylor
remainder, uniform in width and order through the fitting period, is still
missing. Smooth Gaussian response populations need not have a positive
$L^2$ Taylor radius; the positive note gives an explicit diagnostic proving
this fact without claiming nonanalyticity of the actual trained flow.

## 4. Another checked implication, and where its use stops

The existing second-order temporal-history bound implies more than a
projection error estimate. If $a_j$ are the normalized Legendre coefficient
vectors of an actual first-layer history and $b_j=\|a_j\|_2/\sqrt n$,
then

\[
 \sum_{j\ge1}[j(j+1)]^2b_j^2\le B^2.
\]

Hence $\sum_j b_j^p<\infty$ for every $p>2/5$, with a bound in terms
of $B,p$. Applying the actual fixed mixer preserves the weighted estimate
up to its operator norm. This is pathwise information about the real
response history, not a population approximation.

However, these coefficients depend on the learned history. They are not
fresh Gaussian source coordinates. The positive note gives an exact neural
calculation in which a forward action on a second response derivative is a
nonnegative nonconstant quadratic Gaussian expression after conditioning
only on initial forward features. The appropriate reverse response must
also be revealed before the remaining mixer action becomes conditionally
Gaussian. A small temporal tail therefore cannot be substituted for a
proved small sensitivity to unsampled random source directions.

## 5. Current conclusion

The requested broad dichotomy is not settled. There is now a complete
endpoint obstruction to all narrower closures retaining the canonical
Gaussian initialization law, and an exact response-aware neuron sampler
for every finite collection of initial derivatives. Neither establishes
all-time success or impossibility for general source-dependent weighted
sampling. The existing memory-order compression theorem remains unchanged.

No experiment, population-rate premise, clipping, trained-path oracle,
manuscript edit, or Git mutation was used. Full internal check records are
linked from the study README; these checks are not promotion reviews.
In particular, [the negative check](NEURON_GLOBAL_NEGATIVE_CHECK.md)
reconstructs the point-query theorem, [the positive check](NEURON_GLOBAL_POSITIVE_CHECK.md)
reconstructs the response sampler, and [the coordinator check](NEURON_GLOBAL_COORDINATOR_CHECK.md)
also verifies the continuum extension and final source versions.
