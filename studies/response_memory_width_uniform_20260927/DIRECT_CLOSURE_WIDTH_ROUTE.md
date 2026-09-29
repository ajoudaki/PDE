# Direct width analysis of the fixed-order closure

28 September 2026. Scoped continuation of the same study. Scientific
inputs: current `ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`, complete
`ACTIVATION_QUADRATIC_DETERMINISTIC.md`, and the prior scoped direct
predictor derivation. No search, experiment, other study, additional agent,
maintained manuscript edit, or Git mutation was used.

**Conclusion.** Fixed order gives a substantially cleaner state and a
useful order-uniform moment energy identity. The learned interactions are
finite-rank empirical contractions. The initialized Gaussian matrices
still act on adaptively evolving nonlinear features and backward fields;
fixed order does not turn these into finitely many Gaussian queries or
independent drivers. A direct closure width proof is a reasonable route,
but a fixed-order theorem with unspecified order dependence would not
prove the requested accuracy exponent.

## 1. Exact finite-order state

Let `tau=1+integral_0^t rho`, and let

\[
 e_k^\tau(s)=\sqrt{\frac{2k+1}{\tau}}
             P_k(2s/\tau-1),\qquad 0\le k<q,
\]
\[
 H_{\ell,a,k}=\int_0^\tau e_k^\tau(s)h_{\ell,a}(s)\,ds,
 \qquad B_{\ell,a,k}=\int_0^\tau e_k^\tau(s)b_{\ell,a}(s)\,ds,
 \qquad b_{\ell,a}=\frac{r_a}{\rho}\delta_{\ell,a}.
 \tag{1}
\]

The forward prefix has clock length one and constant value equal to the
initial feature. The backward prefix is zero. These are actual closure
histories, not dense-driven histories. The low-rank reconstruction is

\[
 \widehat W_\ell=W_{\ell,0}
       -\frac{2}{mn}\sum_{a=1}^m\sum_{k<q}
                    B_{\ell,a,k}H_{\ell-1,a,k}^T.
 \tag{2}
\]

It has learned rank at most `mq` per hidden matrix. At a fixed time,

\[
 z_{\ell,a}=W_{\ell,0}h_{\ell-1,a}
 -\frac2m\sum_{b,k}B_{\ell,b,k}
          \frac{H_{\ell-1,b,k}^Th_{\ell-1,a}}n,
\]
\[
 p_{\ell-1,a}=W_{\ell,0}^T\delta_{\ell,a}
 -\frac2m\sum_{b,k}H_{\ell-1,b,k}
          \frac{B_{\ell,b,k}^T\delta_{\ell,a}}n.
 \tag{3}
\]

Thus the learned forward/backward terms use `O(m^2 q)` empirical scalar
pairings per layer at the current time. The output uses `m` further
readout/feature pairings. A generic inner-layer neuron stores the incoming
backward moments and outgoing forward moments, `2mq` scalar coordinates;
boundary layers additionally carry the first-layer row or readout.
The full moving-state count is exactly the previously stated
`2(L-1)mnq+n(d+1)+O(1)`.

The state is finite-dimensional at finite width. Its vector field still
contains the two matrix actions displayed in (3), with the same fixed
Gaussian matrices used repeatedly in both directions.

## 2. A genuine order-uniform simplification

For any one vector-valued history `v`, let `a=(a_0,...,a_{q-1})` be its
orthonormal moments, defined as in (1). Put `u_k=sqrt(2k+1)` and define
the lower triangular matrix

\[
 A_{kk}=k+\tfrac12,\qquad
 A_{kj}=u_ku_j\ (j<k),\qquad A_{kj}=0\ (j>k).
 \tag{4}
\]

Differentiating the shifted Legendre basis gives

\[
 \frac{da}{d\tau}=\frac{u}{\sqrt\tau}v(\tau)-\frac1\tau Aa,
 \qquad A+A^T=uu^T.
 \tag{5}
\]

The second identity follows directly from (4), including its diagonal.
Consequently

\[
 \frac d{d\tau}\sum_{k<q}\|a_k\|_2^2
 =\|v(\tau)\|_2^2
   -\left\|v(\tau)-\frac1{\sqrt\tau}
                    \sum_{k<q}u_k a_k\right\|_2^2.
 \tag{6}
\]

To verify (6), differentiate the squared norm, substitute (5), and
complete the square. Multiplying by `rho` gives the physical-time
identity. In the backward equation its endpoint input is
`rho b_a=r_a delta_a`, so the raw physical ODE need not divide by a
zero residual.

The homogeneous moment transport is contractive. Its integrated input
gain is independent of `q`, although `||u||_2=q` and a bound based only
on `||A||op` can grow quadratically in `q`. For differences with a
common clock, (6) applies to the difference history as well.

Projection contraction and the finite activity interval give uniform
bounds for the global moment norms
`[sum_{a,k}||H_{ell,a,k}||_2^2/n]^{1/2}` and
`[sum_{a,k}||B_{ell,a,k}||_2^2/n]^{1/2}`. On these energy balls, the
learned bilinear reconstruction and its actions are Lipschitz with
constants independent of `q`. For example

\[
 \left\|\frac1n\sum_{a,k}B_{a,k}H_{a,k}^T\right\|_F
 \le \left(\sum_{a,k}\frac{\|B_{a,k}\|_2^2}{n}\right)^{1/2}
      \left(\sum_{a,k}\frac{\|H_{a,k}\|_2^2}{n}\right)^{1/2}.
 \tag{7}
\]

Subtracting the two products gives the corresponding Lipschitz bound.
This is a real structural improvement over treating each moment as an
unrelated scalar coordinate. Raw monomial moments would instead introduce
an ill-conditioned polynomial Gram matrix; that conditioning is avoided
by (1), not added as a hypothesis.

Different trajectories have different clocks. Comparing their transport
terms directly introduces `(rho/tau-rho_*/tau_*)Aa_*`; (6) does not
alone eliminate the large norm of `Aa_*`. A direct quantitative proof
must handle clock alignment or a history-based energy comparison as
well. It must not infer full order-uniform flow stability merely from
the common-clock identity.

## 3. Why finite moments do not give finitely many Gaussian drivers

The current input to `W_{ell,0}` is `h_{ell-1,a}(t)`, not just one of
the stored moment vectors. Nonlinear activation does not preserve their
current span. Even if one additionally stores `W_0 H_k`, its derivative
contains `W_0 h(t)` by (5); the new stored quantities do not close the
required action.

More fundamentally, a finite-dimensional local neuron state can produce
a history family with infinite-dimensional span in its probability
space. For example, with one standard Gaussian root `Z`, the family
`h_t=sin(tZ)` has covariance

\[
 \mathbb E[h_t h_s]
 =\tfrac12\{e^{-(t-s)^2/2}-e^{-(t+s)^2/2}\}.
 \tag{8}
\]

It has infinite rank on any nonempty time interval: distinct positive
frequencies give linearly independent sine functions in Gaussian `L2`.
This follows because an almost-everywhere linear relation extends to
all real arguments by continuity, and the odd Taylor derivatives form
a Vandermonde system in the squared frequencies. The Gaussian process
with covariance (8) therefore needs arbitrarily many independent
Gaussian coordinates for its finite-dimensional marginals. This example
illustrates the dimensional issue; it is not asserted to be a trajectory
of the present closure.

For the actual reused matrix, the conditional Gaussian driving history
has covariance given by two-time source-feature pairings. Fixed `q`
places no algebraic finite-rank restriction on that covariance. Refining
a time discretization still creates more forward and transpose queries.
The explicit learning memory is truncated; the Gaussian response history
generated by querying the fixed matrix is not thereby truncated.

Diagonalizing `W_0` does not remove this issue for the stated activation
class: coordinatewise nonlinear activation does not commute with its
singular-vector rotations. Woodbury identities address linear solves
with low-rank matrix increments, not the present nonlinear feature and
backward recursions. Changing the Gaussian matrix at each query would
change the model.

## 4. Strongest realistic direct route

A useful direct program is to formulate the finite local moment state
and empirical contractions (1)--(3), preserve the contractive transport
energy (6), and construct a Gaussian response law for the fixed random
matrix actions. The learned branch then requires only ordinary scalar
empirical observables and bilinear bounds such as (7). The initialized
branch still needs a quantitative common-row cavity/response argument
retaining forward/transpose reuse.

The whole-row Gaussian projection in `WIDTH_RATE_DIRECT_PREDICTOR_R2.md`
can control a returned mean response through a coupled scalar backward
field without differentiating `phi''`. Its remaining joint-innovation
and cavity-source obligations persist at fixed `q`. They now concern
a finite-dimensional local ODE state, which is a meaningful simplification,
but its driving process and covariance can still depend on continuous
history. A deterministic and unique fixed-order population predictor
also needs identification; the current theorem supplies only possibly
random subsequential fixed-order predictor limits.

The exact zero-readout forward-Gram equation and all-time resolvent from
that prior note apply directly to the closure. Thus proving a quantitative
forward-Gram source bound for the closure would bypass the dense
trained-carrier remainder entirely. This is the main reason to pursue
the direct route. No such Gaussian source estimate is proved by the
finite-state rewrite alone.

## 5. The order dependence needed for the accuracy exponent

Suppose a direct theorem eventually gives, at fixed confidence and for
its correctly identified population predictor,

\[
 \text{prediction error}\le Cq^{-2+o(1)}+A(q)n^{-1/2+o(1)}.
 \tag{9}
\]

The width exponent and its residual `o(1)` must be controlled along the
chosen growing order; a separate theorem for every fixed `q` does not
ensure this. With `q_epsilon=epsilon^{-1/2+o(1)}`, the sufficient width
from (9) has scale

\[
 n_\epsilon=\epsilon^{-2+o(1)}A(q_\epsilon)^2,
 \qquad n_\epsilon q_\epsilon
       =\epsilon^{-5/2+o(1)}A(q_\epsilon)^2.
 \tag{10}
\]

Therefore the requested `epsilon^{-5/2+o(1)}` moving-state exponent
requires `A(q)=q^{o(1)}` along this sequence, together with compatible
probability bounds and width thresholds. Polylogarithmic factors and
`exp(C sqrt(log q))` are admissible. A polynomial loss `A(q)=q^alpha`
instead gives `epsilon^{-(5/2+alpha)+o(1)}` by this estimate. Exponential
growth in `q` is much worse. Equivalently, balancing the two terms when
`A(q)=q^alpha` gives `q=n^{1/(4+2alpha)+o(1)}`, not `n^{1/4}`.

The energy identity makes subpolynomial order dependence a more plausible
target than a naive moment-coordinate Gronwall estimate suggests. It does
not prove that dependence for the Gaussian response or moving-clock
comparison. Those two points should be tracked explicitly in any direct
fixed-order proof.
