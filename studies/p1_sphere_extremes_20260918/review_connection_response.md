# Independent review: conditional first input response and transport

2026-09-18. Isolated mathematical review. No experiment, external retrieval,
study history, README, other study, or other review was consulted. The
solve-math-rigorously and investigate-conjectures skills and the latter's
research-contract and adversarial-audit instructions were read. Only this
report was written.

## Verdict and exact scope

**PASS for the conditional unbounded-first-response theorem, the
companion's necessary transport, nonintegrable state-distance, and
delayed-exit estimates, and the elementary logical counterexample.** These results
do not establish almost-sure nonlinear escape, exclusion of nearby bad
endpoints, or convergence to zero loss. The difference between these
conclusions is substantive, and the response theorem states it correctly.

The response theorem applies to the exact canonical dimension-three p=1
population equations in the odd invariant sector, with the retained
nonconstant feature vectors, the physical population-L2/Frobenius metric,
all matrix entries, the fixed Gaussian carriers and initialization, and
the stated seven equally weighted triangle/square inputs. The actual lower
endpoint is `w_*=a sign(q·b1)e1`, where `a>0` and `q` is a nonzero vector
in the nonconstant lower feature space. The upper endpoint is a bounded odd
function of the first upper coordinate satisfying the two displayed
readout constraints. **Strong convergence of this particular canonical
trajectory to this particular endpoint is an assumption**, not a result.
For each tangent input direction with `Delta != 0`, the derivative at zero
noise exists on every finite time interval and is unbounded as time ranges
over `[0,infinity)`. Genericity means Lebesgue-almost-every direction in the
14-dimensional product tangent space, or any absolutely continuous law
there. It does not mean a probability assertion at fixed nonzero noise.

The companion transport conclusion assumes a bounded actual lower endpoint
and strong convergence of the complete physical state. Its delayed-exit
conclusion assumes strong convergence of the base trajectory, fixes a
positive endpoint-ball radius and a sufficiently late entrance time, and
allows all sufficiently small input perturbations with labels and masses
unchanged. The lower bound remains valid with infinite exit time.

The companion's secondary reflection inequality is verified conditionally
on the endpoint properties stated in that section. The existence and size
of its named continuation branches are not certified by this packet;
their complete constructions were not assigned and were not retrieved.
They are not used by any of the three conclusions above.

## Independent derivation checks

### 1. Stationarity, genuine Hilbert Hessian, and cancellation

The residual weights at the reference state are `-8/49` on the three
positive labels and `6/49` on the four negative labels. The two angular
groups have equal normalized first and second angular moments. Therefore

\[
 \sum_i\rho_i=0,\qquad
 \sum_i\rho_i u_i=0,\qquad
 \sum_i\rho_i u_i u_i^T=0,
 \qquad u_i=x_i/\sqrt3.
\]

The first upper backward coordinate vanishes by `E[c_*J]=0`; the other
coordinates vanish by independence and centering. Thus `d_i=0`, all lower
and matrix velocities vanish, and the readout velocity vanishes because
the residuals sum to zero. The loss is
`(3(8/7)^2+4(6/7)^2)/7=48/49`.

For a state direction `(h,k,N)`,

\[
 \delta a_i=\phi'(aC)E[b_1h^T]u_i,
 \qquad
 \delta v_i=N\phi(aC)A+M_*\delta a_i.
\]

In particular `delta v_i` is affine in `u_i`, and every first prediction
variation is the common value `E[kH]`. The residual-weighted second
prediction variation consists of a term linear in `delta v_i`, a term
quadratic in `delta v_i`, and a term multiplied by `d_i=0`. The three
moment cancellations above remove all of it. The remaining loss Hessian
is exactly `2(E[kH])^2`, with no omitted lower or matrix directions.

This is a derivative in the stated Hilbert norm, not merely a formal
quadratic form on bounded perturbations. The lower finite moment map has
a quadratic Taylor remainder bounded by a constant times `||h||_2^2`.
Every lower local gate change in the field multiplies a finite coefficient
vanishing at the reference state. Its L2 Lipschitz bound times that
coefficient is quadratic in the state increment. The remaining maps are
finite-dimensional smooth operations or L2 pairings. Consequently the
gradient field is Fréchet differentiable at the endpoint, with

\[
 A_*(h,k,N)=(0,-2H E[kH],0).
\]

The H,J independence proof is correct: comparing the first and third
Taylor coefficients in `t phi'(zt)=beta phi(zt)` gives incompatible values
when `z>0`. The upper coordinate has positive density on an interval.
Consequently their two-function Gram matrix is positive definite. A linear
combination of H and J supplies a bounded odd readout satisfying both
constraints; existence need not be imported from the older construction.
Likewise the nonconstant lower features have no nontrivial almost-sure
linear relation: conditional reverse Gaussian randomness prevents a
linear relation involving a k-coordinate, and the remaining independent
h-coordinates are nondegenerate. Hence `kappa>0` for every stated nonzero q.

### 2. Finite-time physical differentiation

The complete field is locally Lipschitz jointly in physical state and
finite-dimensional input coordinates on bounded sets. For the lower
features and gates this follows from bounded derivatives of tanh and

\[
 \|w\cdot u-\widetilde w\cdot\widetilde u\|_2
 \le |u|\|w-\widetilde w\|_2
       +|u-\widetilde u|\|\widetilde w\|_2.
\]

Bounded feature marks, finite matrix dimensions, and Cauchy--Schwarz then
control the upper moments and all three field blocks. In the affine
coordinate `w-g`, the needed bound is on `||w||_2`, not on `||g||_infinity`.

For a fixed physical direction the lower argument derivative lies in L2.
The corresponding gate difference quotient is dominated by a constant
times `|h|+|w||xi|`, with the appropriate fixed input factors. Dominated
convergence proves strong directional differentiation. The state
derivatives are bounded linear operators on each bounded set; no false
claim of general Fréchet differentiability of the lower Nemytskii gate on
L2 is required.

For completeness, the integral-remainder version of the proof is enough
even without a general compact-cover differentiability theorem. Solve
the bounded-operator linear integral equation for Z on a finite interval.
Evaluate the directional remainder at the fixed path `theta(t)+epsilon
Z(t)` and the input path. It tends to zero at every fixed t and has a
uniform integrable bound from local Lipschitzness and boundedness of the
paths. Dominated convergence makes its time integral tend to zero. The
remaining difference is bounded by the field's Lipschitz constant times
the error integral; Gronwall gives convergence of the actual difference
quotients uniformly on that finite interval. The spherical chart differs
from its tangent linear path by `O(epsilon^2)`, which does not affect this
argument. The initial derivative is zero because the carriers and
canonical state are unchanged.

There is no finite-time existence gap. The exact gradient identity and
initial loss one imply the companion's polynomial bounds on c, M, and
the lower displacement. They preclude finite-time Hilbert-norm blowup
and allow local solutions to continue for every finite time.

### 3. Operator convergence and the neutral force

The potentially problematic state derivative is the lower multiplication
operator containing `phi''(w·u_i)(h·u_i)b1^T M^T d_i`. Its operator norm
is bounded by a fixed constant times `max_i|d_i|` on the convergent state
trajectory and tends to zero. Every other derivative contribution has
finite rank. Its lower representing functions converge in L2, its upper
functions converge uniformly because their arguments are finite vectors
and marks are bounded, and its c-pairings converge by Cauchy--Schwarz.
This proves convergence to A_* in operator norm, rather than only strong
operator convergence.

For the input derivative, the additional factor w converges strongly in
L2. Products with bounded continuous gate factors converge in L2 by
first subtracting `w-w_*` and then applying bounded dominated convergence
to the fixed `|w_*|^2` weight (or to subsequences). Thus `B(t)->B_*`
strongly in the physical Hilbert space.

At the endpoint the fixed-state input derivative of every prediction is
zero because `d_i=0`. Direct differentiation gives

\[
 (B_*)_c=-2a\kappa\phi'(aC)\Delta J.
\]

Set `k=J-<J,H>H/||H||_2^2`. This is a nonzero bounded odd readout
direction, belongs to the physical state space, and is orthogonal to H.
For `K=(0,k,0)`, A_* is self-adjoint and annihilates K, while

\[
 \langle K,B_*\rangle
 =-2a\kappa\phi'(aC)\Delta\|k\|_2^2\ne0.
\]

If Z were bounded on the whole half-line, the derivative of `<K,Z>`
would converge to this nonzero scalar because `A(t)->A_*` in operator
norm and `B(t)->B_*`. Eventually it has a fixed sign and is bounded away
from zero, contradicting boundedness. This proves unboundedness of Z;
it does not prove a linear growth rate for the actual unbounded Z.

The tangent direction supported at one sample with
`xi_i=e1-(x_i,1/3)x_i` has first coordinate `S^2>0`; its residual weight
is nonzero. Thus Delta is a nonzero linear functional and its kernel is
a codimension-one null set. Finally, a uniform-in-time O(|epsilon|)
state-displacement bound would bound every finite-time derivative and
is excluded. The stated order “choose a finite time, then take noise
sufficiently small” is justified.

### 4. Transport and exit delay

With `B_l=ess sup |b_l|`, loss dissipation and the exact equations give

\[
 \|c(t)\|_2\le2t,\qquad
 \|M(t)\|_F\le\|D\|_F+2B_1B_2t^2,
\]
\[
 \|w(t)-g\|_\infty
 \le 2B_1B_2\|D\|_Ft^2+2(B_1B_2)^2t^4.
\]

All constants and powers in the companion are correct. If `|w_*|<=R`,
then `|w(t)-w_*| >= (|g|-K(t)-R)_+` pointwise, where
`K(t)=||w(t)-g||_infinity`. The Gaussian tail has strictly positive
second moment beyond every fixed finite threshold. Strong L2 convergence
therefore forces `K(t)->infinity`, not merely an unbounded subsequence.
The accumulated L-infinity velocity and its coefficient envelope must
diverge. Strong convergence of the full state bounds M for all time;
the displayed envelope inequality then forces
`integral_0^infinity max_i|d_i(t)| dt=infinity`. No independence between
g and b1 is used. Vanishing d_i at the endpoint is compatible with this
necessary nonintegrability.

For the exit estimate, local Lipschitz continuity first gives
`e(T)<=C_T delta` on a bounded finite-time tube; smallness of delta closes
the tube. Until the first exit from the radius-r endpoint ball,

\[
 e(t)\le\delta[(C_T+1)e^{C(t-T)}-1].
\]

The reference trajectory remains within r/4 after T. At a finite exit,
`e(tau)>=3r/4`, giving exactly the stated logarithmic lower bound. The
constants are uniform over sufficiently small data perturbations, and
no convergence or endpoint continuity of the perturbed trajectory is
assumed. A never-exiting trajectory satisfies the bound trivially.

The appended Section 6 was read completely after the initial companion
packet was frozen. It also passes. Subtracting `v_i=M a_i` and `d_i` at
the endpoint gives the displayed Lipschitz estimates (21)--(22), using
only unit input norms, bounded marks, bounded tanh derivatives, and
`c_* in L2`. When every `d_i,*=0`, these imply

\[
 \max_i|d_i(t)|\le C\|\theta(t)-\theta_*\|_{\mathcal H}
\]

on the trajectory tail. Finite-time continuity makes the omitted prefix
integrable. Divergence of the d_i envelope therefore forces divergence
of the time integral of physical state distance. This excludes every
integrable upper envelope, including exponential decay and
`O(t^(-1-eta))` for `eta>0`, while giving neither a pointwise lower rate
nor a restriction on exponential loss convergence. Boundedness of the
actual lower endpoint and vanishing d_i are essential stated hypotheses
for this consequence of the transport argument.

### 5. Secondary reflection section: verified and missing inputs

For the stated coordinate reflection, the canonical nonconstant feature
law and matrix satisfy the asserted transformation rules. The induced
map is a Hilbert isometry, fixes initialization, and preserves the loss
when the data are invariant under the corresponding same-label
permutation. Uniqueness keeps the trajectory in its closed fixed space.

If the proposed endpoint's lower field is independent of the reflected
Gaussian coordinates, while its c and M are fixed, then the component
orthogonal to that fixed space is exactly `(w_*)_3 e3`. The distance
inequality is therefore correct. Strict positivity requires the stated
nonzero transverse field on positive mass. The sharper
`Theta(epsilon^(1/3))` estimate additionally requires the asserted branch
sizes and uniformly positive masses. Those construction facts are absent
from the frozen packet and remain outside this independent certification.

## Remaining implication gap

The separately assigned elementary example passes a complete independent
check. Its `V_epsilon` has global minimum
`1-3|epsilon|^(4/3)/4>1/4` for `|epsilon|<1`, so the displayed predictions
are real analytic and give exactly the stated equal-mass square loss.
The gradient equations are correct. The plane q=0 is invariant by
uniqueness, and initialization `(1,0,0)` remains on it. Monotonicity and
uniqueness in `z'=epsilon-z^3` give convergence to the real cube root and
global boundedness of these initialized paths. Thus the endpoint loss is
strictly positive for every parameter, while zero-loss states exist at
`a=0,q=1`.

The equilibrium Hessian is `diag(1,3|epsilon|^(2/3),0)`; its q-direction
has negative cubic loss change despite nonnegative quadratic curvature.
The unperturbed connection is nonstationary because `a=e^(-t)`.
Differentiation at zero gives `Z_z'=1`, so `Z_z=t`, while the exact
all-time state displacement is `|epsilon|^(1/3)`. Every stated feature
is therefore compatible with persistence of a bad connection under all
small parameter changes. This is a counterexample to the general logical
implication under discussion, **not** a counterexample in the canonical
p=1 closure. The parameter-invariant plane explains why no conclusion
about that closure can be transferred from this example alone.

The strongest surviving alternative is that a generic perturbed canonical
trajectory remains near the bad set and converges to a bad equilibrium
whose displacement from the original one is larger than linear in noise
but still tends to zero. Unbounded first response does not exclude this.
The companion establishes a necessary delay for escape, not escape.
Neither a finite-dimensional strict-saddle statement nor nullity in
ambient state space supplies a measure statement for the specified
canonical data-dependent trajectory without an additional argument.

No fatal or major gap was found in the scoped conclusions. The
central nonlinear escape question remains unresolved, rather than
negatively answered.

## Integrated synthesis check

The subsequently assigned `INPUT_CONNECTION_RESULTS.md` was read in full.
Its statement of the response theorem, genericity in tangent directions,
restriction to the original single-amplitude endpoint, interpretation of
the elementary example, necessary transport restriction, conditional exit
delay, and remaining nonlinear question faithfully match the reviewed
claims. Its transversality discussion is identified here only as a
summary of another route: the complete `input_basin_transverse.md` was
not read, and this report does not independently certify that route's
trapping graph or transversality theorem. The synthesis correctly does
not assert that its nonzero transverse derivative has been established
for the specified canonical connection.

## Complete read coverage and frozen identities

The complete canonical document was read as the assigned definition of
the exact model; its linked derivations were not followed. The response
and companion documents were read in full, including their limitations
and the secondary reflection section. The complete revised response was
read again after its feature dimensions and directional-continuity
argument were clarified. The subsequently assigned elementary example
was also read in full, as was the complete integrated synthesis after its
exit-time statement was made precise. The companion's entire Section 6
addendum was read, and the SHA256 of its unchanged first 394 lines was
checked against the original frozen companion hash. Scientific inputs not
supplied in the packet were not fetched.

| Complete assigned file | Read coverage | Final SHA256 |
|---|---:|---|
| `docs/observable_p1.md` | 332/332 lines | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `studies/p1_sphere_extremes_20260918/input_connection_response.md` | 344/344 lines | `39a3f5a854c34484132a3dde17f8be2c062c73c8a136fc2f5adbc82ac2096437` |
| `studies/p1_sphere_extremes_20260918/input_connection_response_example.md` | 97/97 lines | `43e57ae8583c1705efcfc801481ba667c0ffe3d01d134ccf59d655e4ff0f8377` |
| `studies/p1_sphere_extremes_20260918/canonical_bad_reach.md` | 465/465 lines | `7f6bbf6b8ce247ecf54474a240673dbaac06a902204452ddbe7b8c2e3dcafa73` |
| `studies/p1_sphere_extremes_20260918/INPUT_CONNECTION_RESULTS.md` | 161/161 lines | `3632c5c0b74c66d3cbe4f034123e22f43510f1e58bfa2c5101cd5d7b23a86982` |

The original companion prefix hash is
`d860ca85798fb46a5c5a011d41e14f3afc3c6ce6da67c05a3b1ee68502174b87`.
This review provides an independent internal mathematical check with the
stated coverage limitations; it is not approval to promote material.
