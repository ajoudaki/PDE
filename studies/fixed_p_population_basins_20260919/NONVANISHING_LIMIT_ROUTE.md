# Exponential rates under a vanishing perturbation

**Scope and provenance.** This is an independent prompt-only theoretical route,
prepared by `/root/rate_limit_transfer` on 2026-09-19. The scientific input is
the supervisor's assignment alone. Required process instructions and the
`solve-math-rigorously` and `investigate-conjectures` skills were read. No other
study material, canonical model equations, external scientific sources, other
route, or experimental result was consulted. The arguments below are complete
abstract implications; applications to a particular closure require checking
their hypotheses in that closure. No canonical failure example is supplied or
known from the allowed inputs. No experiments were performed.

**Conclusion.** Finite-time convergence to deterministic gradient flow and a
common positive exponential rate with a common finite prefactor can coexist
only if that reference flow has the same exponential loss bound. Convergence
in probability is enough; uniform integrability is unnecessary for this
one-sided conclusion. If the reference stalls at positive loss or decays
subexponentially, a uniformly positive rate forces the prefactors to diverge.
Small expected loss also gives an explicit lower bound on the probability of
departing from a reference that still has substantial loss.

## 1. Contract and transfer theorem

Let `(E,d)` be a metric state space, let `L:E -> [0,infinity)` be continuous,
and fix a common initial state `S_0` with finite `L_0=L(S_0)`. Let
`S^0:[0,infinity) -> E` be a deterministic continuous reference trajectory and
`S_epsilon` be random trajectories with `S_epsilon(0)=S_0`. Write

\[
\ell(t)=L(S^0(t)),\qquad X_\varepsilon(t)=L(S_\varepsilon(t)),\qquad
m_\varepsilon(t)=\mathbb E X_\varepsilon(t).
\]

The physical time variable is `t`. All limits below are `epsilon -> 0` with
`t` or the physical horizon `T` fixed, unless a growing horizon is explicitly
stated. Assume at least

\[
S_\varepsilon(t)\longrightarrow S^0(t)\quad\hbox{in probability for each fixed }t.
\tag{1}
\]

The usual stronger premise is

\[
\sup_{0\le s\le T}d(S_\varepsilon(s),S^0(s))\longrightarrow0
\quad\hbox{in probability for every finite }T.
\tag{2}
\]

Measurability of the displayed random variables is assumed. Continuous sample
paths suffice for the hitting-time statements below. Deterministic convergence
is the special case with no randomness. Gradient-flow structure is not needed
for the transfer theorem: it enters only when determining the actual reference
loss `ell`.

**Theorem 1.** Under (1), for every fixed `t`,

\[
\ell(t)\le\liminf_{\varepsilon\to0}m_\varepsilon(t).
\tag{3}
\]

Consequently, if for every sufficiently small `epsilon` and every `t >= 0`,

\[
m_\varepsilon(t)\le C L_0e^{-\lambda t},
\qquad C<\infty,\quad\lambda>0,
\tag{4}
\]

with the same `C,lambda`, then

\[
\ell(t)\le C L_0e^{-\lambda t}\qquad\hbox{for every }t\ge0.
\tag{5}
\]

**Proof.** Continuity at the deterministic point `S^0(t)` implies
`X_epsilon(t) -> ell(t)` in probability: for any `eta>0`, continuity supplies
`r>0` such that state distance below `r` makes loss distance below `eta`.
If `ell(t)>0`, fix `0<a<ell(t)`. Nonnegativity gives

\[
m_\varepsilon(t)\ge a\,\mathbb P(X_\varepsilon(t)\ge a),
\]

and the probability tends to one. Thus the lower limit is at least `a`;
letting `a` increase to `ell(t)` proves (3). If `ell(t)=0`, (3) follows from
nonnegativity. Combining (3) with (4) proves (5) at each fixed `t`. Since the
limit trajectory is deterministic, there is no uncountable intersection of
probability-one events to justify. No exchange of the small-perturbation and
infinite-time limits occurred. ∎

More generally, `m_epsilon(t) <= B_epsilon(t)` implies
`ell(t) <= liminf_epsilon B_epsilon(t)` pointwise. Bounds valid only up to
`T_epsilon -> infinity` give the same conclusion, because every fixed `t`
eventually lies inside that horizon. If (4) is only known on a dense set of
times, (5) extends to all times by continuity of `ell` and the exponential.

If `L_0=0`, (4) forces `X_epsilon(t)=0` almost surely at each fixed time,
and (3) forces `ell(t)=0`. The remaining formulas involving division by
`L_0` assume `L_0>0`; then any bound including `t=0` has `C>=1`.

The necessary condition is sharp at the level of this abstract existence
question: whenever (5) holds, the family `S_epsilon=S^0` satisfies both
convergence and (4). It is not a sufficiency theorem for a prescribed
nontrivial perturbation family, an admissible closure class, or a construction
whose coefficients must obey additional provenance constraints.

## 2. The exact prefactor obstruction

For a requested rate `lambda>0`, define the extended real number

\[
C_*(\lambda)=\sup_{t\ge0}\frac{e^{\lambda t}\ell(t)}{L_0}.
\tag{6}
\]

This is the smallest possible prefactor for the reference trajectory. Suppose

\[
m_\varepsilon(t)\le C_\varepsilon L_0e^{-\lambda t}
\quad(t\ge0).
\tag{7}
\]

For every fixed `t`, (3) gives

\[
\liminf_{\varepsilon\to0}C_\varepsilon
\ge\frac{e^{\lambda t}\ell(t)}{L_0}.
\]

Taking the supremum over these deterministic lower bounds proves

\[
\liminf_{\varepsilon\to0}C_\varepsilon\ge C_*(\lambda).
\tag{8}
\]

Thus `C_*(lambda)=infinity` forces `C_epsilon -> infinity`, not merely
unboundedness along some subsequence. The same conclusion holds if the rates
`lambda_epsilon` in (7) are eventually at least `lambda`. If instead
`lambda_epsilon -> lambda>0`, the bound
`C_epsilon >= e^{lambda_epsilon t}m_epsilon(t)/L_0` and (3) give (8) directly.

In particular, a stalled reference with `ell(t) >= b>0` for arbitrarily large
times has `C_*(lambda)=infinity` for every positive `lambda`. A reference with
positive subexponential loss has the same property. More precisely, put

\[
\kappa=\liminf_{t\to\infty}
-\frac1t\log\frac{\ell(t)}{L_0},
\]

using `-log 0=+infinity`. Every `lambda>kappa` has `C_*(lambda)=infinity`:
for some `delta>0` there are arbitrarily large `t` with
`ell(t)/L_0 > exp(-(lambda-delta)t)`. Conversely, if `0<lambda<kappa`,
choose `delta>0` with `lambda+delta<kappa`; eventually
`ell(t)/L_0 <= exp(-(lambda+delta)t)`. The expression in (6) is then at
most `exp(-delta t)` at large times and is bounded on the remaining compact
interval by continuity. At the boundary `lambda=kappa`, the prefactor may be
finite or infinite; the exponential decay exponent alone does not decide it.

If `C_epsilon` stays bounded and `lambda_epsilon` has a positive lower bound,
the reference must therefore admit a positive exponential rate. If the
reference admits none, either the prefactors escape or the rates have no
positive uniform lower bound. This statement concerns a fixed initial state;
it supplies no constants uniform over other initializations, dimensions, or
problem instances.

## 3. Fixed-accuracy times

Assume continuous loss paths and define, for `0<a<L_0`,

\[
\tau_\varepsilon(a)=\inf\{t\ge0:X_\varepsilon(t)\le a\},\qquad
\tau_0(a)=\inf\{t\ge0:\ell(t)\le a\},
\]

with `inf empty=infinity`. If (4) holds, then

\[
\mathbb P(\tau_\varepsilon(a)>t)
\le\mathbb P(X_\varepsilon(t)>a)
\le\min\left\{1,\frac{C L_0}{a}e^{-\lambda t}\right\}.
\tag{9}
\]

The first inclusion holds because no threshold crossing by time `t` implies
loss above `a` at time `t`. The second follows by bounding the expectation
below by `a` times that probability. Hence, for `0<delta<1`,

\[
\mathbb P\!\left(\tau_\varepsilon(a)\le
\lambda^{-1}\log\frac{C L_0}{a\delta}\right)\ge1-\delta,
\qquad
\tau_0(a)\le\lambda^{-1}\log\frac{C L_0}{a}.
\tag{10}
\]

The reference bound follows from (5) at its displayed time. Furthermore,

\[
\mathbb E\tau_\varepsilon(a)
\le\lambda^{-1}\left(\log\frac{C L_0}{a}+1\right).
\tag{11}
\]

To verify (11), write a nonnegative number `u` as
`integral_0^infinity 1_{u>t} dt` and integrate the corresponding indicators
for the random variable; approximation by increasing nonnegative simple
functions justifies interchanging these nonnegative integrals. Integrating
(9) gives `log(C L_0/a)/lambda` before its two bounds meet and `1/lambda`
afterwards. These estimates concern first attainment; without monotonicity,
they do not promise the loss stays below `a` afterwards. They also do not
imply finite-time attainment of loss exactly zero or convergence of the state.

Convergence of trajectories alone gives a useful but distinct statement.
Under (2),

\[
\sup_{s\le T}|X_\varepsilon(s)-\ell(s)|\longrightarrow0
\quad\hbox{in probability}.
\tag{12}
\]

Indeed, the image of the reference path on `[0,T]` is compact. At each point
of that image choose a continuity ball on which the loss changes by less
than `eta/2`. A finite subcover by balls of one third those radii supplies
a common positive radius such that a nearby state and its reference point
both lie in one original ball; their losses then differ by less than `eta`.
Apply (2) with that radius.

On the event that the supremum in (12) is at most `eta`, for `0<eta<a`,

\[
\tau_0(a+\eta)\wedge T
\le\tau_\varepsilon(a)\wedge T
\le\tau_0(a-\eta)\wedge T.
\tag{13}
\]

For the left inequality, a perturbed crossing before `T` has reference loss
at most `a+eta`; for the right, a reference crossing of `a-eta` before `T`
has perturbed loss at most `a`. Continuity ensures a finite first crossing
attains its threshold. If the relevant crossing is beyond `T`, the capped
inequality is automatic. In particular, if `t<tau_0(a)`, the continuous
reference loss has a strictly positive gap above `a` on `[0,t]`, and (12)
implies `P(tau_epsilon(a)<=t) -> 0`.

Exact hitting-time convergence requires an additional crossing condition,
for example `tau_0(a+eta)` and `tau_0(a-eta)` both tending to `tau_0(a)`
as `eta` decreases to zero. A tangency or plateau can violate that condition;
uniform path approximation alone does not assert it. These qualifications
do not weaken the unconditional bounds (9)--(11).

## 4. Quantified conflict between small loss and faithful approximation

Fix a physical time `t` with `ell(t)>0`, and choose `0<eta<ell(t)`. On the
event `|X_epsilon(t)-ell(t)|<=eta`, loss is at least `ell(t)-eta`. Therefore

\[
\mathbb P\bigl(|X_\varepsilon(t)-\ell(t)|>\eta\bigr)
\ge\left[1-\frac{m_\varepsilon(t)}{\ell(t)-\eta}\right]_+.
\tag{14}
\]

Here `[z]_+=max(z,0)`. If continuity supplies `r>0` such that

\[
d(s,S^0(t))\le r\ \Longrightarrow\ L(s)\ge\ell(t)-\eta,
\]

the identical proof gives the state-space conclusion

\[
\mathbb P\bigl(d(S_\varepsilon(t),S^0(t))>r\bigr)
\ge\left[1-\frac{m_\varepsilon(t)}{\ell(t)-\eta}\right]_+.
\tag{15}
\]

Such a closed-ball radius follows by taking a smaller radius than the open
continuity neighborhood. Combining (14) or (15) with (7) yields the explicit
lower bound

\[
\left[1-\frac{C_\varepsilon L_0e^{-\lambda t}}
{\ell(t)-\eta}\right]_+.
\tag{16}
\]

Thus expected loss substantially below the reference forces departure with
substantial probability, regardless of how the perturbation is implemented.
There is no assumption of bounded loss, monotonicity, or uniform integrability.

Equivalently, suppose an approximation guarantee is actually established at
a possibly growing horizon `T_epsilon`, in the form

\[
\mathbb P\!\left(\sup_{s\le T_\varepsilon}
|X_\varepsilon(s)-\ell(s)|\le\eta_\varepsilon\right)
\ge1-q_\varepsilon.
\]

For `q_epsilon<1`, (7) forces

\[
C_\varepsilon\ge
\frac{1-q_\varepsilon}{L_0}
\sup_{0\le t\le T_\varepsilon}
e^{\lambda t}(\ell(t)-\eta_\varepsilon)_+.
\tag{17}
\]

If `ell(T_epsilon)>=b>eta_epsilon`, this implies

\[
C_\varepsilon\ge
\frac{(1-q_\varepsilon)(b-\eta_\varepsilon)}{L_0}
e^{\lambda T_\varepsilon}.
\tag{18}
\]

For a plateau and fixed error/confidence, maintaining faithful approximation
through time `T` therefore costs a prefactor exponential in `T`. For fixed
`C`, (18) instead bounds the possible horizon by

\[
T\le\lambda^{-1}\log\frac{C L_0}{(1-q)(b-\eta)}.
\]

Finite-horizon convergence (2) alone gives no quantitative relation between
`epsilon` and an admissible growing horizon. Formula (17) uses such a relation
only when it has separately been proved.

## 5. Expectations, pathwise assertions, and tails

An almost-sure bound `X_epsilon(t)<=C L_0 exp(-lambda t)` implies (4) simply
by taking expectations. Conversely, (4) gives probability bounds such as (9)
and (14), not the same pathwise bound. A random prefactor `A_epsilon` is enough
for (4) if the pathwise bound uses that prefactor and
`sup_epsilon E A_epsilon<=C`; almost-sure finiteness of each prefactor does
not provide this uniform moment bound.

For each fixed `epsilon`, (4) does imply a pathwise eventual rate on the
integer time grid: if `0<rho<lambda` and `K>0`,

\[
\mathbb P(X_\varepsilon(n)>Ke^{-\rho n})
\le\frac{C L_0}{K}e^{-(\lambda-\rho)n}.
\]

The probability of any such violation at an integer `n>=N` is at most the
sum of this geometric tail, which tends to zero as `N` tends to infinity.
Thus almost surely only finitely many integer-grid violations occur.
This argument is for each fixed perturbation and supplies no common random
onset time for all perturbations. If loss is pathwise nonincreasing, then
for `n<=t<n+1`, `X_epsilon(t)<=X_epsilon(n)`, so the same eventual rate
extends to continuous time with an extra factor `exp(rho)`. Mere continuity
does not provide that extension.

For completeness, a continuous counterexample to that extension is explicit.
Let `U` be uniform on `[0,1]`, fix `lambda>0`, and for integers `n>=1` set

\[
c_n=n+\tfrac14+\tfrac12U,\quad
w_n=\tfrac1{16}e^{-2\lambda(n+1)},\quad
b_n(t)=\left(1-\frac{|t-c_n|}{w_n}\right)_+,
\quad X(t)=e^{-\lambda t}+\sum_{n\ge1}b_n(t).
\]

Each bump is supported strictly inside `(n,n+1)`; the sum is locally finite,
continuous, nonnegative, and `X(0)=1`. At any fixed `t` in `[n,n+1]`,
the probability that the bump is nonzero is at most `4w_n`, because `c_n`
is uniform on an interval of length `1/2`. Thus

\[
\mathbb E X(t)\le e^{-\lambda t}+4w_n
\le\tfrac54e^{-\lambda t},
\]

using `t<=n+1`; outside all these intervals there is only the baseline.
Yet `X(c_n)>=1` for every `n` on every sample path. Therefore no positive
continuous-time pathwise exponential rate follows from an exponential
expectation bound plus continuity alone. This scalar loss-process example
is an abstract probability counterexample, not an optimizer or closure model.

Uniform integrability is unnecessary for (3), but is relevant to equality
of limiting expectations. To see why it cannot be silently assumed, take
`L(x)=x^2/2`, `S_0=1`, and its ordinary gradient flow `S^0(t)=exp(-t)`.
Let `h(t)=1-exp(-t)` and, on the same uniform random variable `U`, put

\[
S_\varepsilon(t)=e^{-t}
 +\boldsymbol1_{\{U\le\varepsilon\}}\varepsilon^{-1/2}h(t),
\qquad 0<\varepsilon<1.
\]

The initial state is unchanged. For every sample with `U>0`, all sufficiently
small perturbations equal the reference identically, so convergence is
almost sure on every compact horizon. Nevertheless,

\[
\mathbb E L(S_\varepsilon(t))
=\tfrac12e^{-2t}+\sqrt\varepsilon e^{-t}h(t)+\tfrac12h(t)^2,
\]

whose limit exceeds `ell(t)` for `t>0`. The expectations remain bounded;
bounded first moments alone are not uniform integrability. Replacing
`epsilon^{-1/2}` by `epsilon^{-1}` makes the last term
`h(t)^2/(2epsilon)`, so expectations can even diverge while the same
almost-sure convergence holds.

If instead the losses at a fixed time are uniformly integrable, meaning
`sup_epsilon E[X_epsilon 1_{X_epsilon>M}] -> 0` as `M -> infinity`, then
convergence in probability does give `E X_epsilon -> ell`. For fixed `M`,
the bounded variables `min(X_epsilon,M)` converge in probability to
`min(ell,M)`; their mean absolute difference is at most
`eta+M P(|min(X_epsilon,M)-min(ell,M)|>eta)`, which tends to at most `eta`.
Let `eta` decrease to zero, then control the omitted tails by uniform
integrability and take `M>ell` to infinity. This proves the assertion without
using it anywhere in the obstruction theorem.

## 6. What changing the prefactor, delay, or rate actually permits

A delayed estimate with fixed `A,lambda`,

\[
m_\varepsilon(t)\le
A L_0\exp[-\lambda(t-D_\varepsilon)_+],
\]

implies an all-time estimate with prefactor
`C_epsilon=A exp(lambda D_epsilon)`. Uniformly bounded delays thus give
a common prefactor; delays tending to infinity do not. A positive
asymptotic rate for each perturbation, with no common onset or prefactor,
does not contradict a stalled or subexponential reference.

Here is an example using a smooth objective perturbation, rather than an
arbitrary prescribed path. It is still only an abstract one-dimensional
example and makes no statement about any canonical closure. Let

\[
L(x)=(1-x^2)^2,\qquad x(0)=0,
\]

so ordinary gradient flow is `dot x=4x(1-x^2)` and its reference solution
stays at `x=0`, with loss one. Perturb the objective to
`L_epsilon(x)=L(x)+(epsilon/2)(1-x)^2`. Its gradient flow on `[0,1)` is

\[
\dot x_\varepsilon
=(1-x_\varepsilon)[4x_\varepsilon(1+x_\varepsilon)+\varepsilon],
\qquad x_\varepsilon(0)=0.
\tag{19}
\]

Existence and the required properties can be checked directly: the integral
of the reciprocal of the positive right-hand side from `0` to `x<1` is
strictly increasing from zero to infinity as `x` increases to one. Its
inverse defines a continuously differentiable solution for every `t>=0`,
strictly increasing towards one. The perturbation of the vector field is
`epsilon(1-x)`, uniformly at most `epsilon` on `[0,1]`.

Since the right-hand side of (19) is at most `4x_epsilon+epsilon`, multiply
the differential inequality by `exp(-4t)` and integrate to obtain

\[
0\le x_\varepsilon(t)\le\frac\varepsilon4(e^{4t}-1).
\]

Thus these perturbed flows converge to the stalled reference on every fixed
physical horizon. Let `D_epsilon` be the first time `x_epsilon=1/2`.
Before that time the right-hand side is also at least
`2x_epsilon+epsilon/2`; the same integrating-factor calculation gives

\[
\tfrac14\log(1+2/\varepsilon)
\le D_\varepsilon
\le\tfrac12\log(1+2/\varepsilon).
\]

After `D_epsilon`, the variable `y=1-x_epsilon` satisfies
`dot y <= -3y`, because `4x_epsilon(1+x_epsilon)>=3`. Hence

\[
L(x_\varepsilon(t))
\le e^{-6(t-D_\varepsilon)}\quad(t\ge D_\varepsilon),
\qquad
L(x_\varepsilon(t))\le e^{6D_\varepsilon}e^{-6t}\quad(t\ge0).
\]

The second inequality also holds before `D_epsilon`, since loss is then
at most one while its right-hand side is at least one. Each perturbation
therefore has a fixed positive all-time rate `6` with a diverging prefactor.
This example shows precisely why allowing the prefactor to depend on the
perturbation changes the conclusion.

A vanishing rate can instead coexist with a common prefactor. Let
`L(x)=x^4/4`, `x(0)=1`, and perturb its gradient flow to

\[
\dot x_\varepsilon=-x_\varepsilon^3-\varepsilon x_\varepsilon.
\]

Writing `z=x_epsilon^{-2}` gives `dot z=2+2epsilon z`, and hence

\[
x_\varepsilon(t)=
\left[(1+\varepsilon^{-1})e^{2\varepsilon t}
-\varepsilon^{-1}\right]^{-1/2}.
\]

On every fixed horizon this converges uniformly to
`x^0(t)=(1+2t)^{-1/2}`: expansion of the displayed exponential has a
remainder bounded by a constant depending on the horizon times `epsilon^2`,
so the bracket tends uniformly to `1+2t`. Its reference loss is
`L_0(1+2t)^{-2}`, which is subexponential. Positivity and
`dot x_epsilon<=-epsilon x_epsilon` give

\[
L(x_\varepsilon(t))\le L_0e^{-4\varepsilon t}.
\]

The prefactor is one, but the physical-time rate vanishes. This is again a
scalar illustration, not evidence of a canonical obstruction or success.

## 7. Fast oscillations and the clock

No noise-frequency or derivative estimate appears in Theorem 1. Once
finite-physical-time state convergence holds, rapid forcing cannot evade
its conclusion. State convergence also does not require convergence of
velocities: in one dimension the paths

\[
S_\varepsilon(t)=S^0(t)+\varepsilon\sin(t/\varepsilon^2)
\]

have uniform state error at most `epsilon`, share the initial state, and
have an added velocity `epsilon^{-1} cos(t/epsilon^2)`. This example proves
only that velocities may diverge while trajectories converge; it provides
no averaging theorem for stochastic forcing. If a proposed rapidly varying
perturbation has a different effective limit, identifying that limit is a
separate obligation, and premise (1) with the original reference may fail.

An exponential rate must be stated in the same clock as the convergence.
For example, if algorithmic time is `tau=a_epsilon t`, a bound
`C L_0 exp(-kappa tau)` becomes

\[
C L_0e^{-\kappa a_\varepsilon t}
\]

in physical time. If `a_epsilon -> 0`, its physical rate vanishes; if
`a_epsilon -> a>0`, the transferred physical rate is `kappa a`. If
`a_epsilon -> infinity` while `C` stays bounded and convergence (1) holds,
then (3) forces `ell(t)=0` for every `t>0`, which contradicts continuity
at zero whenever `L_0>0`. Reparametrizing the trajectories instead of merely
rewriting an estimate changes the convergence claim and must be checked
again. A diverging delay and a rescaled clock cannot be silently absorbed
into constants claimed uniform in physical time.

## 8. Claim boundary and check record

The proved obstruction is conditional: **a reference that lacks a finite
exponential envelope cannot be the finite-time limit of a family enjoying
that common envelope in expected nonnegative continuous loss.** The proof
does not establish that the canonical reference stalls, is subexponential,
or fails any desired closure claim. The prompt provides no such reference
trajectory or model-specific theorem. Conversely, a reference satisfying
the necessary envelope does not establish the existence, provenance,
restartability, state accuracy, or correct limiting identification of a
particular proposed closure. Fast optimization and faithful approximation
are connected by (14)--(18), not identified as the same property.

The author checked each implication by the displayed lower-expectation
inequality, the explicit integrating-factor calculations, and direct
substitution in the two scalar examples. Boundary cases checked include
zero initial loss, infinite prefactor supremum, threshold tangencies,
nonmonotone loss paths, rare large losses, diverging delays, vanishing
physical rates, and the distinction between integer-grid and continuous-time
pathwise bounds. This is a complete route candidate awaiting the supervisor's
comparison with the canonical inputs and any independent audit; it is not
promoted established material. Only this assigned file was written; the
shared Git index and other working files were not changed.
