# Coordinate reference and the open-family bottleneck

Date: 2026-09-18. Scoped route: `p1_open_family`.
Status: frozen independent theoretical route; internally checked only.
No experiment, numerical integration, or numerical coefficient evaluation was
performed. This file does **not** establish an unconditional convergence
theorem for a genuine three-direction data set.

## Scope and result

The intended target is an open set of three pairwise nonparallel unit
directions, with labels `(1,1,-1)` and positive masses
`(q/2,(1-q)/2,1/2)`, for which the exact canonical full p=1 population
gradient flow converges to zero loss without any assumed trajectory bound,
kernel gap, or endpoint regularity. Initialization, ridge, correlated lower
marks, physical metric, and all three moving blocks are unchanged.

Scientific inputs read were the complete `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10.D.3, and the complete
`initial_geometry.md` and `stationary_geometry.md` in this study. Required
research and rigorous-mathematics skills, including the research contract
and adversarial-audit instructions, were read. No other study or parallel
route was consulted before freezing this file.

The positive result below is an exact, globally convergent coordinate-axis
reference with a finite regular **one-output** endpoint. It is not a
substitute for the genuine-triple target. Its main additional use is to
make the missing perturbation step explicit.

## 1. An exactly solvable canonical reference

By input oddness, the data law with all signed directions `y_i u_i=e_1`
has exactly the same loss and vector field as the one-atom law
`(u,y)=(e_1,1)`, irrespective of its masses. In particular this is the
collapsed boundary of the requested label/mass family.

Write the two lower coordinate blocks as

\[
 \xi_j=\left(h_j/a_*,\ (k_j-\beta h_j/(v+\eta))/b_*\right)
       \in\mathbb R^2,\qquad j=1,2,
\]

and the upper coordinates as `b=(b_1,b_2)=H/c_*`. The order of the four
active lower coordinates is immaterial provided the matrix is reordered
with them. The initializer has two identical diagonal rows
`m_0=(d_h,d_k)`. At the axis reference, the following form is invariant:

\[
 w=(v(G_1,Z_1),G_2),\qquad
 M=\begin{pmatrix}m&0\\0&m_0\end{pmatrix},\qquad
 c=c(b_1).
 \tag{1}
\]

Here `v` is the moving first coordinate, not the initializer's scalar
variance constant. To avoid confusion below, denote this moving coordinate
by `V`. The lower input coefficient is `(a,0)`, where

\[
 a=E[\xi_1\tanh V]\in\mathbb R^2,
 \qquad z=m\cdot a,
 \qquad f=E[c(b_1)\tanh(b_1z)].
 \tag{2}
\]

Indeed the other lower coordinate block is independent and centered; the
upper second coordinate is independent and centered. Every undesired
coefficient and velocity therefore vanishes by direct integration.
The exact full canonical equations preserve (1), so uniqueness identifies
this restricted calculation with the full trajectory. This is an invariant
reference calculation, not an imposed diagonal constraint on general data.

Let

\[
 d=E[b_1c(b_1)\operatorname{sech}^2(b_1z)],
 \qquad B=E[\xi_1\xi_1^T\operatorname{sech}^4 V].
 \tag{3}
\]

At initialization `z=z_0>0`: this is `F(1)>0` in
`initial_geometry.md`, and can also be checked from the two strictly
positive initial components

\[
 a_0=\left(v/a_*,\ \beta\eta/((v+\eta)b_*)\right),
 \qquad m_0=(d_h,d_k)>0.
 \tag{4}
\]

Consider first the following autonomous auxiliary clock `s`, with the same
initial state:

\[
 c_s=\tanh(b_1z),\qquad m_s=da,\qquad
 V_s=d(m\cdot\xi_1)\operatorname{sech}^2V.
 \tag{5}
\]

It is precisely gradient ascent of the scalar prediction `f` in the
physical block metric. It exists on every finite `s` interval. For a direct
continuation bound, `|a|<=1` and `E b_1^2<=1` follow from the canonical
feature-contraction bounds. Thus

\[
 \|c(s)\|_\infty\le s,\quad |d(s)|\le s,
 \quad |m(s)|\le |m_0|+s^2/2,
\]
\[
 \|V(s)-G_1\|_\infty
 \le \|\xi_1\|_\infty\left(|m_0|s^2/2+s^4/8\right).
 \tag{6}
\]

The bounded tanh derivatives make the vector field locally Lipschitz in
these norms. The bounds prevent finite-clock escape, exactly as in the
fixed-order characteristic continuation argument of the supplied source.

Differentiate (2) using (5):

\[
 a_s=dBm,\qquad z_s=d\bigl(|a|^2+m^TBm\bigr).
 \tag{7}
\]

As long as `z>0`, the integral formula for `c` in (5) shows that
`b_1 c(b_1)>=0`. Thus `d>=0` and (7) makes `z` nondecreasing. Since
`z_0>0`, a first-exit argument gives

\[
 z(s)\ge z_0>0,\quad b_1c(s,b_1)>0\ (s>0,\ b_1\ne0),
 \quad d(s)>0\ (s>0).
 \tag{8}
\]

The positivity of `d` uses the nondegenerate continuous upper coordinate
law and the strictly positive gate. No positivity of every component of
`a` or `m` is needed.

The scalar prediction derivative is

\[
 f_s=E\tanh^2(b_1z)+d^2\bigl(|a|^2+m^TBm\bigr)
       \ge \kappa,
 \qquad \kappa:=E\tanh^2(b_1z_0)>0.
 \tag{9}
\]

The first term is bounded below because `z>=z_0` and `tanh^2` increases
with the absolute value of its argument. Since `f(0)=0`, there is a
unique first `s_* in (0,1/kappa]` with `f(s_*)=1`. Bounds (6) make the
entire state finite at this endpoint; in particular `V-G_1` and `c` are
bounded. The scalar prediction differential is nonzero there, already
because its readout component has squared norm at least `kappa`.

## 2. Return to physical time and genuine feature motion

For `0<=s<s_*` put

\[
 t(s)=\int_0^s\frac{d\sigma}{2(1-f(\sigma))}.
 \tag{10}
\]

The denominator is positive, so `t` increases. On the compact clock
interval `[0,s_*]`, the continuous derivative `f_s` has a finite upper
bound `C`. Consequently

\[
 1-f(s)=\int_s^{s_*}f_\sigma\,d\sigma
       \le C(s_*-s),
\]

which makes `t(s)` tend to infinity. Its inverse `s(t)` satisfies
`s_t=2(1-f)`. Substituting this into (5) gives exactly the canonical
negative gradient flow of `(f-1)^2`, including its factor two and all
three physical block metrics. Uniqueness therefore identifies it with the
prescribed physical trajectory for every finite `t`.

Writing `e=1-f`, equations (9)--(10) give

\[
 e_t=-2 f_s e\le-2\kappa e,
 \quad 0<e(t)\le e^{-2\kappa t},
 \quad \mathcal L(t)\le e^{-4\kappa t}.
 \tag{11}
\]

The whole state converges in the bounded-displacement/readout/Frobenius
norms to its finite clock endpoint. In fact

\[
 s_*-s(t)\le e(t)/\kappa,
\]

and the bounded clock velocities in (5) transfer the same exponential
rate, with finite constants, to those state norms.

All three trained blocks move. The readout clock velocity is nonzero by
`z>0`. Also

\[
 (|m|^2)_s=2dz>0\qquad(s>0).
\]

Finally `m` is nonzero, the law of `xi_1` has a positive density on an open
set, and `sech^2 V` is strictly positive at every finite mark. Hence
`V_s` has nonzero population norm whenever `s>0`. This proves actual
first-layer motion, not only motion in the middle/readout blocks. The
untrained second coordinate in this special reference is allowed by the
full equation's invariant symmetry.

## 3. What a regular genuine reference would imply

For clarity, the desired openness step itself has the following valid
local form. Suppose a genuine-triple canonical trajectory converges to a
finite state `theta_*` in the norm

\[
 \|\delta\theta\|_X
  =\|\delta w\|_2+\|\delta c\|_\infty+|\delta M|_F,
 \tag{12}
\]

with zero loss and a surjective differential of its three weighted
predictions. Then there is an open neighborhood of its directions and
positive masses whose canonical trajectories all converge to finite
zero-loss states.

Here is the mechanism, stated to expose rather than assume its hypotheses.
Let `rho_i=sqrt(mu_i)(f_i-y_i)` and let `K` be the physical Gram of the
differentials of `sqrt(mu_i) f_i`. Surjectivity at `theta_*` gives
`K(theta_*)>=2k I` for some `k>0`. On a sufficiently small `X` ball and
small data neighborhood, bounded features and tanh derivatives give
`K>=k I` and

\[
 \mathcal L'=-4\rho^T K\rho\le-4k\mathcal L,
 \qquad \|\theta'\|_X\le C\sqrt{\mathcal L}.
 \tag{13}
\]

These estimates are legitimate in (12): the row gate is Lipschitz in
`L^2`, its backward coefficient is bounded, and the readout velocity is
bounded in supremum norm by the sum of residual magnitudes. The matrix
velocity has the same bound. The finite prediction Gram is continuous
in this norm. Direction variation is controlled using `w in L^2`, not
an invalid supremum bound on the unbounded Gaussian initial row.

If the trajectory enters the smaller concentric ball with sufficiently
small loss, integration of (13) gives remaining `X` path length at most
`C sqrt(L)/(2k)`, smaller than the distance to the ball boundary.
A first-exit argument therefore keeps it in the ball, proves exponential
loss decay, and gives a Cauchy state endpoint. Finite-time continuous
dependence of the characteristic equation, in (12) and the data
parameters, places all sufficiently close canonical data trajectories
inside this same entrance condition. This proves the stated local
openness implication.

The coordinate reference in Sections 1--2 does **not** satisfy this
three-output surjectivity hypothesis. At coincident signed directions,
the three prediction rows are proportional for every state.

## 4. The unresolved split modes

The following elementary scaling check prevents an invalid continuity
argument. At a fixed bounded-displacement reference state consider three
signed directions

\[
 v_i(\varepsilon)=(\cos(\varepsilon a_i),
                       \sin(\varepsilon a_i)),
 \qquad a_1,a_2,a_3\text{ distinct and fixed}.
 \tag{14}
\]

For the upper readout features `T(theta,b)=tanh(b dot z(theta))`, the
map `theta -> T(theta,.)` is twice continuously differentiable into
upper `L^2`. Gaussian initial rows plus bounded displacement supply all
needed moments for differentiation under the lower integrals.
Choose a nonzero coefficient vector `x` with
`sum x_i=sum x_i a_i=0`. Taylor expansion gives

\[
 \left\|\sum_i x_i T(\varepsilon a_i,\cdot)\right\|_2
       =O(\varepsilon^2),
\]

so the least eigenvalue of the unweighted readout Gram is at most
`C epsilon^4` for fixed normalized `x`. Positive fixed masses do not
change this order. The same cancellation applies to the full physical
prediction gradients, whose directional second derivatives lie in their
physical Hilbert spaces at a bounded-displacement state; hence its
least eigenvalue also has this upper bound.

At the axis endpoint the reflection symmetry makes the directional first
derivative of the prediction vanish. The split prediction errors are
therefore `O(epsilon^2)`, with a quadratic coefficient that this route
has not shown to vanish. If it is nonzero, their component in the
second-difference direction has order `epsilon^2`, the same order as
the corresponding gradient feature, and a correction need not tend to
zero in state norm. The local-basin length estimate in (13) is even
less useful because its denominator can shrink like `epsilon^4`.
These estimates identify a gap; they are not a lower bound on actual
training time or a proof that split data fail.

The exact initialized full Gram is positive for every fixed genuine
triple by `initial_geometry.md`. That qualitative fact does not supply
a uniform perturbation radius at the collapsed reference. Likewise,
the finite-state lower submersion and saddle classification in
`stationary_geometry.md` do not bound the split trajectory for all time.

## 5. Frozen conclusion

Proved here: an unconditional canonical coordinate-axis reference has
exponentially vanishing loss, a finite bounded-displacement endpoint,
nonzero motion of each trained block, and a nonzero scalar prediction
differential. Also proved: a finite regular zero-loss endpoint for a
genuine reference would yield an open family by a direct trapping
argument.

Unresolved: construct such a genuine reference, or control the singular
split modes from the coordinate reference without assuming a trajectory
bound or kernel gap. No theorem for an open family of genuine triples,
nor for the equilateral triple, is claimed by this route.

## 6. Bounded extension: radial convexity for a scalar readout objective

This section is a separately recorded extension after the initial freeze.
The supervisor supplied the candidate identity `c_ss=DH DH* c`; no other
route's report was read. The exact metric factors and consequences are
derived here. The genuine-triple target remains unchanged.

Let `x=(w,M)` be the hidden state, with physical `L2/Frobenius` metric.
Suppose a scalar prediction objective has the form

\[
 F(x,c)=\langle c,H(x)\rangle_{L^2(\Omega_2)}.
 \tag{15}
\]

Consider its signal-time gradient ascent

\[
 c_s=H(x),\qquad x_s=DH(x)^*c,
 \qquad c(0)=0.
 \tag{16}
\]

All derivatives below are evaluated along the bounded characteristic
solution, where the tanh derivatives and fixed feature envelopes justify
the chain rules. Put `kappa=||H(x(0))||_2^2>0`. Differentiating the first
equation in (16) gives

\[
 c_{ss}=DH(x)DH(x)^*c.
 \tag{17}
\]

For `q=||c||_2>0`,

\[
 q_{ss}
 =\frac{\|c_s\|_2^2-q_s^2+\langle c,c_{ss}\rangle}{q}
 =\frac{\|H\|_2^2-q_s^2+\|DH^*c\|^2}{q}\ge0.
 \tag{18}
\]

Cauchy--Schwarz gives `|q_s|<=||c_s||_2`. Also
`c(s)=sH(x(0))+o(s)`, so `q_s(0+)=sqrt(kappa)`. On the initially
nonzero interval (18) yields `q>=s sqrt(kappa)`; this prevents a later
zero and extends the argument throughout every finite existence interval.
Consequently

\[
 \|H(x(s))\|_2\ge q_s\ge\sqrt\kappa,
 \qquad F=q q_s,
 \qquad F_s=\|H\|_2^2+\|DH^*c\|^2\ge\kappa.
 \tag{19}
\]

Thus the individual readout feature norm need not be proved monotone.
The radial norm `q` supplies the needed lower bound.

For one arbitrary unit input take `H(x)=tanh(b_2^T M a(u))`.
For a signed equal-weight pair take
`H=(T_1-T_2)/2`, where `T_i=tanh(b_2^T M a(u_i))`.
In either case `||H||_infty<=1`, and the corresponding hidden velocities
satisfy

\[
 \|c(s)\|_\infty\le s,
 \|M(s)-D\|_F\le s^2/2,
 \|w(s)-g\|_\infty
 \le K_1\bigl(\|D\|_{op}s^2/2+s^4/8\bigr),
 \tag{20}
\]

with `K_1=||b_1||_infty`. For the pair, for example,
`M_s=(d_1a_1^T-d_2a_2^T)/2`; both `|a_i|<=1` and `|d_i|<=s`.
The first-layer estimate follows from the same half-weighted sum and
bounded features. These bounds prove finite-clock global existence.

If symmetry ensures that the physical loss equals `(F-1)^2` and its
full gradient equals `2(F-1) grad F` at every reached state, the clock
change of Section 2 applies verbatim. The resulting physical flow has a
finite endpoint, exponentially vanishing loss, and a nonzero scalar
prediction differential, with rate constant (19). This proves the
single-effective-direction statement for **every rotation**, using the
unchanged canonical initializer. It does not invoke rotation covariance
of that initializer.

## 7. An exact reflected pair with one scalar residual

Let `S` be a signed coordinate reflection, so `S^2=I`, `S` preserves
the initialized mark laws and intertwines `D`. Take distinct nonparallel
unit inputs `u_1` and `u_2=S u_1`, labels `(1,-1)`, and masses `(1/2,1/2)`.
For example, `S` may swap coordinates and
`u_1=(cos(theta),sin(theta))`, provided
`cos(theta)!=+/-sin(theta)`.

The transformation which reflects both mark spaces and the hidden state,
and also negates the readout, preserves these data and the full gradient
equations. The initial state is fixed. Uniqueness therefore gives

\[
 f(Su)=-f(u),\qquad f_2=-f_1.
 \tag{21}
\]

Set `F=(f_1-f_2)/2` and `H=(T_1-T_2)/2`. At every reached state,
`F=f_1`, and direct differentiation of the original unhalved loss gives

\[
 \mathcal L=\tfrac12(f_1-1)^2+\tfrac12(f_2+1)^2=(F-1)^2,
\]
\[
 \nabla\mathcal L
  =(F-1)(\nabla f_1-\nabla f_2)
  =2(F-1)\nabla F.
 \tag{22}
\]

Thus no unrecorded factor of two or rescaling of the restricted physical
metric occurs. The signal-time equations are exactly (16). Initial
upper-feature independence from `initial_geometry.md` gives
`kappa=||H(0)||_2^2>0`. Sections 6 and 2 now prove unconditional
exponential loss decay and convergence to a finite bounded-displacement
endpoint for this genuinely two-direction reference.

For the swapping example, the initial upper vectors are
`(F(cos(theta)),F(sin(theta)))` and the swapped vector. Their determinant
is nonzero because the scalar initialized `F` is odd and strictly
increasing, and `cos(theta)!=+/-sin(theta)`. Hence the initial lower
coefficient vectors `a_1,a_2` are linearly independent. The same holds
for a coordinate-sign reflection of a direction having two nonzero
coordinates.

All three trained blocks move near initialization. Write
`Delta=z_1(0)-z_2(0)`. Since `a_1,a_2` are independent, a matrix
variation can prescribe `delta z_1=Delta/2`, `delta z_2=-Delta/2`.
It gives

\[
 \delta H
 =\tfrac14(b_2\cdot\Delta)
       \{\operatorname{sech}^2(b_2\cdot z_1)
          +\operatorname{sech}^2(b_2\cdot z_2)\}.
 \tag{23}
\]

The initial `H` and `b_2 dot Delta` have the same sign, so
`<H,delta H>>0`. Thus `D_MH(0)^*H(0)!=0`, and (16) gives a nonzero
leading matrix velocity `s D_MH(0)^*H(0)+o(s)`.
Writing `d_i^0=E[b_2 H(0) sech^2(b_2 dot z_i(0))]`, (23) also shows
that the two `d_i^0` are not both zero. The leading first-layer velocity
is

\[
 \frac{s}{2}\left[
  (b_1\cdot D^T d_1^0)\operatorname{sech}^2(g\cdot u_1)u_1
 -(b_1\cdot D^T d_2^0)\operatorname{sech}^2(g\cdot u_2)u_2
 \right]+o(s)
 \tag{24}
\]

in population `L2`. If its coefficient vanished, independence of
`u_1,u_2`, positivity of the lower gates, the lower open feature density,
and injectivity of `D^T` would imply `d_1^0=d_2^0=0`, a contradiction.
The readout velocity is nonzero already at zero. The arbitrary rotated
single-input case also has nonzero hidden motion: its initial backward
coefficient `d^0` satisfies
`z_0 dot d^0=E[(b_2 dot z_0)tanh(b_2 dot z_0)sech^2(b_2 dot z_0)]>0`.

The scalar regularity furnished by (19) alone is not a proof of
surjectivity of the unrestricted two-output differential. The next
section verifies that extra property for a particular family.

## 8. A regular two-direction endpoint and an open two-input family

For small `epsilon>0`, take

\[
 u_1=(\cos\varepsilon,\sin\varepsilon),\qquad
 u_2=(-\cos\varepsilon,\sin\varepsilon),
 \qquad (y_1,y_2)=(1,-1),\quad\mu_1=\mu_2=1/2.
 \tag{25}
\]

Oddness makes this exactly equivalent, including its vector field, to
the two positive-label inputs
`v_+=(cos(epsilon),sin(epsilon))` and
`v_-=(cos(epsilon),-sin(epsilon))`. Their signal-time feature is
`H_epsilon=(T(v_+)+T(v_-))/2`. At `epsilon=0` it is the axis reference
of Sections 1--2, with `kappa_0>0`.

On every fixed signal-clock interval, the vector fields depend
continuously on `epsilon` in norm (12). Subtraction of the row equations
uses `||w dot (u-v)||_2<=||w||_2 |u-v|`; the moment coefficients and
readout supremum norm have the same continuous-dependence estimates.
Bounds (20) are uniform in `epsilon`. Thus the signal-time states and
their scalar predictions converge uniformly on compact clock intervals
to the axis reference. Since `kappa_epsilon -> kappa_0>0` and (19)
bounds the derivative at every crossing, their unique clock endpoints
`s_*(epsilon)` tend to `s_*(0)`. The endpoint states
`theta_*(epsilon)` consequently tend to the axis endpoint in (12),
and all have a common bound on `w-g` in supremum norm.

Let `z_epsilon(u)=M_*(epsilon) a_*(epsilon,u)` be the two-vector upper
argument at the endpoint. Reflection in the first coordinate axis gives

\[
 z_{\varepsilon}(\cos\alpha,-\sin\alpha)
   =\operatorname{diag}(1,-1)
       z_{\varepsilon}(\cos\alpha,\sin\alpha).
 \tag{26}
\]

In particular `z_epsilon,2(e_1)=0`. At the limiting axis endpoint,
use the notation of Section 1. The derivative of its second component
along the input circle is

\[
 r_*:=\left.\partial_\alpha
           z_{0,2}(\cos\alpha,\sin\alpha)\right|_{\alpha=0}
   =E[\operatorname{sech}^2 V_*]\,
          m_0\cdot E[\xi_2G_2]>0.
 \tag{27}
\]

The first factor is strictly positive. For the second, the exact
initialized calculation in `initial_geometry.md` gives
`E[m_0 dot xi_2 | G_2]=psi(G_2)/c_*`, with `psi'>0`. Gaussian
integration by parts therefore yields
`m_0 dot E[xi_2 G_2]=E psi'(G_2)/c_*>0`. The integration is justified
by bounded `psi` and bounded first derivative.

The input derivative of `z` is continuous under the just-proved endpoint
convergence and input convergence. Explicitly, its lower coefficient is
`E[b_1 sech^2(w dot u)(w dot u')]`; convergence follows by
Cauchy--Schwarz and truncation of the common Gaussian row, using the
uniform bounded displacement. This also gives uniformity for small
input angles. Integrating that derivative from `0` to `epsilon`, and
using (26)--(27), proves

\[
 z_{\varepsilon,2}(v_+)/\varepsilon\longrightarrow r_*>0,
 \qquad z_{\varepsilon,1}(v_+)\longrightarrow z_*>0.
 \tag{28}
\]

Thus, for every sufficiently small fixed `epsilon>0`, the endpoint
upper vectors for the actual two inputs in (25) are

\[
 (A_\varepsilon,B_\varepsilon),\qquad
 (-A_\varepsilon,B_\varepsilon),
 \qquad A_\varepsilon B_\varepsilon\ne0.
 \tag{29}
\]

They are nonparallel. The positive upper mark density and the ridge
independence lemma make their two-by-two readout Gram positive definite.
Hence the unrestricted full two-output differential is onto at the
finite zero-loss endpoint. Applying the trapping argument of Section 3
with two outputs proves an **unconditional open family of two-input
problems**, allowing independent perturbations of both directions and
of the positive masses around each such reference. The initializer,
physical metric, and full moving matrix remain exactly canonical.

This proves more than convergence on a symmetry curve, but it still
does not supply a third genuine direction.

## 9. Why a third interpolation point is still missing

For a general reflected opposite-label pair, let `a` be a unit vector
in the reflection's negative eigenspace. Oddness and reflection imply
zeros on its positive eigenspace and corresponding pairs of level
crossings. They do not require another unoriented direction with
prediction `+1` or `-1`.

For example the smooth nonlinear function

\[
 p(u)=\frac{\tanh(\lambda a\cdot u)}
                 {\tanh(\lambda a\cdot u_1)},\qquad\lambda>0,
 \tag{30}
\]

has every required odd/reflection identity and interpolates the two
training labels, yet its `+1` level on the circle consists exactly of
`u_1` and `-u_2`. Its `-1` level consists of their antipodes. This is
not claimed to be a canonical trained predictor. It proves that a
third-root argument based only on symmetry, continuity, nonlinearity,
and the known interpolation values is insufficient.

The radial-convexity estimate controls the scalar trained objective and
state boundedness; it does not give the whole-circle shape inequality
which would force an additional level crossing. No such inequality was
proved here, including for pairs near a contradictory coincidence.
A third crossing, if obtained by a separate argument, would also need
its full three-output differential checked before invoking openness.
The unconditional genuine-triple/open-three-input target therefore
remains unresolved after this extension.
