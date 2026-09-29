# Intrinsic geometry of finite-memory relearning

Status: internally derived exact identities and conditional local theorems; no
experiments and no promotion claim. Input scope was `MODEL.md` and
`docs/notation.qmd`, plus the required mathematical/research skills. This route
uses the prescribed fixed Gaussian hidden matrices and zero initial readout.
There is no width limit, independence replacement, or comparison trajectory.
The general identities and local theorems hold at each fixed finite width and
each finite order, in particular q = 1, 2, 3. The explicit witness is scalar.

The main new conclusion is conditional on reaching a fitted memory state with
a specified strict contraction margin. Near such a state, the leading nonlinear
dependence of the final *whole test function* on a label perturbation has
functional dimension at most one. Its shape vanishes on the training set, and
its amplitude is the extra activity-clock advance. This gives a sharp criterion
for a kink in the final label-to-function map. A scalar, one-sample tanh
benchmark proves that the kink coefficient is nonzero at canonically reachable
fitted states on a positive-probability set of Gaussian initializations, for
each fixed q, including q=1,2,3. This benchmark does not establish the frequency
or magnitude of the phenomenon for larger networks or arbitrary data.

## 1. Endpoint projection and exact velocity

Write d_k = 2k+1. For each hidden link and training sample define vectors

\[
\widehat h_{\ell,a}=\tau^{-1}\sum_{k<q}d_k B_{\ell,a,k},\qquad
\widehat b_{\ell,a}=\tau^{-1}\sum_{k<q}d_k C_{\ell,a,k}.
\]

These are the endpoints of the polynomial projections of the closure's own
forward and backward histories. In formulas below h_a denotes the current
forward vector at layer ell-1 when the layer is suppressed. Define

\[
M_{\ell,a}=\tau^{-1}\sum_{k<q}d_k C_{\ell,a,k}B_{\ell,a,k}^{T}.
\]

On an interval of positive residual, use activity tau as the independent
variable and put b_a = (r_a/rho) delta_a^ell. The moment equations give

\[
\frac{dM_{\ell,a}}{d\tau}
=b_a\widehat h_{\ell,a}^{T}
 +\widehat b_{\ell,a}h_a^{T}
 -\widehat b_{\ell,a}\widehat h_{\ell,a}^{T}
=b_a h_a^{T}-(b_a-\widehat b_{\ell,a})
                    (h_a-\widehat h_{\ell,a})^{T}.                 \tag{1}
\]

To verify all cross terms, let the lower triangular moment matrix have entries
A_kk = k and A_kj = d_j for j<k. With D = diag(d_k), its identity is

\[
D+DA+A^TD=dd^T.
\]

Its diagonal entries are d_k(1+2k)=d_k^2, and both off-diagonal triangles
have entries d_kd_j. Differentiating M and using this identity proves (1).
Returning to physical time removes every division by rho:

\[
\dot W_\ell=-\frac{2}{mn}\sum_a\left[
r_a\delta_a^\ell\widehat h_{\ell,a}^{T}
 +\rho\widehat b_{\ell,a}
       (h_a^{\ell-1}-\widehat h_{\ell,a})^{T}\right].             \tag{2}
\]

Equation (2), including its zero value at rho=0, is an exact identity of the
finite-memory system. The second term is motion produced by transporting the
stored memory when the activity interval grows.

## 2. Exact whole-function equation

For any input x, compute its current forward fields and backward fields using
the reconstructed current weights. Define the generally nonsymmetric kernel

\[
\begin{aligned}
K(x,a)={}&\frac{(h_x^L)^Th_a^L}{n}
 +\frac{x^Tx_a}{d}\frac{(\delta_x^1)^T\delta_a^1}{n}\\
&+\sum_{\ell=2}^L
 \frac{(\delta_x^\ell)^T\delta_a^\ell}{n}
 \frac{(h_x^{\ell-1})^T\widehat h_{\ell,a}}{n},\\
V(x)={}&-\frac{2}{mn^2}\sum_{\ell=2}^L\sum_a
 ((\delta_x^\ell)^T\widehat b_{\ell,a})
 ((h_a^{\ell-1}-\widehat h_{\ell,a})^T h_x^{\ell-1}).
\end{aligned}
\]

The network chain rule and (2) yield

\[
\dot f(x)=-\frac{2}{m}\sum_a K(x,a)r_a+\rho V(x).                 \tag{3}
\]

The first-layer factor follows from the prescribed mobility: its output
Jacobian is delta_x^1 x^T/(n sqrt(d)), whereas its stored weight velocity has
no factor 1/n. Each middle-layer contraction has two factors 1/n. Thus the
normalizations in (3) agree with `MODEL.md`.

At a fixed state, reversal of all residuals reverses the first term of (3)
and leaves the second term unchanged. This even part is a possible observable
consequence of memory transport. It is not a consequence of making the fixed
Gaussian operators independent or replacing the current feature vectors.

## 3. A checkable local contraction condition

Let S_* be any finite fitted augmented state with tau_*>0 and predictions
f_*(x_a)=y_a. An augmented state consists of W1, w, tau and every B and C;
the hidden weights are reconstructed. It can, for example, be a finite limit
of a canonical training trajectory. Reachability is a separate hypothesis.

Evaluate the preceding quantities at S_* and set

\[
A=\frac{2}{m}[K(x_b,a)]_{b,a=1}^m,\quad
v=[V(x_b)]_{b=1}^m,\quad c=\frac{v}{\sqrt m},\quad
A_s=\frac{A+A^T}{2}.
\]

At any state, the training residual equation is exactly

\[
\dot r=-A(S)r+\|r\|_2 c(S).                                    \tag{4}
\]

For r nonzero, with u=r/||r||_2,

\[
\frac{d}{dt}\log\|r\|_2=-u^TA_s(S)u+c(S)^Tu.
\]

Consequently the exact strict uniform instantaneous contraction criterion at
S_* is

\[
\mu:=\min_{\|u\|_2=1}\{u^TA_su-|c^Tu|\}>0.                   \tag{5}
\]

The absolute value is valid because the sphere contains both u and -u.
A readily checked sufficient condition is

\[
\lambda_{\min}(A_s)>\|c\|_2.
\]

Condition (5) implies that A_s is positive definite and hence A is invertible:
if Az=0 for z nonzero then z^TA_sz=z^TAz=0, a contradiction.

This is a necessary and sufficient criterion for a *strict uniform
instantaneous Euclidean contraction margin*. It is not claimed necessary for
eventual convergence in dimensions m>1. If mu<0, there is a residual direction
with instantaneous loss growth. Direction rotation could still lead to later
convergence. If mu=0, higher-order behavior is unresolved by this criterion.

**Actual local return to interpolation.** Suppose (5) holds. Keep S_* as the
initial memory state and change the labels from y to y+eta. For all sufficiently
small eta, the new trajectory converges to a fitted state S_infinity(eta), and

\[
\|r(t)\|_2\le \|\eta\|_2 e^{-\gamma t},\qquad
\sup_{t\ge0}\|S(t)-S_*\|_2\le C\|\eta\|_2,                    \tag{6}
\]

where gamma>0 and C are independent of small eta. The state also has finite
total path length.

Proof: by continuity, a neighborhood of S_* has contraction margin at least
gamma=mu/2. The raw equations have the form

\[
\dot S=P(S)r+\|r\|_2Q(S),
\]

with smooth P and Q while tau stays positive; tanh and the reconstruction are
smooth there. Hence ||Sdot||_2 <= M||r||_2 in a smaller bounded neighborhood.
The contraction bound gives total state travel at most M||eta||_2/gamma.
Choose eta small enough that this travel cannot reach the neighborhood
boundary. This closes the trapping argument and proves (6). Integrability of
Sdot makes S converge; continuity and r(t)->0 prove interpolation.

This proof is entirely about the closure's own flow. It gives the finite
activity advance needed below and does not presuppose a global loss theorem.

## 4. One-function nonlinear response theorem

For a fixed test input, let the row vector

\[
a(x)=\frac{2}{m}[K(x,1),\ldots,K(x,m)].
\]

At S_*, define the test function

\[
D(x)=V(x)-a(x)A^{-1}v.                                         \tag{7}
\]

For x=x_b, a(x_b) is row b of A, so D(x_b)=0. Under (5), the converged
function after the label perturbation obeys

\[
f_\infty(x;y+\eta)-f_*(x)
=a(x)A^{-1}\eta+D(x)\,[\tau_\infty(\eta)-\tau_*]
 +O(\|\eta\|_2^2).                                            \tag{8}
\]

For each compact test-input set, the remainder is uniform on that set. No
uniform statement on an unbounded input domain is needed.

Proof: put I=integral_0^infinity r(t)dt and
Delta tau=integral_0^infinity ||r(t)||_2 dt/sqrt(m). The coefficient functions
are locally Lipschitz. By (6), replacing each coefficient along the trajectory
by its value at S_* produces an integrated error bounded by

\[
C\sup_t\|S(t)-S_*\|_2\int_0^\infty\|r(t)\|_2dt
=O(\|\eta\|_2^2).
\]

Integrate (4), using r(0)=-eta and r(infinity)=0:

\[
\eta=-AI+v\,\Delta\tau+O(\|\eta\|_2^2).
\]

Integrating the test equation (3) gives

\[
f_\infty(x)-f_*(x)=-a(x)I+V(x)\,\Delta\tau+O(\|\eta\|_2^2).
\]

Eliminating I proves (8).

The coefficient a(x)A^{-1} also equals K(x,train)K(train,train)^{-1}.
This does not make K symmetric or positive semidefinite; invertibility here
comes from (5). Equation (8) is an expansion of the actual nonlinear
relearning trajectory, not an assumed kernel algorithm.

**Interpretation.** Regardless of the number of samples, width, depth or
finite response order, all leading nonlinear dependence on the label change
lies in the single function D. Its amplitude is the extra activity clock.
This dimension-one statement relies on the model's *shared scalar clock*.
It need not hold for variants with independently evolving layer clocks.

There are constants 0<c_1<=c_2 such that

\[
c_1\|\eta\|_2\le\Delta\tau(\eta)\le c_2\|\eta\|_2.           \tag{9}
\]

The upper bound follows from (6). For the lower bound, choose a local bound
M_r >= ||A(S)||+||c(S)||. Equation (4) gives
d||r||_2/dt >= -M_r||r||_2, so ||r(t)||_2 >= ||eta||_2 exp(-M_r t).
Integration gives c_1=1/(sqrt(m)M_r); the upper constant is
1/(sqrt(m)gamma).

**Differentiability criterion.** On a compact test domain, the terminal
label-to-function map is Frechet differentiable at y if and only if D vanishes
identically on that domain. Sufficiency follows from (8), with derivative
eta -> a(.)A^{-1}eta. For necessity, choose x with D(x) nonzero. Adding (8)
for eta and -eta cancels the linear term and gives

\[
f_\infty(x;y+\eta)+f_\infty(x;y-\eta)-2f_*(x)
=D(x)[\Delta\tau(\eta)+\Delta\tau(-\eta)]
 +O(\|\eta\|_2^2).
\]

By (9), this is nonzero at first order along any nonzero perturbation direction.
It contradicts the odd first-order response required by differentiability.

The scalar directional response can also be made explicit. For eta=epsilon z,
epsilon down to zero, the rescaled training residual converges to the solution

\[
\dot e=-Ae+\|e\|_2c,\qquad e(0)=-z.
\]

Local Lipschitz continuous dependence gives convergence on bounded time
intervals; the uniform exponential bound (6) controls the remaining integral.
Thus

\[
\lim_{\epsilon\downarrow0}\frac{\Delta\tau(\epsilon z)}\epsilon
=\frac1{\sqrt m}\int_0^\infty\|e(t)\|_2dt.
\]

It is strictly positive for z nonzero and positively homogeneous in z. No
assertion that it is a norm, even, or differentiable is required.

## 5. A closed label cycle can change the test function at first order

Start from S_* at labels y, fit labels y+eta, retain the resulting fitted
memory, and fit the original labels y again. Both local fits exist by the
strict margin. Indeed, the first fitted state S_1 differs from S_* by
O(||eta||_2), so continuity preserves a uniform positive contraction margin
for the second fit. Write Delta tau_out and Delta tau_back for the two
nonnegative clock advances. Then

\[
f_{\rm cycle}(x)-f_*(x)
=D(x)(\Delta\tau_{\rm out}+\Delta\tau_{\rm back})
 +O(\|\eta\|_2^2).                                            \tag{10}
\]

The remainder is uniform on each compact test-input set. To prove this, let
L_*(x)=a(x)A^{-1}. The outward fit contributes
L_*(x)eta+D(x)Delta tau_out+O(||eta||_2^2). At S_1 the return fit has label
perturbation -eta. Its coefficients satisfy L_1=L_*+O(||eta||_2) and
D_1=D+O(||eta||_2), uniformly on the compact test set. The return contribution
is -L_1(x)eta+D_1(x)Delta tau_back+O(||eta||_2^2). The linear terms cancel
to second order, while Delta tau_back=O(||eta||_2). This proves (10).

Both fits end with their prescribed training predictions, so the completed
cycle returns every training output exactly to its original value. But if
D(x) is nonzero at some test input, (9) and its uniform counterpart for the
return fit show an off-training change of order ||eta||_2 there. Reversing the
sign of eta does not cancel this first-order effect: both clock advances
remain positive. If D vanishes identically, the cycle changes the test
function by at most O(||eta||_2^2). These are local statements about one small
cycle; accumulation over arbitrarily many cycles is not established.

Thus the fitted test function can retain the direction of *memory transport*
after a label excursion even when the final labels and all fitted training
outputs are unchanged. Section 8 supplies canonically reachable strictly
contracting fitted states with D nonzero in a restricted scalar benchmark;
no arbitrary memory history is substituted for a canonical trajectory.

## 6. One-sample one-sided terminal kernels

Specialize only this section to m=1. Let

\[
a_x=2K(x,1),\quad c_x=V(x),\qquad a=a_{x_1},\quad c=c_{x_1}.
\]

Condition (5) is precisely a>|c|. The directional residual equation is
e'=-ae+c|e|. A positive label perturbation has initial residual -epsilon and
decays at leading rate a+c; a negative perturbation has positive residual
and decays at leading rate a-c. Therefore

\[
\begin{aligned}
\partial_{y,+}f_\infty(x)&=\frac{a_x+c_x}{a+c},\\
\partial_{y,-}f_\infty(x)&=\frac{a_x-c_x}{a-c}.                  \tag{11}
\end{aligned}
\]

Both equal one at the training input. Their difference is

\[
\partial_{y,+}f_\infty(x)-\partial_{y,-}f_\infty(x)
=\frac{2(ac_x-a_xc)}{a^2-c^2}.
\]

Consequently the learned function can have a label-response kink even though
the target value is matched exactly and smoothly at the training point. The
kink disappears precisely when the transport field c_x is everywhere
proportional to the residual-linear response field a_x, with proportionality
c/a. Nonzero transport alone does not suffice for a kink: that proportional
case is an important exception.

If a<|c|, one sign of sufficiently small residual has instantaneous growth.
At a=|c|, a first-order rate vanishes and higher-order analysis is necessary.
These statements do not establish global divergence or rule out later return.

## 7. Obstruction to a smooth loss-gradient representation

There is a specific conclusion about optimization geometry, weaker than a
claim that no potential of any kind exists. At a fixed memory state, write
the physical parameter velocity as

\[
\dot\theta=U(\theta,\text{memory})r
       +\|r\|_2 Q_\theta(\theta,\text{memory}).                  \tag{12}
\]

The readout and first-weight components of Q_theta vanish. Its hidden-link
components, from (2), are

\[
(Q_\theta)_\ell=-\frac{2}{mn\sqrt m}\sum_a
\widehat b_{\ell,a}(h_a^{\ell-1}-\widehat h_{\ell,a})^T.
\]

If Q_theta is nonzero at a fitted state, (12) cannot be represented near that
state, uniformly under small label perturbations, as

\[
\dot\theta=-G(\theta,\text{memory},r)\nabla_\theta\mathcal L,
\]

with G continuous at r=0. This obstruction does not even require G to be
symmetric or positive. At fixed physical parameters,
gradient_theta L=(2/m)J_theta^T r is linear and odd in r. Continuity of G
would make the sum of velocities at r and -r be o(||r||_2). Equation (12)
makes that sum exactly 2||r||_2 Q_theta, a contradiction.

For the entire raw augmented state, the tau component already supplies a
nonzero even velocity, since tau_dot=||r||_2/sqrt(m). The physical-parameter
criterion above is stronger scientifically because it concerns actual network
motion, rather than merely an auxiliary clock convention. If D is nonzero at
some test input, then V is nonzero as a function and hence Q_theta is nonzero,
so the terminal kink implies this physical obstruction.

This does not exclude nonsmooth residual-dependent mobilities, a different
objective, a nonlocal variational formulation, or a specially chosen potential
on a smaller invariant set. It excludes the stated smooth training-loss
gradient interpretation at states satisfying the nonzero-transport condition.

## 8. A reachable canonical witness for q=1,2,3

This section restricts to m=n=d=1, L=2, training input x_1=1 and tanh in both
layers. The prescribed Gaussian first and middle weights are scalars. Fix
positive initial values p>0 and M>0 and the prescribed w(0)=0. Write

\[
h=\tanh p,\quad a=\tanh(Mh),\quad
E=\operatorname{sech}^2p,\quad H=\operatorname{sech}^2(Mh),\quad
v_0=Ha,\quad U=E^2Mv_0>0.
\]

The initial state is fitted for label zero. Its contraction coefficients are
A=2a^2>0 and c=0, because the readout and all backward moments vanish.
Applying Section 3 to a sufficiently small positive label y gives convergence
from this very same initial state to a fitted state S_y. This is precisely the
canonical initialization for label y; no initialization is changed. The state
remains near its initial value, and the scalar residual stays negative for
every finite time: while r<0 its equation is r'=-(A(S)+c(S))r, which cannot
reach zero in finite time when the coefficients are bounded.

On this trajectory set s=2 integral_0^t |r(u)|du. Then tau=1+s/2. The raw
equations in s are smooth, with w_s=h_1^(2), W1_s=delta_1^(1) and

\[
\frac{dC_k}{ds}=-\frac12\delta_1^{(2)}
 -\frac1{2\tau}\left[kC_k+\sum_{j<k}(2j+1)C_j\right].
\]

The leading Taylor coefficients obtained directly from these equations are

\[
\begin{aligned}
w(s)&=as+O(s^3),&\quad \delta_1^{(2)}(s)&=v_0s+O(s^3),\\
h_1^{(1)}(s)&=h+\frac12Us^2+O(s^4),&
C_k(s)&=-\frac14v_0s^2+O_q(s^3).
\end{aligned}
\]

For the first-layer coefficient, W1_s=E M v_0s+O(s^3), and multiplying
its integrated displacement by the derivative E of tanh gives U/2.
The middle weight and first weight have no linear displacement, giving the
stated orders for w and delta. The common leading term of C_k follows because
its damping term is O(s^2).

The forward endpoint projection satisfies widehat h=h+O_q(s^3). Indeed, it
reproduces the constant history h exactly. The deviation of the forward
history from h is O(s^2) and is supported on an activity interval of length
s/2, while the fixed-q endpoint projection kernel is bounded there. Also,

\[
\widehat b=-\frac{q^2}{4}v_0s^2+O_q(s^3),
\]

because sum_(k<q)(2k+1)=q^2 and tau=1+O(s).

For a fixed test input x define its initial features and derivative

\[
h_x=\tanh(px),\qquad a_x=\tanh(Mh_x),\qquad
H_x=\operatorname{sech}^2(Mh_x).
\]

Then delta_x^(2)=asH_x+O(s^3). Substitution in (3) gives

\[
\begin{aligned}
V(x)&=\frac{q^2s^5}{4}\,a v_0 U H_xh_x+O_q(s^6),\\
K(x,1)&=aa_x+O_q(s^2),\qquad K(1,1)=a^2+O_q(s^2),\\
D(x)&=\frac{q^2s^5}{4}\,a v_0 U
 \left[H_xh_x-\frac{a_x}{a}Hh\right]+O_q(s^6).                 \tag{13}
\end{aligned}
\]

Take the explicit test input x=2. Then h_2>h>0. The bracket in (13) equals
a_2[g(h_2)-g(h)], where

\[
g(z)=\frac{z\operatorname{sech}^2(Mz)}{\tanh(Mz)}
    =\frac{2z}{\sinh(2Mz)}.
\]

This function is strictly decreasing for z>0: its derivative has the sign
of sinh(t)-t cosh(t) for t=2Mz>0, and that expression vanishes at t=0 and
has derivative -t sinh(t)<0. Thus the leading coefficient in D(2) is
strictly negative.

At the fitted endpoint, s_infinity>0 tends to zero with y. More precisely,
the training output is a^2s+O_q(s^3), so
s_infinity=y/a^2+O_q(y^3). Therefore D(2)<0 at the canonically reached fitted
state for every sufficiently small positive y, for each fixed finite q.
The strict contraction margin persists by continuity from 2a^2>0.

This proves actual one-sided terminal label sensitivities and an actual
first-order closed-label-cycle change at x=2 in the prescribed canonical
model. The positive initial pairs p,M form a positive-probability Gaussian
event. To state the witness with one fixed label rather than a label chosen
after initialization, take a small closed box around any strictly positive
pair: the strict coefficients and all local bounds above hold uniformly on
that box, so a common sufficiently small y works on its positive-probability
interior.

The witness is deliberately restricted. It proves occurrence within the
canonical family, not a typical-width statement, not a lower bound uniform
in q, and not that the memory-induced test drift is beneficial.

## 9. Claim boundaries and the remaining bottleneck

- Equations (1)--(4) are exact for every finite q, including q=1,2,3, at every
  finite state with tau>0.
- Condition (5), the local return theorem, the rank-one functional expansion
  (8), and the differentiability criterion are proved conditional on a fitted
  state with that strict margin. They require no random-coordinate assumption.
- The one-sample formulas (11) concern relearning from an existing fitted
  memory, not retraining from fresh zero readout for each label. Confusing these
  two protocols would erase the question being analyzed.
- Section 8 proves a positive-probability canonical scalar witness with D
  nonzero and a strict margin for each fixed finite q. What remains open is
  a mechanism-preserving extension describing occurrence, scale or sign in
  larger networks or general multi-sample data; the scalar witness does not
  supply those quantifiers.
- No claim compares different response orders on the same fabricated history,
  no arbitrary moment-state pair is used as a reachable-state counterexample,
  and no statement of global convergence or minimum-energy selection is made.

A useful structural sufficient special case is
widehat h_(ell,a)=h_a^(ell-1) for all hidden links and samples. Then V=0 and K
is the sum of Gram kernels of the current parameter derivatives, so it is
symmetric positive semidefinite. If it is positive definite on the training
set, (5) holds and D=0. Mere small training residual, or interpolation by
itself, does not impose this equality of endpoint projection and current
forward response.
