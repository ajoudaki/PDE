# Sample modes as a third compression axis

Continuation after the user's clarification, 2026-10-10. This note develops
the response-level interpretation of the same sample-compression question.
It does not supersede the proved finite-time results in `RESULT.md` or assert
a complete-trajectory theorem for the three existing methods.

## Target and interpretation

The network's responses have three indices: neuron, physical time, and
input/example. The intended extension is to approximate the sample index
by a small shared family of functions, then compress time and neurons on
that representation. A compact list of representative samples is one
possible implementation, not the definition of the third axis.

At fixed nonzero label scale, width, accuracy, depth and quantitative data
regularity, the sample contribution to retained storage should be bounded
independently of m. Ideally the constants also preserve the existing width
rates. Both fixed and moving storage count. Initialization may read the data;
runtime may not retain a full-data oracle or an m-by-R sampled basis matrix.
The comparison remains to the same-initialization dense trajectory, with the
same time/query domain, not merely to ground-truth labels.

The dense normalization is the current paper's: z^(1)=W^(1)x/sqrt(d),
z^(ell)=W^(ell)h^(ell-1), h^(ell)=phi_ell(z^(ell)),
f=w^T h^(L)/n, loss m^(-1)sum_a(f(x_a)-y_a)^2, and block mobilities
(n,1,...,1,n). Here delta^(ell)=n partial(f)/partial(z^(ell)) is
residual-free. The hidden-update factor below uses precisely this convention.

## 1. An exact cancellation in the sample direction

For this section write <u,v>_m=m^{-1}sum_a u_a v_a, with componentwise
interpretation for vector-valued u,v. Let psi_1,...,psi_R be fixed sample
functions orthonormal for this inner product, and let P denote their
orthogonal projector, acting independently on each neuron coordinate.
Consider one hidden interface, suppressing its layer index, and put
b_a=r_a delta_a. This is the residual-weighted backward response, not the
residual-free response delta_a. The canonical dense update is

\[
 \dot W=-\frac2n\frac1m\sum_a b_a h_a^\top.
\]

Define h_j=<psi_j,h>_m and b_j=<psi_j,b>_m. Orthogonality gives exactly

\[
 \frac1m\sum_a b_a h_a^\top
 =\sum_{j=1}^R b_jh_j^\top
 +\frac1m\sum_a ((I-P)b)_a((I-P)h)_a^\top.       \tag{1}
\]

Indeed write each response as its projection plus its orthogonal tail;
both cross terms vanish componentwise. Cauchy--Schwarz consequently bounds
the Frobenius norm of the omitted interaction by

\[
 \left(\frac1m\sum_a\|((I-P)b)_a\|^2\right)^{1/2}
 \left(\frac1m\sum_a\|((I-P)h)_a\|^2\right)^{1/2}. \tag{2}
\]

This is a product of tails, not a sum. It explains why sample compression
can inherit the same structural advantage as temporal orthogonal
projection. It does not prove that either tail is small along training.

For Legendre put rho=||r||_2/sqrt(m) and
tau(t)=1+integral_0^t rho(s)ds. Use the clock history
b_a(tau(t))=(r_a(t)/rho(t))delta_a(t) while rho>0. On the prefix
[0,1], put b=0 and h equal to the initialized feature. At residual zero
all physical velocities vanish and stationary continuation is used; any
value assigned to b at the final clock endpoint is irrelevant to its
integrals. Physical moment writes involve r delta, not residual division.
Fixed sample projection and time projection commute. Their product is an
orthogonal projector under empirical sample measure times the unnormalized
clock measure dxi on [0,tau], so the same componentwise argument applies
to the integrated weight increment. In the paper's unnormalized Legendre
moments, bar h_{i,j}=integral_0^tau P_j(2xi/tau-1)h_i(xi)dxi
and likewise for bar delta using b_i, the retained increment is

\[
 -\frac{2}{n\tau}\sum_{i=1}^R\sum_{j=0}^{q-1}
 (2j+1)\bar\delta_{i,j}\bar h_{i,j}^\top.
\]

This follows from the squared Legendre norm tau/(2j+1).
The sample/time memory count becomes 2(L-1)n R q. First-layer weights,
readout, scalar clock and fixed dense mixers remain. This is an algebraic
inventory, not an optimized-error theorem.

If one instead projects r, delta and h separately, the retained update
uses triple moments <psi_i psi_j psi_k>_m. Its discrepancy is not generally
the product of two tails: errors in each separate factor contribute.
The joint residual-weighted backward field is the natural object in (1).

## 2. How structure can bound the sample rank

These are approximation statements about a shared family of functions,
not assumptions about labels alone. They must cover the necessary forward
responses and residual-weighted backward responses, at all relevant layers,
neurons and times, in the norm being used. The constants in that family
bound must themselves be uniform in m.

**Lipschitz latent geometry.** Suppose normalized inputs come from a compact
k-dimensional Lipschitz image, and every required response is uniformly
Lipschitz in the observed inputs with a known bound. An observed-input
cover and its cluster-indicator basis approximate the entire family.
Its rank at error eta is at most C eta^(-k), independently of m. The
generator and latent coordinates need not be known to construct the cover.
The constant depends on the size/Lipschitz bound of the latent image and
the response regularity. Residual-weighted responses additionally require
label regularity, or a separate force/mean-label treatment as in RESULT.
This is a genuine common sample-space approximation; its lowest-order
closed implementation is weighted grouping.

**Analytic latent responses.** A stronger assumption yields a much sharper
rank. For example, suppose each required response is a vector-valued
holomorphic function of z in a polydisk |z_j|<rho, rho>1, bounded in norm
by B, with observed coordinates in [-1,1]^k. Use a common rho and B for
the entire response family and actual trajectories. Cauchy's coefficient
formula gives ||c_alpha||<=B rho^(-|alpha|). Keeping powers below K in
each variable leaves the uniform tail

\[
 \left\|\sum_{\max_j\alpha_j\ge K}c_\alpha z^\alpha\right\|
 \le kB\rho^{-K}(1-\rho^{-1})^{-k}.             \tag{3}
\]

To verify the bound, union over the k possible indices whose power is at
least K and sum the k geometric series; overlaps only increase the upper
bound. There are K^k retained monomials. Thus a sample space of dimension

\[
 R\le C[\log(C/\eta)]^k                         \tag{4}
\]

suffices uniformly over all observed samples. Dependencies of C include
k,B,rho, not m. Linear dependence among sampled monomials only decreases
dimension. A uniform approximation also gives empirical L2 approximation
without assumptions on empirical sampling density.

This explicit sufficient condition is not implied by a merely Lipschitz
latent map. Nor does the existence of analytic latent coordinates give an
algorithm access to them. An accessible chart/basis or a separate recovery
theorem is needed to implement this sharper representation. A Lipschitz
image alone supports the preceding covering route, not (4).

**Sphere harmonics.** A common uniformly decaying harmonic tail for the
response family supplies the analogous sample space, with dimension of
order K^(d-1) through degree K at fixed d. Tail control only in population
L2 is insufficient for arbitrary empirical measures or sphere-supremum
accuracy. Label bandwidth can reduce the actively excited response modes
when the dynamics preserve or weakly couple those modes; it does not by
itself imply common response tails.

At fixed eta all these ranks are O(1) in m. If a separate goal imposes
eta=m^(-c), (4) becomes O((log m)^k), while the Lipschitz rank becomes a
power of m. This explains the distinction between fixed-accuracy sample
compression and accuracy improving with the number of samples. Translating
eta into prediction error additionally requires a propagation bound.

## 3. Closure and retained information

A rank representation is not a runtime. Projected nonlinearities and
sample contractions must be evaluated from retained information.

One direct construction stores input/label coefficients and empirical
product moments of basis functions. Polynomial nonlinear maps then use
finite tensor contractions. The route note TENSOR_ROUTE supplies a
quadratic example with fixed storage O(dR+R^3), excluding network weights
and the basis evaluator. The reduced network is trained by the actual
gradient of its coefficient-space squared loss, so its own energy identity
is exact. It is a changed approximation architecture, not an identity for
the original nonpolynomial network.

For general analytic activations one can approximate the activation and
its derivative on a controlled preactivation range, or use compact positive
cubature to evaluate the nonlinear integrals. The nonlinear order and
quadrature storage must be counted; sample rank R alone does not determine
them. Derivative accuracy, persistence of the preactivation range, and
training comparison require their own proof. Retaining an unspecified
integration oracle would not close the construction.

Cluster-indicator functions are a useful exact special case: functions
constant on each cluster form an algebra, so componentwise nonlinearities
remain in that space. Its finite representation is weighted representative
training. Higher spatial modes offer greater accuracy per retained mode
but require product tensors or quadrature. Thus grouping and spectral
sample compression are two resolutions of the same representation idea.

## 4. Why a full minimum gap is not the right target

The diagnostic result in MODAL_ROUTE concerns a prescribed PSD residual
generator with common eigenfunctions and zero initial output. It is not
a substituted model for the paper. Each label coefficient evolves by a
factor between zero and one. Dropping modes whose label coefficient tail
has norm at most eta then changes the prediction by at most eta for all
time in empirical RMS, with no minimum eigenvalue assumption. A weighted
coefficient-tail bound gives a corresponding input supremum statement.

The message is positive: a weakly damped mode need not matter merely
because it exists. Its excitation and feedback matter. For nonlinear
feature learning, modes can mix and the residual operator changes between
the dense and reduced trajectories. A useful proof target is a bound on
the time-integrated omitted force/coupling, not a lower bound on every
sample direction. The modal route states such a conditional contraction
estimate; it does not supply an autonomous neural closure or control the
operator mismatch produced by changing the trajectory.

This refines the previous stability discussion: resolved-space coercivity
is one sufficient route, not a universally necessary condition. The
paper's full-gap label cap is not a lower bound ruling out sample
compression and should not be used to shrink labels toward zero.

## 5. Relation to the current methods and remaining theorem

- Legendre can replace separate sample histories by shared sample/time
  coefficients, using (1). Its temporal basis need not become data-dependent,
  although the additional sample representation generally is.
- Harmonic already shares spatial source coefficients but still preserves
  all exact training constraints and their Gram. A genuine sample extension
  would preserve a small set of residual moments instead, and use compact
  moment integration to evaluate the updates. A full m-dimensional inverse
  or deficit must not remain hidden in the inventory.
- Taylor can replace separately indexed input curves by a shared sample
  basis before temporal approximation. Its passive-query family must also
  have a compact representation on the promised support/panel; otherwise
  the retained query list still scales with m. Unseen-support guarantees
  require a compact evaluable basis and support coverage, not latent access.

The intended new theorem would bound retained coordinates by a function of
width, accuracy and quantitative data/response complexity, independent of m,
while approximating the full nonlinear trajectory on the agreed query
domain. Identities (1)--(2), the sufficient rank estimate (3)--(4), and the
finite-tensor construction establish useful parts of this program.
The missing implication is from meaningful initial data/label conditions
to uniformly controlled nonlinear response tails, a closed low-cost runtime,
and all-time transport of its error with width-compatible constants.
No optimized combined storage exponent for Legendre, Harmonic or Taylor
is claimed here. No paper changes or experiments were made.
