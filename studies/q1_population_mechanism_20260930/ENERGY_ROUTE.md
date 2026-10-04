# Exact energy and passivity route for the autonomous q=1 closure

This is an independent, prompt-only theory result, frozen before receiving other
routes. It treats the stated finite-width autonomous closure as the object of
study. It uses no dense-training comparison, external scientific inputs,
experiments, or width limit. All identities below hold for every finite
realization of the stated Gaussian initialization. Conditional fitting statements
are labeled explicitly.

The main conclusion is an exact loss-dissipation identity with one signed
delayed-key work term, together with a stronger unconditional *integrated*
readout balance. These establish global existence and an online-regression
principle, but do not establish general fitting. A scalar reachable case does
admit an unconditional exponential-fitting theorem.

## 1. Setup and exact loss identity

Write

\[
 E=\frac1m\sum_a r_a^2=\rho^2,\qquad
 H=[h_a],\ K=[k_a],\ V=[v_a],\ G=[g_a],\ P=[r_a d_a],
 \qquad \Delta=H-K,\quad \alpha=\frac\rho\tau.
\]

The matrices displayed in brackets have size \(n\times m\). Introduce the
*derived* matrix

\[
 B=W_0+\frac{VK^\top}{mn},
 \qquad F=\frac{PH^\top}{mn},
 \qquad Z=\frac{(2P+\alpha V)\Delta^\top}{mn}.
\]

This notation does not add a stored state. The evolution remains exactly the
given closure. Define nonnegative quantities

\[
 D_A=\frac{\|\dot A\|_F^2}{n},\qquad
 D_w=\frac{\|\dot w\|^2}{n}.
\]

**Exact identity.** Along every solution,

\[
 \boxed{\quad \dot E=-D_A-D_w-4\|F\|_F^2+2\langle F,Z\rangle_F.\quad} \tag{1}
\]

To verify it, regard \(A,w,B\) temporarily as independent coordinates in the
forward map. Direct differentiation gives

\[
 \nabla_A E=-\dot A/n,\qquad
 \nabla_w E=-\dot w/n,\qquad
 \nabla_B E=\frac{2PH^\top}{mn}=2F.
\]

These are identities of this closure because its stated \(l_a\) equals
\((1-h_a^2)\odot B^\top d_a\). Its actual derived-matrix derivative is

\[
 \dot B=\frac{-2PK^\top+\alpha V\Delta^\top}{mn}
       =-2F+Z.
\]

The chain rule now proves (1). In particular, when current and stored keys
coincide, all three displayed channels dissipate the actual closure loss at
that instant. Delayed keys create the single signed work term \(2\langle
F,Z\rangle\); its first part comes from value updates against old keys and
its second from key movement against accumulated values. Neither part has a
general sign. This identifies a concrete mechanism and a concrete obstruction,
without importing a dense gradient-flow law.

## 2. Reachable keys are passive averages, not arbitrary vectors

The initialized key equation integrates exactly to

\[
 K(t)=\frac{H(0)+\int_0^t\rho(s)H(s)\,ds}{\tau(t)},\qquad
 \tau(t)=1+\int_0^t\rho(s)\,ds. \tag{2}
\]

Consequently every key coordinate stays in \([-1,1]\). With

\[
 e=\frac{\|H-K\|_F}{\sqrt{mn}},\quad
 \kappa^2=\frac{\|K\|_F^2}{mn},\quad
 \eta^2=\frac{\|H\|_F^2}{mn},
\]

the filter has the exact storage identity

\[
 \frac d{dt}(\tau\kappa^2)=\rho(\eta^2-e^2),\qquad
 \tau(t)\kappa(t)^2+\int_0^t\rho e^2
 =\eta(0)^2+\int_0^t\rho\eta^2. \tag{3}
\]

Indeed, the derivative on the left is
\(\rho(\|K\|_F^2+2\langle K,H-K\rangle_F)/(mn)
=\rho(\|H\|_F^2-\|H-K\|_F^2)/(mn)\).
This is genuine filter dissipation, but it does not control the sign of its
coupling to \(P,V\) in (1).

An exact lag formula and a useful bound are

\[
 \Delta(t)=\frac1{\tau(t)}\int_0^t\tau(s)\dot H(s)\,ds,
 \qquad
 e(t)\le\frac1{\tau(t)}\int_0^t\tau(s)\sqrt{D_A(s)}\,ds. \tag{4}
\]

For the identity, integrate
\((\tau H)'=\rho H+\tau\dot H\) and subtract (2). For the bound,
\(\dot h_a=(1-h_a^2)\odot\dot A x_a/\sqrt d\), so
\(\|\dot H\|_F\le\sqrt m\|\dot A\|_F\), using
\(\|x_a\|=\sqrt d\). Thus key lag is produced precisely by read-in motion
and filtered with the residual clock.

## 3. Unconditional readout balance and global existence

For any *fixed* comparator \(u\in\mathbb R^n\), let

\[
 f_{u,a}(t)=u^\top g_a(t)/n,\qquad
 E_u(t)=\frac1m\sum_a(f_{u,a}(t)-y_a)^2.
\]

The comparator uses the actual current, endogenously evolving features. It
does not generate a second trajectory. Directly from the readout equation,

\[
 \frac d{dt}\frac{\|w-u\|^2}{2n}
 =-E+E_u-\frac1m\sum_a(f_a-f_{u,a})^2. \tag{5}
\]

The proof is the scalar identity
\(2(f-y)(f-f_u)=(f-y)^2-(f_u-y)^2+(f-f_u)^2\), averaged over
examples. This proof never differentiates \(g_a\), so feature feedback and
delayed memory do not spoil the balance.

Taking \(u=0\), using \(w(0)=0\) and \(y_a^2=1\), yields

\[
 \boxed{\quad
 \frac{\|w(t)\|^2}{2n}
 +\int_0^t\left[E(s)+\frac1m\sum_a f_a(s)^2\right]ds=t.
 \quad} \tag{6}
\]

Thus the time-average MSE never exceeds the initial value \(1\), even if
instantaneous loss increases. The readout is passive with input labels and
output predictions: equivalently,
\(d[\|w\|^2/(4n)]/dt=\operatorname{mean}_a(y_af_a-f_a^2)\).
This is a balance, not a decreasing state-only Lyapunov function.

Equation (6) also proves global well-posedness. On every local solution,

\[
 \|w(t)\|/\sqrt n\le\sqrt t,\qquad
 1\le\tau(t)\le1+t,\qquad
 \frac{\|V(t)\|_F}{\sqrt{mn}}\le\sqrt2\,t^{3/2}. \tag{7}
\]

The sharper readout bound uses
\(E+\operatorname{mean}f^2=1/2+2\operatorname{mean}(f-y/2)^2\ge1/2\)
in (6). The clock bound follows from
\(\int_0^t\rho\le\sqrt{t\int_0^t E}\le t\).
Writing \(R=\|w\|/\sqrt n\), one has
\(\|P\|_F/\sqrt{mn}\le\rho R\), since
\(\|d_a\|\le\|w\|\). Therefore

\[
 \frac{\|V(t)\|_F}{\sqrt{mn}}
 \le2\int_0^t\rho R
 \le2\sqrt{\int_0^t E}\sqrt{\int_0^tR^2}
 \le\sqrt2\,t^{3/2}.
\]

Since \(\|K\|_F\le\sqrt{mn}\),
\(\|B\|_{\rm op}\le\|W_0\|_{\rm op}+\sqrt2\,t^{3/2}\).
The read-in equation obeys
\(\|\dot A\|_F/\sqrt n\le2\rho R\|B\|_{\rm op}\).
All its factors are bounded on each finite interval: in particular
\(\rho\le1+R\). Every state variable therefore stays bounded on finite
intervals, while \(\tau\ge1\). The vector field is locally Lipschitz on
\(\tau>0\), because tanh is smooth and \(\rho\) is a Euclidean norm of
smooth residuals. Local uniqueness holds, and a finite maximal lifetime would
contradict extension from a bounded state inside \(\tau>0\). Hence solutions
are unique and global. No random-matrix norm estimate is needed.

For arbitrary fixed \(u\), integrating (5) gives the sharper consequence

\[
 \frac1t\int_0^t E(s)\,ds
 \le\frac1t\int_0^tE_u(s)\,ds+\frac{\|u\|^2}{2nt}. \tag{8}
\]

Thus the flow has vanishing average excess loss against each fixed readout
on its own evolving features. If one fixed readout fits those features in
long-time average, then the actual time-average training loss tends to zero.
This condition is substantive and is not guaranteed by pointwise existence
of a different interpolating readout at each time.

For completeness, a sufficient bridge to pointwise fitting is: for some fixed
\(u\), \(\int_0^\infty E_u<\infty\), and \(G(t)\) is uniformly continuous.
Equation (5) then bounds \(w\) and makes \(E\) integrable. The readout
equation makes \(w\) Lipschitz, since \(g\) and the resulting residuals are
bounded. Boundedness of \(w,G\) and their uniform continuity make \(E\)
uniformly continuous. If a nonnegative uniformly continuous integrable
function failed to tend to zero, a sequence of disjoint intervals of fixed
positive length would each carry fixed positive mass; contradiction.
Therefore \(E(t)\to0\). Uniform continuity holds, for example, when
\(G(t)\) has a finite limit. These remain conditional feature assumptions.

## 4. Quantitative fitting condition using the actual key lag

Suppose on an interval \([0,T]\) that

\[
 \|w(t)\|/\sqrt n\le R_*,\qquad
 \lambda_{\min}\!\left(\frac{G(t)^\top G(t)}{mn}\right)\ge\lambda_*>0.
\]

The initialized value equation and the clock give

\[
 v(t):=\frac{\|V(t)\|_F}{\sqrt{mn}}
 \le2R_*\bigl(\tau(t)-1\bigr),\qquad
 \|Z\|_F\le(2\rho R_*+\alpha v)e\le4\rho R_*e.
\]

Here the bound on \(Z\) uses the Frobenius product inequality. Completing
the square in (1),

\[
 -4\|F\|_F^2+2\langle F,Z\rangle_F\le\|Z\|_F^2/4,
 \qquad D_w\ge4\lambda_* E,
\]

proves the useful bound

\[
 \dot E\le-D_A-4(\lambda_*-R_*^2e(t)^2)E. \tag{9}
\]

Consequently, if \(R_*^2e(t)^2\le(1-\delta)\lambda_*\) on the interval,
where \(0<\delta\le1\), then

\[
 E(t)\le e^{-4\delta\lambda_*t}\qquad(0\le t\le T). \tag{10}
\]

If the hypotheses persist for all time, they give exponential fitting. They
are sufficient, not necessary; the Gram condition is impossible when
\(m>n\). The hard unresolved work is to establish excitation and lag control
from the initialized closure for interesting multi-sample data. Equations
(2)–(4) alone do not establish either. Unlike simply postulating a positive
residual kernel, (9) isolates a measurable structural failure mode and a
quantitative tolerance for it.

## 5. What cannot be concluded, and one exact reachable fitting case

**Ambient-state loss is not a Lyapunov function.** Set
\(n=m=d=1\), \(x=y=1\), \(h=1/2\), \(k=-1/2\), \(w=1\),
\(v=W_0=0\), and any \(\tau\ge1\). Then
\(f=0,r=-1,d=1\), \(\dot w=\dot A=0\), and \(\dot v=2\).
Thus \(\dot z=\dot vkh=-1/2\) and \(\dot E=1>0\).
The strict sign persists under sufficiently small perturbations of this
state, including \(W_0\). This only refutes loss descent on the unrestricted
state space. The state has not been shown reachable from \(w=V=0,K=H\),
and the example does not refute monotonicity on initialized trajectories or
existence of a different Lyapunov function.

**Unconditional fitting for arbitrary supplied labels is false.** Every
forward map in this architecture is odd in \(x\). For the two examples
\(x,-x\) with equal labels \(+1,+1\), the initialized feature columns are
opposites and \(\dot w(0)=0\). The exact solution has
\(w=V=0\), constant \(A,H,K\), \(\tau=1+t\), and \(E=1\) for all time,
for every initialization. More generally, \(G(0)y=0\) traps the stated
initialization at this zero-readout solution. This is a reachable obstruction,
not an arbitrary-state construction; for the antipodal data it also reflects
architectural nonrealizability.

**One unit and one example fit exponentially.** Let \(n=m=1\), allow any
\(d\) with the stated input normalization, and suppose
\(W_0h(0)\ne0\). Put \(b=|W_0|\), \(s=\operatorname{sign}h(0)\),
\(c=\operatorname{sign}W_0\), and

\[
 H=sh,\quad K=sk,\quad q=cs\,v,\quad u=ycs\,w,
 \quad \Gamma=\tanh((b+qK)H),\quad \epsilon=1-u\Gamma.
\]

Here scalar \(H,K\) replace the matrix notation within this paragraph.
Initially \(H=K=|h(0)|>0\), \(q=u=0\), and \(\epsilon=1\).
Substitution in the exact equations gives

\[
 \begin{aligned}
 \dot u&=2\epsilon\Gamma,\\
 \dot q&=2\epsilon u(1-\Gamma^2),\\
 \dot H&=2\epsilon u(b+qK)(1-\Gamma^2)(1-H^2)^2,\\
 \dot K&=(|\epsilon|/\tau)(H-K),\qquad \dot\tau=|\epsilon|.
 \end{aligned}
\]

As long as \(\epsilon\ge0\), these equations preserve
\(u,q\ge0\), \(H\ge K>0\); all four variables are nondecreasing.
At \(H=K\), the difference derivative is \(\dot H\ge0\), proving the
filter-order assertion. At \(\epsilon=0\) the entire vector field vanishes,
so uniqueness prevents crossing to \(\epsilon<0\). Consequently
\(\Gamma(t)\ge\Gamma_0:=\tanh(|W_0h(0)|)>0\) and
\(\dot\Gamma\ge0\). Therefore

\[
 \dot\epsilon=-\dot u\Gamma-u\dot\Gamma
 \le-2\Gamma_0^2\epsilon,\qquad
 E(t)=\epsilon(t)^2\le e^{-4\Gamma_0^2t}. \tag{11}
\]

The nonzero condition holds almost surely under the stipulated scalar
Gaussian initialization. This proof uses a reachable sign-preserving cone:
the key stays between its initial value and the growing current feature.
That cone, rather than an imported dense-flow property, makes all learning
channels cooperate. There is no claim that this cone extends to general
width or multiple labeled examples.

## Frozen conclusion

Proved: exact signed memory work (1), passive key filtering (2)–(4), exact
endogenous-feature comparator balance (5), global existence and time-average
control (6)–(8), conditional robust fitting (9)–(10), and almost-sure scalar
one-sample exponential fitting (11). Disproved: ambient-state loss monotonicity
and fitting for arbitrary labeled sphere data. Open: a state-only Lyapunov
for general initialized trajectories, reachable loss monotonicity, and
self-generated excitation plus lag control for realizable multi-sample data.
The exact balance laws alone do not show that the memory mechanism improves
learning over a readout with fixed or otherwise evolving features.

## Post-freeze extensions: a quantitative certificate and the selected scalar function

The independent first version was frozen with SHA256
`cdf2e62938f2d34b3ef65b3493f236f8815a9b1e4ccb54072ca1b3dc6cf5888c`.
The supervisor subsequently suggested the valid sharpening
\(\|w\|^2/n\le t\), now incorporated into (7). The extensions below were
derived after that freeze without reading another route.

**An optimized finite-time fitting certificate.** The complete trajectory up
to a fixed horizon defines

\[
 b_t=\int_0^t\frac{G(s)y}{mn}\,ds,\qquad
 C_t=\int_0^t\frac{G(s)G(s)^\top}{mn^2}\,ds.
\]

Integrating (5) and dropping its nonnegative terms gives, for every constant
\(u\),

\[
 \int_0^t E(s)\,ds
 \le t-2u^\top b_t+u^\top\left(C_t+\frac{I}{2n}\right)u.
\]

The matrix in parentheses is positive definite. Completing the square and
choosing \(u_t=(C_t+I/(2n))^{-1}b_t\) proves

\[
 \int_0^t E(s)\,ds
 \le t-b_t^\top\left(C_t+\frac{I}{2n}\right)^{-1}b_t. \tag{12}
\]

The chosen comparator is constant throughout each fixed-horizon calculation;
its dependence on the completed horizon is only a diagnostic choice. No
future-dependent input enters the closure. Persistent label-feature
correlation produces a quantitative improvement over the zero predictor.
If the subtracted term is \(t-o(t)\), time-average fitting follows. If labels
are representable by unrelated readouts at different times but no common
readout, (12) need not approach zero. The certificate describes the intrinsic
readout mechanism but does not by itself explain why feature motion should
improve this certificate.

**The scalar fitting trajectory selects a finite limiting function and a
permanently delayed key.** In the one-unit, one-example case of (11),
\(u\Gamma\le1\) and \(\Gamma\ge\Gamma_0\) give
\(0\le u\le1/\Gamma_0\). Also,

\[
 \int_0^\infty\epsilon(t)\,dt\le\frac1{2\Gamma_0^2},\qquad
 q(t)\le\frac1{\Gamma_0^3},\qquad
 \tau_\infty\le1+\frac1{2\Gamma_0^2}.
\]

The value bound follows by integrating
\(\dot q\le2\epsilon/\Gamma_0\). The signed training preactivation
\(a=Ax/\sqrt d\) satisfies

\[
 \left|\dot a\right|
 \le\frac{2\epsilon}{\Gamma_0}
       \left(b+\frac1{\Gamma_0^3}\right).
\]

Thus \(a\) converges to a finite \(a_\infty\); the nonnegative transformed
variables \(u,q,H,K\) are bounded and nondecreasing, hence converge.
Consequently all original parameters converge, and
\(u_\infty\Gamma_\infty=1\). In fact \(H\) increases strictly for every
positive finite time: \(u>0\), and finite tanh preactivations make all its
other factors positive while \(\epsilon>0\). The latter cannot vanish at
finite time, because reaching a stationary zero-residual state would violate
backward local uniqueness. Thus \(H_\infty>H(0)\). Formula (4) yields

\[
 H_\infty-K_\infty
 =\frac1{\tau_\infty}\int_0^\infty\tau(s)\dot H(s)\,ds
 \ge\frac{H_\infty-H(0)}{\tau_\infty}>0. \tag{13}
\]

Successful fitting therefore does not require the key to catch the current
feature. The finite accumulated residual clock preserves a positive lag.

Only the component of \(A\) along the training input changes. Writing
\(a_0(x')=A(0)x'/\sqrt d\), one has exactly

\[
 A_\infty=A(0)+(a_\infty-a_0(x))\frac{x^\top}{\sqrt d}.
\]

For every unseen input \(x'\), the limiting predictor is consequently

\[
 f_\infty(x')
 =y\,
 \frac{\tanh\!\left[B_\infty\tanh\!\left(
 a_0(x')+(a_\infty-a_0(x))\frac{x^\top x'}d\right)\right]}
 {\tanh\!\left[B_\infty\tanh(a_\infty)\right]},
 \qquad B_\infty=W_0+v_\infty k_\infty. \tag{14}
\]

The denominator is nonzero because its absolute value is
\(\Gamma_\infty\ge\Gamma_0\). Equation (14) is a characterization in
terms of the dynamically selected limiting scalars, not a closed formula for
those scalars. It proves interpolation at \(x\), prediction \(-y\) at
\(-x\), and retention of the initialized read-in components orthogonal to
the training input. There is no accuracy claim for other unseen labels.
