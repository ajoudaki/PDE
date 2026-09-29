# One-sample unit-label range: scalar alignment and all-time comparison

Scoped proof check, 28 September 2026. Inputs were the supervisor's proposed
argument, `OLD_CLOCK_ROUTE.md`, `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`,
`SMALL_LABEL_ENERGY.md`, the endpoint lemmas of
`SMALL_LABEL_SPECTRAL_SLACK.md`, `docs/notation.qmd`, and the
`solve-math-rigorously` skill. No other study, experiment, or maintained-file
change was used. This is an internal proof check, not a promotion review.

**Verdict.** The proposed argument is valid for one sample and exactly zero
initial readout. It removes the small-label restriction throughout
`0<|y|<=1`, for every memory order above a constant threshold independent of
width and label size. No exponential decay assumption on the closure is
needed. The stronger defect and comparison estimates are

\[
 \int_0^\infty e_E(t)\,dt
 \le \frac{C Y^2(1+\sqrt nY^2)}{P(P+1)},
 \tag{1}
\]
\[
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
 \le \frac{C Y^2(1+\sqrt nY^2)}{P(P+1)}
             e^{CY+C\sqrt nY^2}.
 \tag{2}
\]

Constants depend only on the fixed depth `L`, input norm `X`, initialized
hidden operator bound `K`, and initial feature lower bound `lambda`.
In particular, after enlarging `C`,

\[
 P\ge\max\{P_0,(1+\sqrt n)e^{C\sqrt n}\}
 \quad\Longrightarrow\quad
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))\le C/P.
 \tag{3}
\]

The constant in (3) is uniform in width, time, and `0<Y<=1`, on the
displayed order/width region. This is not a theorem uniform over all widths
at each fixed `P`.

The proof first preserves the scalar readout alignment using the integrated
defect, closes an activity bound, then uses the constant scalar residual
direction to obtain two continuous `H1` histories. Residual damping finally
turns the stronger defect into (2).

## 1. Setup and the activity-capped estimates

There is one datum `(x,y)`, with

\[
 X=\|x\|_2/\sqrt d<\infty,\quad
 0<Y=|y|\le1,\quad \sigma=\operatorname{sign}y.
\]

Use tanh at every layer, `L>=2`, canonical mobilities, and the loss
`(f-y)^2`. Both systems start at the same finite parameter, with

\[
 w_0=0,\qquad
 \max_{2\le\ell\le L}\|W_{0,\ell}\|_{\rm op}\le K,\qquad
 H_0:=\|h_L(0)\|_2^2/n\ge\lambda>0.
 \tag{4}
\]

Necessarily `lambda<=1`. No bound on the unnormalized first matrix is
required for the constants below. Its entries are finite for continuation.
All undecorated quantities in Sections 1--4 belong to the actual autonomous
old-clock closure. Write

\[
 r=f-y,\quad\rho=|r|,\quad s(t)=\int_0^t\rho(u)\,du,\quad
 \tau=1+s,\quad e_E=\sum_{\ell=2}^L\|E_\ell\|_F.
\]

The supplied exact physical and residual equations are

\[
 \dot\theta=F(\theta)+E,\quad E_1=E_w=0,\qquad
 \dot r=-2\Gamma r+JE,
 \tag{5}
\]
\[
 \Gamma=H+
 X^2\frac{\|\delta_1\|_2^2}{n}
 +\sum_{\ell=2}^L
       \frac{\|\delta_\ell\|_2^2}{n}
       \frac{\|h_{\ell-1}\|_2^2}{n},
 \qquad H=\|h_L\|_2^2/n.
 \tag{6}
\]

Stop initially at `s<=S=4Y/lambda`, and set `A=1+S`. The capped estimates
in Section 2 of `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md` apply independently of
any Gram bound or residual decay. In their recursions set

\[
 \beta_L=2S,\quad D_\ell=K+2A\beta_\ell,\quad
 \beta_{\ell-1}=D_\ell\beta_\ell.
\]

They give `||W_l||_op<=D_l`, `||delta_l||_2/sqrt(n)<=beta_l`, and

\[
 Z_\ell(t):=\int_0^{\tau(t)}
       \frac{\|\partial_\xi h_\ell\|_2^2}{n}\,d\xi
       \le Z_\ell^*,\qquad
 \int_0^t e_E\le
 \frac{A\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}}
      {\sqrt{P(P+1)}}.
 \tag{7}
\]

The explicit forward recursion is

\[
 Z_1^*=4SX^4\beta_1^2,\qquad
 Z_\ell^*=3\{4S\beta_\ell^2+
                 (D_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}^*\}.
\]

Since `S=(4/lambda)Y` and `Y<=1`, finite downward and upward induction
prove, with common constants independent of `n,P,Y`,

\[
 D_\ell\le D_*,\qquad \beta_\ell\le C_\beta Y,
 \qquad Z_\ell^*\le C_ZY^3,
 \qquad \int_0^t e_E\le C_EY^3/P.
 \tag{8}
\]

These bounds hold on every regular capped interval. In particular,
`C_EY^3` is justified uniformly throughout `0<Y<=1`, not just as a
small-`Y` asymptotic.

The raw moment ODE is locally Lipschitz on `tau>0`, and every raw velocity
vanishes at `rho=0`. Local uniqueness, also applied backward from a finite
time, therefore excludes reaching zero residual from `rho(0)=Y>0` at a
finite regular time. Hence

\[
 r=-\sigma\rho,\qquad \rho=Y-\sigma f>0
 \tag{9}
\]

on every such interval. Activity-capped raw states remain bounded at each
fixed `n,P` by the supplied moment representations. Thus a finite maximal
existence endpoint before activity exit is impossible.

## 2. The quotient at zero time and its continued positivity

Put

\[
 B(t)=\|w(t)\|_2/\sqrt n,\qquad g(t)=\sigma f(t),\qquad
 q(t)=g(t)/B(t)\quad\hbox{when }B(t)>0.
\]

The unchanged readout equation and (9) give

\[
 \dot w=2\sigma\rho h_L.
\]

Since the physical parameter path is continuously differentiable at zero,

\[
 w(t)=2\sigma Yh_L(0)t+o(t),\quad
 B(t)=2Y\sqrt{H_0}\,t+o(t),\quad
 g(t)=2YH_0t+o(t).
 \tag{10}
\]

These limits are at each fixed `n,P,Y`; uniform error terms are unnecessary.
They prove `B(t)>0` for sufficiently small positive time and
`q(0+)=sqrt(H_0)`.

Where `B>0`, direct differentiation yields

\[
 \dot B=2\rho q,\qquad
 \dot g=2\rho\Gamma+\sigma JE,
 \qquad
 \dot q=\frac{2\rho}{B}(\Gamma-q^2)+\frac{\sigma JE}{B}.
 \tag{11}
\]

Cauchy--Schwarz gives `q^2=f^2/B^2<=H`, while (6) gives `Gamma>=H`.
The first term of `dot q` is therefore nonnegative.

The apparent division by small `B` in the second term is harmless for a
specific reason: the *instantaneous* backward recurrence, using the capped
hidden operator bounds, gives

\[
 \frac{\|\delta_\ell(t)\|_2}{\sqrt n}
       \le M_\ell B(t),\qquad M_\ell\le D_*^{L-\ell}.
\]

In each hidden block
`J_l E_l=delta_l^T E_l h_(l-1)/n`, so for a common `C_J`,

\[
 |JE|\le C_J B e_E,\qquad \dot q\ge-C_J e_E.
 \tag{12}
\]

Dividing the time-independent cap `beta_l` by `B(t)` would not justify
(12); the instantaneous recurrence is essential. Integrating (12) from
positive time and then using (10) gives

\[
 q(t)\ge\sqrt{H_0}-C_J\int_0^t e_E
       \ge\sqrt\lambda-C_JC_EY^3/P.
 \tag{13}
\]

Choose an integer `P_0` satisfying

\[
 P_0\ge\max\{1,8C_JC_E/\sqrt\lambda\}.
 \tag{14}
\]

For `P>=P_0`, (13) gives in particular `q>=sqrt(lambda)/2`. This estimate
holds for the entire capped interval: starting with the interval on which
`B>0`, (11) makes `B` strictly increasing there. At any proposed positive
endpoint, `B` is bounded below by its value at an earlier positive time,
so it cannot return to zero. Continuity therefore extends the quotient
argument until activity exit or the maximal existence endpoint. In
particular,

\[
 H(t)\ge\lambda/4,\qquad
 0<g(t)<Y,\qquad B(t)=g(t)/q(t)\le2Y/\sqrt\lambda.
 \tag{15}
\]

## 3. Closing activity and obtaining convergence

Equations (5), (9), (12), and (15) imply

\[
 \dot\rho\le-\frac\lambda2\rho+C_FY e_E,
 \qquad C_F=2C_J/\sqrt\lambda.
 \tag{16}
\]

Integrate and discard the nonnegative terminal residual. By (8), (14),
and `Y<=1`,

\[
 \begin{split}
 s(t)&\le\frac2\lambda
       \left(Y+C_FY\int_0^t e_E\right)\\
 &\le\frac{2Y}{\lambda}
       \left(1+\frac{C_FC_EY^3}{P}\right)
 \le\frac{5Y}{2\lambda}<\frac{3Y}{\lambda}<S.
 \end{split}
 \tag{17}
\]

Thus activity cannot first attain `S`; capped continuation excludes any
earlier finite maximal endpoint. The closure is global, with
`s(infinity)<=5Y/(2lambda)`, and (8), (15) hold for all time.

The canonical dense velocity satisfies `||F||_mob<=C rho` on these bounds,
and `||E||_mob<=e_E`. Hence

\[
 \int_0^\infty\|\dot\theta\|_{\rm mob}\,dt
       \le Cs(\infty)+\int_0^\infty e_E<\infty.
\]

At each finite width the physical parameters converge. Their residual
converges by continuity of the network, and a positive limiting absolute
residual would contradict finite activity. The limit therefore interpolates.
This argument proves fitting without asserting an exponential closure rate.

For the dense trajectory, repeat (10)--(13) with `E=0`. The alignment is
nondecreasing, so `H_D>=H_0>=lambda` and

\[
 \rho_D(t)\le Ye^{-2\lambda t},\qquad
 \int_0^\infty\rho_D(t)\,dt\le Y/(2\lambda).
 \tag{18}
\]

The same stopped continuation argument proves global dense existence,
finite parameter variation, and interpolation. Both trajectories satisfy
the common operator and backward bounds (8).

## 4. Two regular histories give a second power of the memory order

Let `Pi_P` be projection onto polynomials of degree below `P` on
`[0,tau]`, and let a star denote its value at the current endpoint. The
endpoint lemmas proved in Section 2 of `SMALL_LABEL_SPECTRAL_SLACK.md` are

\[
 \|(\Pi_P b)(\tau)\|_2\le C\sqrt P\sup_\xi\|b(\xi)\|_2,
 \tag{19}
\]
\[
 \|h(\tau)-(\Pi_Ph)(\tau)\|_2
 \le C\sqrt{\tau/P}\,
                 \|\partial_\xi h\|_{L^2(0,\tau;\mathbb R^n)}.
 \tag{20}
\]

The second identity follows by integrating the endpoint Legendre kernel:
its primitive is `(p_P+p_(P-1))/2`, whose squared integral is
`tau(1/(2P+1)+1/(2P-1))/4`. Thus (20) applies to the continuous
forward prefix. The first lemma is the scalar kernel's `L1` bound
`C sqrt(P)`, so it applies to vector histories by the integral triangle
inequality; it requires no backward derivative. Both are valid for `P=1`.

Here `b_l=(r/rho)delta_l=-sigma delta_l`. Its entire history, including
the zero prefix, has normalized supremum at most `CY`. By (8), (19),
and (20),

\[
 \frac{\|b_\ell-b_\ell^*\|_2}{\sqrt n}\le C\sqrt P\,Y,
 \qquad
 \frac{\|h_{\ell-1}-h_{\ell-1}^*\|_2}{\sqrt n}
                      \le CY^{3/2}/\sqrt P.
\]

Use these in the exact defect formula

\[
 E_\ell=\frac{2\rho}{n}
       (b_\ell-b_\ell^*)(h_{\ell-1}-h_{\ell-1}^*)^T
\]

to obtain the uniform pointwise bound

\[
 e_E\le CY^{5/2}\rho.
 \tag{21}
\]

No smallness relative to `lambda` is asserted in (21), and no exponential
closure estimate is deduced from it. Its purpose is derivative control.
The canonical updates, (8), (21), and `Y<=1` give

\[
 \|\dot W_1\|_F/\sqrt n\le CY\rho,
 \quad\sum_{\ell=2}^L\|\dot W_\ell\|_F\le CY\rho,
 \quad\|\dot w\|_2/\sqrt n\le2\rho,
 \quad\|\dot w\|_\infty\le2\rho.
 \tag{22}
\]

Differentiating the forward recurrence and using the bounded operator
norms proves

\[
 \max_\ell\frac{\|\dot z_\ell\|_2+\|\dot h_\ell\|_2}{\sqrt n}
                                                   \le CY\rho.
 \tag{23}
\]

At a lower backward layer, its full carrier
`W_(l+1)^T delta_(l+1)` has Euclidean norm at most `C sqrt(n)Y`.
Its supremum norm is bounded by the same quantity. Since
`|tanh''|<=2`, the differentiated gate contributes at most
`C sqrt(n)Y * CY rho` in normalized Euclidean norm. The differentiated
matrix contributes at most `CY rho * CY`, and the next backward derivative
is multiplied by a bounded operator. At the top layer, the readout
derivative contributes `2rho`, and the gate term has the same bound.
Finite downward induction therefore proves

\[
 \max_\ell\frac{\|\dot\delta_\ell\|_2}{\sqrt n}
                       \le C(1+\sqrt nY^2)\rho.
 \tag{24}
\]

The scalar direction in (9) is constant, so division by the closure's
own `rho` gives

\[
 \frac{\|\partial_\xi b_\ell\|_2}{\sqrt n}
                    \le C(1+\sqrt nY^2).
 \tag{25}
\]

There is no derivative of a varying residual direction and no residual
ratio between trajectories. At zero initial readout every initial
`delta_l` vanishes, so the backward history joins its zero prefix
continuously. The forward history joins its constant prefix continuously.
Both histories are therefore `H1` on each complete interval `[0,tau(t)]`,
and extend continuously to the bounded terminal clock interval. Equations
(8), (17), (25) give

\[
 \int_0^{\tau(t)}\frac{\|h_\ell'\|_2^2}{n}\,d\xi\le CY^3,
 \qquad
 \int_0^{\tau(t)}\frac{\|b_\ell'\|_2^2}{n}\,d\xi
                       \le CY(1+\sqrt nY^2)^2.
 \tag{26}
\]

For a vector-valued `H1` history `a`, the Legendre tail estimate is

\[
 \int_0^\tau\frac{\|(I-\Pi_P)a\|_2^2}{n}\,d\xi
 \le\frac{1}{P(P+1)}
    \int_0^\tau\xi(\tau-\xi)\frac{\|a'\|_2^2}{n}\,d\xi
 \le\frac{A^2}{4P(P+1)}
    \int_0^\tau\frac{\|a'\|_2^2}{n}\,d\xi.
 \tag{27}
\]

Denote the normalized squared tails on the left by `D_h,D_b`. The exact
growing-history identities are `dot D_h=rho||h-h*||_2^2/n` and its
backward counterpart. The rank-one Frobenius identity and time
Cauchy--Schwarz consequently give

\[
 \int_0^t\|E_\ell\|_F\,du
                  \le2\sqrt{D_{b,\ell}(t)D_{h,\ell-1}(t)}.
 \tag{28}
\]

Apply (26)--(27) to (28), sum over fixed depth, and let `t` increase to
infinity. This proves (1). The absence of a prefix jump is precisely
where the assumption `w_0=0` enters this full `P^-2` argument.

## 5. Residual damping comparison without small-label absorption

For completeness, the following direct comparison verifies that the
small-label restriction in `SMALL_LABEL_ENERGY.md` is unnecessary once
the common boundedness, positive readout Gram, and finite activity have
been established. Define

\[
 x(t)=\frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F,
 \quad z(t)=\frac{\|\widehat w-w_D\|_2}{\sqrt n},\quad d(t)=x(t)+z(t).
\]

Here `x(t),z(t)` are scalar discrepancies, distinct from the datum and
layer-indexed preactivations. This sum dominates the mobility Hilbert
distance `d_n`. Forward recurrence and tanh's Lipschitz constant give

\[
 \max_\ell\frac{\|\widehat z_\ell-z_{\ell,D}\|_2
                         +\|\widehat h_\ell-h_{\ell,D}\|_2}{\sqrt n}
                                                        \le Cx.
 \tag{29}
\]

The current dense backward carriers have supremum norm at most
`C sqrt(n)Y`. Subtract the backward recurrences, placing the dense carrier
in the gate-difference term. The readout difference contributes `z`, the
matrix difference contributes at most `CYx`, the gate difference
contributes at most `C sqrt(n)Yx`, and the next backward difference is
multiplied by a bounded operator. Thus

\[
 b(t):=\max_\ell
       \frac{\|\widehat\delta_\ell-\delta_{\ell,D}\|_2}{\sqrt n}
                    \le C[z+\sqrt nYx].
 \tag{30}
\]

The explicit tangent Gram (6), with backward norms at most `CY`, then gives

\[
 |\widehat\Gamma-\Gamma_D|
        \le C[x+Yb+Y^2x]
        \le C[(1+\sqrt nY^2)x+Yz].
 \tag{31}
\]

Set `v=|f_hat-f_D|`, `Q(t)=integral_0^t v`, and
`epsilon(t)=integral_0^t e_E`. Subtract (5) between the two paths and use
`Gamma_hat>=lambda/4` and `|J_hat E|<=CY e_E`. The norm's upper derivative
satisfies

\[
 D^+v\le-\frac\lambda2v
       +C\rho_D[(1+\sqrt nY^2)x+Yz]+CY e_E.
\]

At a zero of `v`, this follows by the triangle inequality for its
derivative; equivalently regularize by `sqrt(v^2+eta^2)` and let `eta`
decrease to zero. Since `v(0)=0`, integration yields

\[
 Q(t)\le C\int_0^t\rho_D[(1+\sqrt nY^2)x+Yz]\,du
                           +CY\epsilon(t).
 \tag{32}
\]

Subtracting readout equations, and then the first and hidden parameter
equations, gives respectively

\[
 z(t)\le2Q(t)+C\int_0^t\rho_Dx\,du,
\]
\[
 x(t)\le CYQ(t)+C\int_0^t\rho_D[b+Yx]\,du+\epsilon(t).
 \tag{33}
\]

For example each hidden product is split into the residual difference
times the closure backward/forward pair, the dense residual times the
backward difference, and the dense residual times the forward difference.
The normalized rank-one bound gives exactly the three contributions in
(33). The first block has the same form with the fixed factor `X`.

Insert (30), (32) into (33), add the two inequalities, and use only
`Y<=1`, not a smallness threshold. This proves

\[
 d(t)\le C\epsilon(t)
       +C(1+\sqrt nY)\int_0^t\rho_D(u)d(u)\,du.
 \tag{34}
\]

For each terminal time, replace the nondecreasing inhomogeneous term by
its terminal value and apply the integral Gronwall inequality. By (18),

\[
 \sup_{t\ge0}d(t)
       \le C\epsilon(\infty)
           \exp\{C(1+\sqrt nY)Y\}
       =C\epsilon(\infty)e^{CY+C\sqrt nY^2}.
 \tag{35}
\]

Combining (1) and (35) proves (2). Neither exponential closure fitting,
closeness of the two residuals relative to either one, nor a width-uniform
parameter Lipschitz estimate has been used.

## 6. Quantifiers and boundaries

The integer `P_0` and all constants above depend only on `L,X,K,lambda`.
The claims hold simultaneously for every finite width satisfying (4),
every label sign and `0<Y<=1`, and every integer `P>=P_0`. The two finite
parameter limits are included in (2) by passage to the limit.

Equation (2) is bounded by
`C(1+sqrt(n)) exp(C sqrt(n))/P^2`; choosing the exponential constant in
(3) at least as large gives (3) directly. This is a sufficient, potentially
very expensive order schedule. No claim of its necessity or numerical
efficiency follows from this upper bound.

The argument also applies on any fixed bounded label interval after
recomputing constants. It does not prove the corresponding multi-sample
statement: both the scalar alignment quotient and the constant residual
direction are specific to one sample. It does not cover nonzero initial
readout without addressing the initial alignment and backward prefix jump.
Finally, no probabilistic initialization theorem or unrestricted
width-uniform fixed-order tracking theorem is asserted here.
