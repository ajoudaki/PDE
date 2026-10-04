# A finite scalar terminal model for the actual q=1 closure

Root derivation, 2026-09-30. Conditional theorem; see
`TERMINAL_SCALAR_CHECK.md` for its internal check and source hashes.
This is a new derivation from the current manuscript's q=1 equations.
No earlier study is a scientific input. The result is a local-to-all-time
terminal compression theorem, not a complete initialization-to-endpoint
sublinear-state theorem.

## 1. Exact finite aggregate equation

Use the manuscript's exact finite-width q=1 model: two tanh hidden
layers, m normalized training inputs, n neurons per layer, residual r=f-y,
loss L=||r||^2/m, rho=||r||/sqrt(m), and

\[
B=W_0+\frac1{mn}\sum_bv_bk_b^T,\quad
h_a=\tanh(Ax_a/\sqrt d),\quad g_a=\tanh(Bh_a),
\]
\[
f_a=w^Tg_a/n,\quad d_a=w\odot(1-g_a^2),\quad
\ell_a=(1-h_a^2)\odot B^Td_a.
\]

The full autonomous state equations are

\[
\dot w=-\frac2m\sum_a r_ag_a,\qquad
\dot A=-\frac2m\sum_a r_a\ell_a x_a^T/\sqrt d,
\]
\[
\dot v_a=-2r_ad_a,\qquad
\dot k_a=\frac{\|r\|}{\sqrt m\tau}(h_a-k_a),\qquad
\dot\tau=\frac{\|r\|}{\sqrt m}.
\]

For the initialization statement below, w(0)=0, v_a(0)=0,
k_a(0)=h_a(0), and tau(0)=1. The terminal theorem itself applies at a
reached handoff and does not use the initialization law.

The manuscript's raw moments give k=bar h_0/tau, v=-2 bar delta_0, so

\[
\dot B=-\frac2{mn}\sum_b r_b d_b k_b^T
+\frac{\rho}{mn\tau}\sum_bv_b(h_b-k_b)^T.
\tag{1}
\]

Set I_ab=x_a^Tx_b/d and define the scalar array and scalar vector

\[
C_{ab}=\frac2m\left[
\frac{g_a^Tg_b}{n}
+I_{ab}\frac{\ell_a^T\ell_b}{n}
+\frac{d_a^Td_b}{n}\frac{k_b^Th_a}{n}\right],
\tag{2}
\]
\[
b_a=\frac1{m\sqrt m\tau}\sum_b
\frac{d_a^Tv_b}{n}\frac{(h_b-k_b)^Th_a}{n}.
\tag{3}
\]

In (3) the summation index b is an example index; the bold-free symbol b
on the left names an m-vector. No new population coordinate is introduced.
The exact residual dynamics are

\[
\dot r=-C(X)r+\|r\|b(X),
\tag{4}
\]

where X=(A,w,(v_a,k_a)_a,tau) is the full q=1 state and norms on r are
ordinary Euclidean norms. To verify every contribution, differentiate

\[
\dot f_a=\dot w^Tg_a/n+d_a^T\dot B h_a/n
              +\ell_a^T\dot A x_a/(n\sqrt d).
\]

Substitution of wdot, Adot and the residual-driven part of (1) gives
respectively the first, second and third terms of (2). The remaining part
of (1) gives rho times the key-motion term. Since
rho=||r||/sqrt(m), the latter is exactly ||r||b in (3).

Thus a loss-relevant aggregate description needs an m by m generally
nonsymmetric matrix and an additional m-vector, not only a symmetric kernel.
The current-key pairing k_b^Th_a need not be symmetric or positive.
The key-motion contribution is first order in the residual norm, even near
an interpolating state with a nonzero accumulated memory. Dropping it is not
automatically a second-order approximation.

Both C(X) and b(X) are smooth functions of the full finite state when tau>0.
Moreover the full dynamics have the exact factorization

\[
\dot X=\sum_{a=1}^m r_a F_a(X)+\|r\|F_0(X),
\tag{5}
\]

with smooth coefficient fields on tau>0: put the readout, read-in and value
velocities in F_a, the key/clock velocities in F_0, and their stated m and
sqrt(m) factors in these fields. In particular every state coordinate stops
when r=0. Equation (5), rather than physical-time analyticity, is the
structural input to the theorem below.

At the prescribed zero-readout initialization, C_0=(2/m)[g_a^Tg_b/n] and
b_0=0. The matrix and vector derivatives at that instant also vanish:
Adot=vdot=kdot=0, hence gdot=0; d and ell are O(t), so their quadratic
terms are O(t^2), and b contains both v and h-k. Thus (4) initially agrees
with its frozen-C_0 version through the first derivative of its vector field
along the trajectory. This onset fact alone proves no long-time accuracy.

## 2. A checkable terminal hypothesis

Choose any reached handoff time and reset it to t=0. Let X_0 be that state,
r_0 its residual, R=||r_0||, C_0=C(X_0), b_0=b(X_0). This does not require
knowing the future endpoint. Suppose a closed ball of radius a>0 about X_0
lies in the admissible domain and has the following bounds, in a stated
finite-dimensional state norm:

\[
\|\dot X\|\le H\|r\|,
\tag{6}
\]
\[
\|C(X)-C_0\|_{\rm op}+\|b(X)-b_0\|
 \le J\|X-X_0\|.
\tag{7}
\]

For finite n these hold with finite H,J on every sufficiently small compact
ball, by (5) and smoothness. No width-uniform bound is asserted by that fact.
Assume the aggregate dissipation margin

\[
\lambda_0:=\lambda_{\min}\!\left(\frac{C_0+C_0^T}{2}\right)
                -\|b_0\|>0,
\tag{8}
\]

and the small-tail conditions

\[
\frac{2HR}{\lambda_0}<a,\qquad
\frac{2JHR}{\lambda_0}<\frac{\lambda_0}{2}.
\tag{9}
\]

Zero J or H causes no problem; inequalities containing those constants are
read literally. R=0 is the stationary case. These assumptions are a
certificate for a particular terminal region, not a universal fitting
assertion from the prescribed initialization. They can hold on an open
finite-state region with a nonsymmetric C and nonzero b. No special symmetry
of training inputs is required in the statement.

## 3. Terminal scalar closure and theorem

Discard the full evolving state after the handoff. Retain only r_0, C_0,b_0
and, optionally, tau_0. Evolve the autonomous scalar system

\[
\dot{\widehat r}=-C_0\widehat r+\|\widehat r\|b_0,
\qquad \widehat r(0)=r_0,
\tag{10}
\]
\[
\dot{\widehat\tau}=\|\widehat r\|/\sqrt m,
\qquad \widehat\tau(0)=\tau_0,\quad
\widehat L=\|\widehat r\|^2/m.
\tag{11}
\]

It has m moving scalars, or m+1 with the clock, and m^2+m fixed scalar
coefficients. Its right-hand side costs O(m^2) arithmetic per evaluation.
There is no retained population, matrix action W0, neuronwise state or future
trace in this terminal evaluator. The fixed data are aggregates at the
handoff; producing them without full earlier training is a separate problem.

**Theorem.** Under (6)--(9), the full q=1 solution remains in the ball for
every t>=0, converges to a finite interpolating state, and

\[
\|r(t)\|\le R e^{-\lambda_0t/2},\qquad
\|\widehat r(t)\|\le R e^{-\lambda_0t}.
\tag{12}
\]

Both systems stop at zero residual. They have equal initial residual
velocity. At equal physical times,

\[
\sup_{t\ge0}\|r(t)-\widehat r(t)\|
 \le\frac{JH}{\lambda_0^2}R^2,
\tag{13}
\]
\[
\sup_{t\ge0}|L(t)-\widehat L(t)|
 \le\frac{2JH}{m\lambda_0^2}R^3,
\tag{14}
\]
\[
\sup_{t\ge0}|\tau(t)-\widehat\tau(t)|
 \le\frac{4JH}{\sqrt m\lambda_0^3}R^2.
\tag{15}
\]

The bounds include the infinite physical-time tail. They do not require
identifying two differently parametrized trajectories by their clock values.
Constants depend on the certified terminal tube, data and initialization;
population or width-uniform use requires bounds uniform in that setting.

### Proof

For t before first ball exit, let z=||r|| and q=||X-X_0||. At positive z,
(4), (7) and (8) give

\[
\dot z\le-(\lambda_0-Jq)z.
\tag{16}
\]

Stop also before Jq reaches lambda_0/2. On the stopped interval,
z<=R exp(-lambda_0 t/2), and (6) gives

\[
q(t)\le\int_0^tH z(u)du
\le\frac{2HR}{\lambda_0}(1-e^{-\lambda_0t/2}).
\tag{17}
\]

The strict inequalities (9) rule out either exit. The full state stays in a
compact subset of tau>0; its locally Lipschitz vector field consequently
continues for all physical times. Its speed is integrable by (6) and (12),
so every state coordinate converges. The residual tends to zero. At z=0
the field is zero, so the same bounds hold by continuity.

For any u,v in R^m, set T(u)=-C_0u+||u||b_0. The reverse triangle
inequality and Cauchy--Schwarz show

\[
(u-v)^T[T(u)-T(v)]
\le-\lambda_0\|u-v\|^2.
\tag{18}
\]

Thus (10) is globally Lipschitz, strictly contractive, and satisfies its
bound in (12) by taking v=0. Regard the full residual equation as
rdot=T(r)+E(t). From (7), (12) and (17), with lambda=lambda_0/2,

\[
\|E(t)\|
\le Jq(t)\|r(t)\|
\le\frac{2JH}{\lambda_0}R^2 e^{-\lambda t}.
\tag{19}
\]

The dropped factor 1-exp(-lambda t) only weakens this bound. Applying (18)
to the difference, or differentiating a regularized norm and passing to its
limit, gives

\[
\|r(t)-\widehat r(t)\|
\le\frac{4JH}{\lambda_0^2}R^2
       (e^{-\lambda_0t/2}-e^{-\lambda_0t}).
\tag{20}
\]

For q=exp(-lambda_0 t/2) in [0,1], q-q^2<=1/4; this proves (13).
Since both residual norms are at most R, the difference of their squared
norms is at most 2R times (13), proving (14). Finally integrate (20):

\[
\int_0^\infty\|r-\widehat r\|dt
\le\frac{4JH}{\lambda_0^3}R^2.
\]

The norm is 1-Lipschitz, and both clocks integrate the residual norm divided
by sqrt(m), which proves (15). All comparisons use the same t.

## 4. Other scalar observables can be appended

Suppose a scalar observable O(X) has an exact equation

\[
\dot O=p(X)^Tr+\|r\|q(X),
\tag{21}
\]

with ||p(X)-p_0||+|q(X)-q_0|<=J_O||X-X_0|| in the same tube.
For a smooth O this follows by differentiating (5); p and q are finitely
many aggregate derivatives, not additional moving fields. Evolve one more
scalar using frozen p_0,q_0 and the residual in (10), initialized at O(X_0).
Direct subtraction and integration yield

\[
\sup_{t\ge0}|O(X(t))-\widehat O(t)|
\le\left[\frac{4J_OH}{\lambda_0^2}
+\frac{4JH(\|p_0\|+|q_0|)}{\lambda_0^3}\right]R^2.
\tag{22}
\]

Indeed the first integrand is at most J_O q(t)||r(t)||, whose integral
is at most 4J_O H R^2/lambda_0^2 using (17) and (12); the second is
(||p_0||+|q_0|)||r-rhat|| and uses (20). This bound is conservative.
The appended scalar plateaus because its velocity is integrable and vanishes
at zero residual. A finite list of training Gram entries or passive-query
predictions is covered if its coefficient hypotheses are checked. Loss gets
the stronger cubic bound (14); arbitrary observables do not inherit it.

## 5. Why residual extinction alone is weaker

First, a frozen-kernel terminal model generally omits the term ||r||b_0.
For one scalar residual with a>b>0 and initial R>0, the true homogeneous
model rdot=-(a-b)r and the omitted-b model rdot=-ar both fit and stop.
At any fixed t>0 their loss difference is

\[
R^2(e^{-2(a-b)t}-e^{-2at}),
\]

which is order R^2, not the order R^3 in (14). Matching the complete leading
residual generator is a quantitative improvement, not just enforced fitting.
In q=1, nonzero b at interpolating states is allowed by (3); setting r=0
does not force either v or h-k to vanish. This is an algebraic statement,
not a claim that every such state is reached from the chosen initialization.

Second, decay of loss alone need not make the activity clock finite.
The scalar system rdot=-r^2 for r>=0 has r=1/(1+t), loss ->0, but
integral r dt diverges. Bounds like (8)--(9) or another integrable activity
criterion are necessary for the finite-clock explanation.

Third, a finite activity interval does not by itself give analytic smoothness
in activity time. Consider the stable two-dimensional residual system

\[
\dot r=-(\lambda I+\omega J_2)r,\quad
J_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad \lambda>0,
\]

and an auxiliary coordinate zdot=r_1, with R=||r(0)||>0. Its activity clock
s=integral ||r||dt has finite endpoint R/lambda. But the direction r/||r||
rotates with angle proportional to log(1-lambda s/R), infinitely often near
that endpoint when omega!=0; dz/ds has no limit. This is an exactly solvable
benchmark, not a claimed q=1 trajectory. It disproves the inference that
finite activity alone supplies the regularity needed for efficient polynomial
compression. Loss itself is R^2 exp(-2lambda t), so observable choice matters.

## 6. What has and has not been compressed

The late q=1 dynamics admit an actual autonomous scalar evaluator with
m moving residuals and optional scalar observations. It preserves the exact
first residual velocity, residual-zero stopping, exponential fitting under a
finite-dimensional margin, all-time physical loss accuracy and clock accuracy.
Its data are C_0,b_0 and the declared observation coefficients at a handoff.

This is a valid terminal module. It does not yet supply those coefficients,
or an accurate entire early loss curve, from a sublinear initialization-only
scalar system. Running the full population to get them would fail the desired
end-to-end resource contract. Nor does local smoothness yield width-uniform
H,J or the population q=1 limit. These are explicit missing bridges.

At root-width accuracy epsilon~n^(-1/2), the terminal moving count is O(m)
for fixed m, but that fact is not an end-to-end sublinear-width theorem.
The full research target remains open until an admissible accurate early
aggregate closure and its initialization/cost bounds are supplied.
